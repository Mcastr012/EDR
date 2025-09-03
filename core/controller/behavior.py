from utils.common import *
import view.message as msg
from db.elastic import ES
from config import *
from data.sysmon import SysmonData
from utils.log import *
import data.rule as rule
import data.attck as attck


def get_behavior(form):
    if not assert_keys_in_form_exist(form, ['behaviorType', 'endpointID', 'startDate',
                                            'endDate', 'pageSize', 'pageIndex']):
        return msg.error_msg("Invalid request.")

    startdate = form['startDate']
    enddate = form['endDate']
    behavior = form['behaviorType']
    eid = encode_md5(form['endpointID'])
    page_index = int(form['pageIndex'])
    page_size = int(form['pageSize'])

    if behavior not in ['ProcessBehavior', 'NetworkBehavior', 'FileBehavior', 'RegistryBehavior']:
        return msg.error_msg('Undefined behavior type.')

    index = 'raw' + '-' + behavior.lower()
    ts_tr = format_daterange((startdate, enddate))

    result = ES.query(_index=index, doctype='behavior', page_index=page_index, page_size=page_size, args={
        'bool': {
            'must': {
                'match': {
                    'endpoint.uuid': eid
                }
            },
            'filter': {
                'range': {
                    'timestamp': {
                        'gte': ts_tr[0],
                        'lte': ts_tr[1]
                    }
                }
            }
        }
    })

    # return msg.success_msg(result)
    return result

def load_behavior(form):
    if not assert_keys_in_form_exist(form, ['endpointID', 'startDate', 'endDate']):
        return msg.error_msg("Invalid request.")

    startdate = form['startDate']
    enddate = form['endDate']
    eid = form['endpointID']

    try:
        ts_tr = format_daterange((startdate, enddate))
        raw_data = ES.load(WINLOGBEAT_INDEX, '_doc', args={
            'bool': {
                'must': {
                    'match': {
                        'host.hostname': eid
                    }
                },
                'filter': {
                    'range': {
                        '@timestamp': {
                            'gte': ts_tr[0],
                            'lte': ts_tr[1]
                        }
                    }
                }
            }
        })
        behavior_list = []

        for _, e in raw_data.iterrows():
            eid = str(e['winlog']['event_id'])
            func = SysmonData.eventid_behavior_mappings(eid)

            if func:
                try:
                    props = [en.split(': ')[1] for en in e['message'].split('\n')[1:]]
                    mid = encode_md5(e['winlog']['computer_name'])
                    behav = func(eid, mid, props)
                    behavior_list.append(behav)
                except Exception as e:
                    log_error('Error: {} {}-{}'.format(e, eid, repr(props)))

        if behavior_list:
            ES.insert_behaviors('raw', behavior_list)

        # Detect abnormal behaviors
        attck_techs = attck.load_attcks(ATTCK_YAML)
        abnormals = rule.filter_abnormal_behaviors(behavior_list, attck_techs)

        if abnormals:
            ES.insert_behaviors('abnormal', abnormals)


    except Exception as e:
        log_error(e)
        return msg.error_msg("Fail to update bahavior.")

    return msg.success_msg({})


def get_abnormal(form):
    if not assert_keys_in_form_exist(form, ['behaviorType', 'endpointID', 'startDate',
                                            'endDate', 'pageSize', 'pageIndex']):
        return msg.error_msg("Invalid request.")

    startdate = form['startDate']
    enddate = form['endDate']
    behavior = form['behaviorType']
    eid = encode_md5(form['endpointID'])
    page_index = int(form['pageIndex'])
    page_size = int(form['pageSize'])

    if behavior not in ['ProcessBehavior', 'NetworkBehavior', 'FileBehavior', 'RegistryBehavior']:
        return msg.error_msg('Undefined behavior type.')

    index = 'abnormal' + '-' + behavior.lower()
    ts_tr = format_daterange((startdate, enddate))

    result = ES.query(_index=index, doctype='behavior', page_index=page_index, page_size=page_size, args={
        'bool': {
            'must': {
                'match': {
                    'endpoint.uuid': eid
                }
            },
            'filter': {
                'range': {
                    'timestamp': {
                        'gte': ts_tr[0],
                        'lte': ts_tr[1]
                    }
                }
            }
        }
    })

    # return msg.success_msg(result)
    return result