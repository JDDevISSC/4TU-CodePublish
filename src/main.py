from requests import HTTPError
from api.dataset_api import DatasetAPI
from util import metadata_helper
from config import Config
import json
import sys

class __main__:
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    
    dataset_api = DatasetAPI(Config())
    try:
        metadata_json = metadata_helper.prepare_dataset("dataset_example.json")
        response = dataset_api.create_dataset(json.loads(metadata_json))
        dataset_id = dataset_api.retrieve_dataset_id_from_response(response)
        dataset_api.put_dataset_details(dataset_id, metadata_json)
        dataset_json = json.dumps(dataset_api.get_dataset(dataset_id))
        print(dataset_json)
    except HTTPError as e:
        print(e)