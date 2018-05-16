from datetime import timedelta, datetime

from elasticsearch import Elasticsearch
from elasticsearch_dsl import DocType, Date, Text, Keyword, Integer, Search
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
from elasticsearch_dsl.query import Range

from config import Config

connections.create_connection(hosts=Config.ES_URI)

class RecallDocumentMeta:
    index = 'fdk-recalls.v0.9'
    type = 'recall'

class Recall(DocType):
    announced_date = Date()
    title = Text(fields={'raw': Keyword()})
    description = Text()
    hazard = Text(fields={'raw': Keyword()})
    product = Text(fields={'raw': Keyword()})
    announced_in = Text(fields={'raw': Keyword()})
    fdk_id = Integer()
    origin = Text(fields={'raw': Keyword()})

    class Meta:
        index = 'fdk-recalls.v0.9'
        type = 'recall'

    def save(self, **kwargs):
        return super(Recall, self).save(id=self.fdk_id, **kwargs)

    def search(self):

        todate=self.announced_date + timedelta(days=7)
        fromdate=self.announced_date - timedelta(days=7)

        s = Search(index=RecallDocumentMeta.index) \
            .query("match", hazard=self.hazard) \
            .query("match", announced_in=self.announced_in) \
            .query(Range(announced_date={'gte':fromdate, 'lte':todate}))

        count = s.count()
        response = s[0:count].execute()

        possibly = {}
        hits = []
        for hit in response:
            hits.append(hit.fdk_id)

        possibly['similar'] = hits

        return possibly
