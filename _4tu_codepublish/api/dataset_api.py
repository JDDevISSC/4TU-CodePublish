import logging
import sys
from urllib import response
import requests
import json
from _4tu_codepublish.conf.config import Config

class DatasetAPI():
    def __init__(self, config=None):
        if not isinstance(config, Config):
            raise TypeError("config must be an instance of the Config class.")
        self._config = config
        self._logger = logging.getLogger(__name__)
        
    @property
    def config(self):
        """Gets the config of this DatasetAPI.  

        Config for DatasetAPI  

        :return: The config of this DatasetAPI.  
        :rtype: config
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this DatasetAPI.

        Config for DatasetAPI  

        :param config: The config of this DatasetAPI.  
        :type: config
        """
        if config is None:
            raise ValueError("config value for `config`, must not be `None`")  

        self._config = config
        
    @property
    def logger(self):
        """Gets the logger of this DatasetAPI.  

        Logger for DatasetAPI  

        :return: The logger of this DatasetAPI.  
        :rtype: Logger
        """
        return self._logger

    @logger.setter
    def logger(self, logger):
        """Sets the logger of this DatasetAPI.

        Logger for DatasetAPI  

        :param logger: The logger of this DatasetAPI.  
        :type: Logger
        """
        if logger is None:
            raise ValueError("logger value for `logger`, must not be `None`")  

        self._logger = logger
            
    def _post(self, endpoint, json):
        try:    
            headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
            response = requests.post(f"{self._config.base_url}{endpoint}", json=json, headers=headers)
            response.raise_for_status()  # Raises an error for 4XX/5XX responses
            return response
        except Exception as e:
            self.logger.error(f"Failed to post to {self._config.base_url}{endpoint}. With message: {e}")
            self.logger.debug(f"JSON: {json}")
            sys.exit()
            
    def _get(self, endpoint):
        try:
            headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
            response = requests.get(f"{self._config.base_url}{endpoint}", headers=headers)
            response.raise_for_status()  # Raises an error for 4XX/5XX responses
            return response
        except Exception as e:
            self.logger.error(f"Failed to get from {self._config.base_url}{endpoint}. With message: {e}")
            sys.exit()
                
    def _put(self, endpoint, json):
        try:
            headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
            response = requests.put(f"{self._config.base_url}{endpoint}", json=json, headers=headers)
            response.raise_for_status()  # Raises an error for 4XX/5XX responses
        except Exception as e:
            self.logger.error(f"Failed to put to {self._config.base_url}{endpoint}. With message: {e}")
            sys.exit()            

    def create_dataset(self, metadata):
        """Creates a dataset on 4TUResearchData
        
        """
        self.logger.info("Creating dataset.")
        response = self._post("/v2/account/articles", metadata)
        return json.loads(response.text)
    
    def get_datasets(self):
        """Gets all datasets belonging to the user
        
        """
        self.logger.info("Getting datasets.")
        response = self._get("/v2/account/articles")
        return response
        
    def get_dataset(self, dataset_id):
        """Get dataset with dataset_id
        
        """
        self.logger.info(f"Get dataset with dataset_id ({dataset_id}).")
        response = self._get(f"/v2/account/articles/{dataset_id}")
        return json.loads(response.content)
    
    def search_authors(self, search_string):
        """Search author with search_string
        
        """
        self.logger.info(f"Searching author with search_string ({search_string}).")
        # Search Authors: POST http://127.0.0.1:8080/v2/account/authors/search
        search_json = { "search": search_string }
        response = self._post("/v2/account/authors/search", search_json)
        return json.loads(response.text)
    
    def get_licenses(self):
        """Get licenses that are available on the instance
        
        """
        self.logger.info("Getting licenses")
        # Get available licenses: GET http://127.0.0.1:8080/v2/licenses
        response = self._get("/v2/licenses")
        return json.loads(response.text)

    def get_authors_for_dataset(self, dataset_id, limit=10000):
        """Get authors for dataset with dataset_id
        
        """
        self.logger.info(f"Getting authors for dataset with dataset_id ({dataset_id}).")
        self.logger.debug(f"limit:{limit}")
        # Get authors for dataset: GET http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848/authors?limit=10000
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/v3/datasets/{dataset_id}/authors?{limit}", headers=headers)
        return json.loads(response.text)
    
    def get_collaborators_for_dataset(self, dataset_id, limit=10000, order="id", order_direction="asc"):
        """Get collaborators for dataset with dataset_id
        
        """
        self.logger.info(f"Getting collaborators for dataset with dataset_id ({dataset_id}).")
        self.logger.debug(f"limit={limit}, order={order}, order_direction={order_direction}")
        # Get collaborators: GET http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848/collaborators?limit=10000&order=id&order_direction=asc
        response = self._get(f"/v3/datasets/{dataset_id}/collaborators?{limit}?order={order}?order_direction={order_direction}")
        return json.loads(response.text)
    
    def get_references_for_dataset(self, dataset_id, limit=10000, order="id", order_direction="asc"):
        """Get references for dataset with dataset_id
        
        """
        self.logger.info(f"Getting references for dataset with dataset_id ({dataset_id}).")
        self.logger.debug(f"limit={limit}, order={order}, order_direction={order_direction}")
        # Get references for dataset: GET http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848/references?limit=10000&order=asc&order_direction=id
        response = self._get(f"/v3/datasets/{dataset_id}/references?{limit}?order={order}?order_direction={order_direction}")
        return json.loads(response.text)
            
    def get_tags_for_dataset(self, dataset_id, limit=10000):
        """Get tags for dataset with dataset_id
        
        """
        self.logger.info(f"Getting tags for dataset with dataset_id ({dataset_id}).")
        self.logger.debug(f"limit={limit}")
        # Get tags for dataset: GET http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848/tags?limit=10000
        response = self._get(f"/v3/datasets/{dataset_id}/tags?{limit}")
        return json.loads(response.text)
    
    def get_funding_for_dataset(self, dataset_id, limit=10000, order="id", order_direction="asc"):
        """Get funding for dataset with dataset_id
        
        """
        self.logger.info(f"Getting funding for dataset with dataset_id ({dataset_id}).")
        self.logger.debug(f"limit={limit}, order={order}, order_direction={order_direction}")
        # Get funding for dataset: GET http://127.0.0.1:8080/v2/account/articles/556cb091-9b73-45f2-85c7-d7a97465d848/funding?limit=10000&order=id&order_direction=asc
        response = self._get(f"/v2/account/articles/{dataset_id}/funding?{limit}?order={order}?order_direction={order_direction}")
        return json.loads(response.text)
    
    def get_categories(self):
        """Get categories
        
        """
        self.logger.info("Getting categories.")
        # Get categories: GET http://127.0.0.1:8080/v2/categories
        response = self._get("/v2/categories")
        return json.loads(response.text)   
    
    def get_categories_for_dataset(self, dataset_id, limit=10000):
        """Get categories for dataset with dataset_id
        
        """
        self.logger.info(f"Getting categories for dataset with dataset_id ({dataset_id}).")
        self.logger.debug(f"limit={limit}")
        # Get categories for datset: GET http://127.0.0.1:8080/v2/account/articles/556cb091-9b73-45f2-85c7-d7a97465d848/categories?limit=10000
        response = self._get(f"/v2/account/articles/{dataset_id}/categories?{limit}")
        return json.loads(response.text)        
    
    def get_git_branches_for_dataset(self, dataset_id):
        """Get git branches for dataset with dataset_id
        
        """
        self.logger.info(f"Getting git branches for dataset with dataset_id ({dataset_id}).")
        # Get git branches for dataset: GET http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848.git/branches
        response = self._get(f"/v3/datasets/{dataset_id}.git/branches")
        return json.loads(response.text)
    
    def put_dataset_details(self, dataset_id, metadata):
        """Update dataset with dataset_id with metadata
        
        """
        self.logger.info(f"Updating dataset with dataset_id ({dataset_id}).")
        self.logger.debug(metadata)
        response = self._put(f"/v2/account/articles/{dataset_id}", metadata)
        return response
    
    def put_default_branch_for_dataset(self, dataset_id, branch=None):
        """Set default branch for dataset with dataset_id
        
        """
        self.logger.info(f"Setting default branch for dataset with dataset_id ({dataset_id}).")
        self.logger.debug(f"branch={branch}")
        # Set default branch for dataset: PUT http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848.git/set-default-branch
        if branch == None:
            raise ValueError("Invalid value for `branch`, must not be `None`")
        default_branch_json = { "branch": branch }
        response = self._put(f"/v3/datasets/{dataset_id}.git/set-default-branch", default_branch_json)
        return response
    
    def post_tags_for_dataset(self, dataset_id, tags={"tags": []}):
        """Set tags for dataset with dataset_id
        
        """
        self.logger.info(f"Setting tags for dataset with dataset_id ({dataset_id}).")
        self.logger.debug(f"tags={tags}")
        # http://127.0.0.1:8080/v3/datasets/556cb091-9b73-45f2-85c7-d7a97465d848/tags
        response = self._post(f"/v3/datasets/{dataset_id}/tags", tags)
        return response