import json
import logging
from urllib.parse import urlparse

class NoMetadataError(Exception):
    "Raised when the metadata is None"
    pass

def prepare_dataset_metadata(metadata_path):
    logging.debug(f"Preparing dataset metadata with metadata path: {metadata_path}")
    metadata = _load_metadata_from_file(metadata_path)
    if metadata != None or metadata == "":
        logging.debug("Loaded metadata:")
        logging.debug(metadata)
        return metadata
    else:
        raise NoMetadataError

def _load_metadata_from_file(path):
    with open(path, "r") as file:
        metadata = ""
        metadata = file.read()
        file.close
    return metadata

    
def retrieve_dataset_id_from_response(response):
    """Retrieve dataset_id from from response
    
    """
    logging.debug(f"Retrieving dataset_id from response:")
    logging.debug(response)
    parsed_url = urlparse(response['location'])
    uuid = parsed_url.path.split('/')[-1]
    logging.debug(f"Found uuid ({uuid})")
    return uuid