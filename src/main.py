from requests import HTTPError
from api.dataset_api import DatasetAPI
from util import metadata_helper
from model.dataset import Dataset, DatasetDecoder, DatasetEncoder
from config import Config
import json

class __main__:
    dataset_api = DatasetAPI(Config())
    try:
        dataset = metadata_helper.create_dataset_metadata("dataset_example.json", "", "")
        print(dataset)
        metadata_json = json.dumps(dataset, indent=2, cls=DatasetEncoder)
        response = json.loads(dataset_api.create_dataset(metadata_json).text)
        print (json.dumps(response, indent=2))
        
    except HTTPError as e:
        print(e)

    
    