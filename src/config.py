from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("4TU_API_TOKEN")
BASE_URL = "http://127.0.0.1:8080"

class Config():
    def __init__(self, api_token=API_TOKEN, base_url=BASE_URL):
        self._api_token = api_token
        self._base_url = base_url
        
    @property
    def api_token(self):
        """Gets the api_token of this Config.  

        api_token for Config  

        :return: The api_token of this Config.  
        :rtype: str
        """
        return self._api_token

    @api_token.setter
    def api_token(self, api_token):
        """Sets the api_token for this Config.

        api_token for Config 

        :param api_token: The api_token for this Config.  
        :type: str
        """
        if api_token is None:
            raise ValueError("Invalid config value for `api_token`, must not be `None`")  

        self._api_token = api_token
        
    @property
    def base_url(self):
        """Gets the base_url of this Config.  

        base_url for Config  

        :return: The base_url of this Config.  
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this Config.

        base_url for Config 

        :param base_url: The base_url for this Config.  
        :type: str
        """
        if base_url is None:
            raise ValueError("Invalconfig value for `base_url`, must not be `None`")  

        self._base_url = base_url