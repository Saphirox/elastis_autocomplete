from operator import index

from elasticsearch import Elasticsearch, helpers

es = Elasticsearch("https://elastic:changeme@localhost:9200", verify_certs=False)

def generate_data(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield {
                "_index": "my_index",
                "_source": {
                    "my_field": line.strip()
                }
            }

helpers.bulk(es, generate_data('words.txt'))
