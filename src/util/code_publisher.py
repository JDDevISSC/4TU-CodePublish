import json
from requests import HTTPError
from api import dataset_api
from util import metadata_helper


def publish(): 
    # The following methods can be used to generate a local JSON file for the user.
    search_results = dataset_api.search_authors("Jori")
    response = dataset_api.get_licenses()
    response = dataset_api.get_categories()
    response = dataset_api.get_authors_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
    # Collaborators are in Beta and I'm having some trouble getting collaborators to save
    # On the current Djehuty build.
    # response = dataset_api.get_collaborators_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
    response = dataset_api.get_references_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
    response = dataset_api.get_tags_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
    response = dataset_api.get_funding_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
    response = dataset_api.get_categories_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
    response = dataset_api.get_git_branches_for_dataset("556cb091-9b73-45f2-85c7-d7a97465d848")
    
    # Example flow
    ## Prepare metadata by reading it from a local JSON file
    metadata_json = metadata_helper.prepare_dataset_metadata("dataset_example.json")
    ## Create dataset on instance with metadata
    response = dataset_api.create_dataset(metadata_json)
    ## Using the response we'll retrieve the dataset_id from it
    dataset_id = metadata_helper.retrieve_dataset_id_from_response(response)
    ## With the dataset_id we can update the dataset with extra metadata that can't be added during the dataset creation
    dataset_api.put_dataset_details(dataset_id, metadata_json)
    response = dataset_api.put_default_branch_for_dataset(dataset_id, "master")
    response = dataset_api.post_tags_for_dataset(dataset_id, {"tags": ["keyword 1", "keyword 2"]})
    ## Get the dataset's metadata from the instance.
    dataset_json = json.dumps(dataset_api.get_dataset(dataset_id))