import logging
from urllib.parse import urlparse

class NoMetadataError(Exception):
    "Raised when the metadata is None"
    pass

def prepare_dataset_metadata(metadata_path):
    """Prepares metadata for use with the DatasetAPI by reading JSON from a file
    
    """
    logging.getLogger(prepare_dataset_metadata.__name__).debug(f"Preparing dataset metadata with metadata path: {metadata_path}")
    metadata = _load_metadata_from_file(metadata_path)
    if metadata != None or metadata == "":
        logging.getLogger(prepare_dataset_metadata.__name__).debug("Loaded metadata:")
        logging.getLogger(prepare_dataset_metadata.__name__).debug(metadata)
        return metadata
    else:
        raise NoMetadataError
    
def retrieve_dataset_id_from_response(response):
    """Retrieve dataset_id from from response
    
    """
    logging.getLogger(retrieve_dataset_id_from_response.__name__).debug(f"Retrieving dataset_id from response:")
    logging.getLogger(retrieve_dataset_id_from_response.__name__).debug(response)
    parsed_url = urlparse(response['location'])
    uuid = parsed_url.path.split('/')[-1]
    logging.getLogger(retrieve_dataset_id_from_response.__name__).debug(f"Found uuid ({uuid})")
    return uuid

def _load_metadata_from_file(path):
    with open(path, "r") as file:
        metadata = ""
        metadata = file.read()
        file.close
    return metadata