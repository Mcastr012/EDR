from controller.behavior import *
import data.attck as attck
import data.rule as rule

form = {
    "behaviorType" : "ProcessBehavior",
    "endpointID" : "DESKTOP-3LRRD6K",
    "startDate" : "2020-04-08",
    "endDate" : "2020-04-08",
    "pageSize" : "10",
    "pageIndex" : "0"
}

ts_tr = format_daterange(('2020-04-05', '2020-04-07'))
raw_data = ES.load(WINLOGBEAT_INDEX, '_doc', args={
    'bool': {
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

attck_techs = attck.load_attcks('../attck.yaml')

abnormals = rule.filter_abnormal_behaviors(behavior_list, attck_techs)

for abnormal in abnormals:
    print(str(abnormal.attck_ids) + '###' + str(abnormal))
