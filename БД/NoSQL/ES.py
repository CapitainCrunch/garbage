__author__ = 'Bogdan'
from elasticsearch import Elasticsearch
# encoding=utf-8
class ES(object):
    def __init__(self):
        self.es = Elasticsearch()
        self.id = 0

    def insert_es(self, id, good, description):
        doc = {
            'id': id,
            'good': good,
            'description': description
            }
        res = self.es.index(index="test-index", doc_type='description_goods', id=self.id, body=doc)
        print(res['created'])
        res = self.es.get(index="test-index", doc_type='description_goods', id=self.id)
        print(res['_source'])
        self.es.indices.refresh(index="test-index")
        self.id += 1

    def search_es(self, what, query):
        res = self.es.search(index="test-index", body={"query": {"match": {what: query}}})  #"author": 'kimchy'
        print("Got %d Hits" % res['hits']['total'])
        documents = []
        for hit in res['hits']['hits']:
            print hit
            documents.append(hit['_source'])
        return documents

    def del_by_query(self, query):
        res = self.es.delete_by_query(index="test-index", body={"query": {"match": {query}}}) #{"match_all": {}}

    def del_all(self):
        res = self.es.delete_by_query(index="test-index", body={"query": {"match_all": {}}}) #{"match_all": {}}