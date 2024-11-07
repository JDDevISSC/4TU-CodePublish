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
        response = requests.post(f" {self._config.base_url}/account/articles", json=metadata, headers=headers)
        response.raise_for_status()  # Raises an error for 4XX/5XX responses
        return json.loads(response.text)
    
    def get_datasets(self, metadata):
        """Gets all datasets belonging to the user from 4TUResearchData
        
        """
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/account/articles", json=metadata, headers=headers)
        response.raise_for_status()  # Raises an error for 4XX/5XX responses
        return response
    
    def put_dataset_details(self, dataset_id, metadata):
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.put(f"{self._config.base_url}/account/articles/{dataset_id}", json=metadata, headers=headers)
        response.raise_for_status()  # Raises an error for 4XX/5XX responses
        
        
    def get_dataset(self, dataset_id):
        headers = {"Authorization": f"token {self._config.api_token}", "Content-Type": "application/json"}
        response = requests.get(f"{self._config.base_url}/account/articles/{dataset_id}", headers=headers)
        response.raise_for_status()  # Raises an error for 4XX/5XX responses
        return json.loads(response.content)
    
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
    
    