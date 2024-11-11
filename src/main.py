import logging
from requests import HTTPError
from api.dataset_api import DatasetAPI
from util import log_helper, metadata_helper
from config import Config
import json
import sys

class __main__:
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    config = Config()
    log_helper.setup_logging(config.log_level, config.log_file)
    logging.info("Starting 4TU-CODEPUBLISH")
    dataset_api = DatasetAPI(config)
    try:
        
        # The following methods can be used to generate a local JSON file for the user.
        search_results = dataset_api.search_authors("Jori")
        response = dataset_api.get_licenses()
        response = dataset_api.get_authors_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_collaborators_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_references_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_tags_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_funding_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_categories_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_git_branches_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        
        # Example flow
        ## Prepare metadata by reading it from a local JSON file
        metadata_json = metadata_helper.prepare_dataset_metadata("dataset_example.json")
        ## Create dataset on instance with metadata
        response = dataset_api.create_dataset(json.loads(metadata_json))
        ## Using the response we'll retrieve the dataset_id from it
        dataset_id = metadata_helper.retrieve_dataset_id_from_response(response)
        ## With the dataset_id we can update the dataset with extra metadata that can't be added during the dataset creation
        dataset_api.put_dataset_details(dataset_id, metadata_json)
        response = dataset_api.set_default_branch_for_dataset(dataset_id, "master")
        ## Get the dataset's metadata from the instance.
        dataset_json = json.dumps(dataset_api.get_dataset(dataset_id))
    except HTTPError as e:
        print(e)