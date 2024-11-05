import json
from model.dataset import Dataset
from types import SimpleNamespace

from model.dataset import Dataset, DatasetDecoder

class NoMetadataError(Exception):
    "Raised when the metadata is None"
    pass

def create_dataset_metadata(dataset_path, references_path, tags_path):
   dataset =  _load_metadata_from_file(dataset_path)
   return dataset

def _load_metadata_from_file(path):
    with open(path, "r") as file:
        metadata = ""
        metadata = file.read()
        file.close
    if metadata != None or metadata == "":
        return _convert_json_to_object(metadata)
    else:
        raise NoMetadataError
    
def _convert_json_to_object(json_data):
    return json.loads(json_data, object_hook=DatasetDecoder)