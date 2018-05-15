from elasticsearch_dsl import DocType, Date, Text, Keyword, Integer
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
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

    def save(self, **kwargs):
        return super(Recall, self).save(id=self.fdk_id, **kwargs)

    class Meta:
        index = 'fdk-recalls.v0.9'
        type = 'recall'