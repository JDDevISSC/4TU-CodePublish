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
        # search_results = dataset_api.search_authors("Jori")
        # print(search_results)
        
        response = dataset_api.get_licenses()
        

        response = dataset_api.get_authors_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_collaborators_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_references_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_tags_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_funding_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_categories_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.get_git_branches_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
        response = dataset_api.set_default_branch_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848", "master")
        
        metadata_json = metadata_helper.prepare_dataset("dataset_example.json")
        response = dataset_api.create_dataset(json.loads(metadata_json))
        dataset_id = dataset_api.retrieve_dataset_id_from_response(response)
        dataset_api.put_dataset_details(dataset_id, metadata_json)
        dataset_json = json.dumps(dataset_api.get_dataset(dataset_id))
        print(dataset_json)
    except HTTPError as e:
        print(e)