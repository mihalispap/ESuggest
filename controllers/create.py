from flask import Flask, request

from config import Config
from models.documents import Recall, RecallDocumentMeta
import pandas as pd
import json

app = Flask(__name__)


def create_index():
    Recall.init()

    resp = {'status': 'OK'}
    return pd.Series(resp).to_json()


def create_recall():
    content = request.get_json(silent=True, force=True)
    print(content)

    rdoc = Recall()

    rdoc.product = content['product']
    rdoc.hazard = content['hazard']
    rdoc.title = content['title']
    rdoc.fdk_id = content['fdk_id']
    rdoc.description = content['description']
    rdoc.announced_date = content['announced_date']
    rdoc.announced_in = content['announced_in']
    rdoc.origin = content['origin']

    rdoc.save()

    resp = {'status': 'OK'}
    return pd.Series(resp).to_json()
