from elasticsearch import Elasticsearch, helpers
import pandas

from utils.log import *
from config import *


class ES:
    es = None

    @classmethod
    def connect(cls):
        cls.es = Elasticsearch([ES_HOST])

    @classmethod
    def insert_behaviors(cls, _index, data):
        records = []
        for _be in data:
            if _be is None:
                continue

            _cols = _be.get_attribute_names()
            _record = _be.serialize()

            try:
                records.append({
                    '_index': _index + '-' + _be.getname().lower(),
                    '_type': 'behavior',
                    '_source': pandas.DataFrame([_record], columns=_cols).loc[0].to_json(default_handler=str),
                })
            except Exception as e:
                log_error('Elasticsearch insert failed. {}'.format(e))
                log_error(pandas.DataFrame([_record], columns=_cols).loc[0])

        helpers.bulk(cls.es, records)

    @classmethod
    def load(cls, _index, doctype, args):
        records = []
        try:
            page = cls.es.search(index=_index, doc_type=doctype, scroll='2m', size=1000, timeout='10m', body={
                "query" : args,
            })

            sid = page['_scroll_id']
            scroll_size = page['hits']['total']['value']
            docs = page['hits']['hits']
            records += [x['_source'] for x in docs]

            while scroll_size > 0:
                page = cls.es.scroll(scroll_id=sid, scroll='5m')
                sid = page['_scroll_id']
                scroll_size = len(page['hits']['hits'])
                docs = page['hits']['hits']
                records += [x['_source'] for x in docs]
            return pandas.DataFrame(records)

        except Exception as e:
            log_error('Elasticsearch query failed. {}'.format(e))
            return pandas.DataFrame([])

    @classmethod
    def query(cls, _index, doctype, args, page_size, page_index):
        records = []
        try:
            page = cls.es.search(index=_index, doc_type=doctype, body={
                "query": args,
                "from": page_index * page_size,
                "size": page_size
            })
            docs = page['hits']['hits']
            records += [x['_source'] for x in docs]
            return records

        except Exception as e:
            log_error('Elasticsearch query failed. {}'.format(e))
            return records


ES.connect()
