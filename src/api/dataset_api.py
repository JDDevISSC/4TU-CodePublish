import requests
from config import Config
from urllib.parse import urlparse
import json

class DatasetAPI():
    
    def __init__(self, config=None):
        if not isinstance(config, Config):
            raise TypeError("config must be an instance of the Config class.")
        self._config = config
        
    @property
    def config(self):
        """Gets the config of this DatasetAPI.  

        Config for Dataset  

        :return: The config of this Dataset.  
        :rtype: config
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this Dataset.

        Unique configentifier for Dataset  

        :param config: The config of this Dataset.  
        :type: config
        """
        if config is None:
            raise ValueError("Invalconfig value for `config`, must not be `None`")  

        self._config = config
    
    def create_dataset(self, metadata):
        """Creates a dataset on 4TUResearchData
        
        """
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.post(f" {self._config.base_url}/v2/account/articles", json=metadata, headers=headers)
        response.raise_for_status()  # Raises an error for 4XX/5XX responses
        return json.loads(response.text)
    
    def get_datasets(self, metadata):
        """Gets all datasets belonging to the user from 4TUResearchData
        
        """
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/v2/account/articles", json=metadata, headers=headers)
        response.raise_for_status()  # Raises an error for 4XX/5XX responses
        return response
    
    def put_dataset_details(self, dataset_id, metadata):
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.put(f"{self._config.base_url}/v2/account/articles/{dataset_id}", json=metadata, headers=headers)
        response.raise_for_status()  # Raises an error for 4XX/5XX responses
        
        
    def get_dataset(self, dataset_id):
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/v2/account/articles/{dataset_id}", headers=headers)
        response.raise_for_status()  # Raises an error for 4XX/5XX responses
        return json.loads(response.content)
    
    def search_authors(self, search_string):
        # Search Authors: POST http://127.0.0.1:8080/v2/account/authors/search
        search_json = { "search": search_string }
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.post(f"{self._config.base_url}/v2/account/authors/search", json=search_json, headers=headers)
        return json.loads(response.text)
    
    def get_licenses(self):
        # Get available licenses: GET http://127.0.0.1:8080/v2/licenses
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/v2/licenses", headers=headers)
        return json.loads(response.text)

    def get_authors_for_dataset(self, dataset_id, limit=10000):
        # Get authors for dataset: GET http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848/authors?limit=10000
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/v3/datasets/{dataset_id}/authors?{limit}", headers=headers)
        return json.loads(response.text)
    
    def get_collaborators_for_dataset(self, dataset_id, limit=10000, order="id", order_direction="asc"):
        # Get collaborators: GET http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848/collaborators?limit=10000&order=id&order_direction=asc
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/v3/datasets/{dataset_id}/collaborators?{limit}?order={order}?order_direction={order_direction}", headers=headers)
        return json.loads(response.text)
    
    def get_references_for_dataset(self, dataset_id, limit=10000, order="id", order_direction="asc"):
        # Get references for dataset: GET http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848/references?limit=10000&order=asc&order_direction=id
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/v3/datasets/{dataset_id}/references?{limit}?order={order}?order_direction={order_direction}", headers=headers)
        return json.loads(response.text)
            
    def get_tags_for_dataset(self, dataset_id, limit=10000):
        # Get tags for dataset: GET http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848/tags?limit=10000
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/v3/datasets/{dataset_id}/tags?{limit}", headers=headers)
        return json.loads(response.text)
    
    def get_funding_for_dataset(self, dataset_id, limit=10000, order="id", order_direction="asc"):
        # Get funding for dataset: GET http://127.0.0.1:8080/v2/account/articles/556cb091-9b73-45f2-85c7-d7a97465d848/funding?limit=10000&order=id&order_direction=asc
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/v2/account/articles/{dataset_id}/funding?{limit}?order={order}?order_direction={order_direction}", headers=headers)
        return json.loads(response.text)
    
    def get_categories_for_dataset(self, dataset_id, limit=10000):
        # Get categories for datset: GET http://127.0.0.1:8080/v2/account/articles/556cb091-9b73-45f2-85c7-d7a97465d848/categories?limit=10000
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/v2/account/articles/{dataset_id}/categories?{limit}", headers=headers)
        return json.loads(response.text)        
    
    def get_git_branches_for_dataset(self, dataset_id):    
        # Get git branches for dataset: GET http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848.git/branches
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/v3/datasets/{dataset_id}.git/branches", headers=headers)
        return json.loads(response.text)
    
    def set_default_branch_for_dataset(self, dataset_id, branch=None):
        # Set default branch for dataset: PUT http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848.git/set-default-branch
        if branch == None:
            raise ValueError("Invalid value for `branch`, must not be `None`")
        default_branch_json = { "branch": branch }
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.put(f"{self._config.base_url}/v3/datasets/{dataset_id}.git/set-default-branch", json=default_branch_json, headers=headers)
        return response
    
    def retrieve_dataset_id_from_response(self, response):
        """Retrieve dataset_id from from response
        
        """
        parsed_url = urlparse(response['location'])
        uuid = parsed_url.path.split('/')[-1]
        return uuid
    
    def push_gitrepo():
        """Push git repository to git remote on 4TUResearchData
        
        """
        response = None
        return response
    
    def publish_dataset():
        """Publish a dataset on 4TUResearchData
        
        """
        response = None
        return response
    
    