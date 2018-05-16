import pandas as pd

from flask import request

from models.documents import Recall


def search_similar_recall():
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

    possibly = rdoc.search()
    return pd.Series(possibly).to_json()
