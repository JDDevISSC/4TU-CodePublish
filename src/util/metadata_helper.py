import json

class NoMetadataError(Exception):
    "Raised when the metadata is None"
    pass

def prepare_dataset(metadata_path):
    metadata = _load_metadata_from_file(metadata_path)
    if metadata != None or metadata == "":
        return metadata
    else:
        raise NoMetadataError

def _load_metadata_from_file(path):
    with open(path, "r") as file:
        metadata = ""
        metadata = file.read()
        file.close
    return metadata