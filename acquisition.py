import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['preferences_db']
collection_surv_results = db['surv_results']

for ans in range(1005):
    with open("chunck_%04d.jsonl" % ans, "r+") as f:
        file_data = json.load(f)
        # .insert is deprecated in favor of insert_one, but with .insert we can use check_keys=False to avoid issues with json keys having '.' characters. May be worth further investigation.
        collection_surv_results.insert(file_data, check_keys=False)

"""
#* Testing the very first json file to ensure it worked.
with open("chunck_0000.jsonl", "r+") as f:
        file_data = json.load(f)
        collection_surv_results.insert(file_data, check_keys=False)
"""

client.close()