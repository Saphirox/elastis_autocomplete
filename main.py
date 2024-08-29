import os

from elasticsearch import Elasticsearch
from flask import Flask, request, jsonify

es = Elasticsearch("https://elastic:changeme@localhost:9200", verify_certs=False)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def todo():
    es_query =  {
            "match": {
                "my_field": {
                    "query": request.args.get("text"),
                    "analyzer": "trigrams",
                    "minimum_should_match": "2<75%"
                }
            }
        }

    search = es.search(index="my_index", query=es_query)
    return jsonify(list(map(lambda x: x['_source']['my_field'], search["hits"]["hits"])))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9091), debug=True)
