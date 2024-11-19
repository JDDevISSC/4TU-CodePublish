from dotenv import load_dotenv
import os

load_dotenv()

API_TOKEN = os.getenv("4TU_API_TOKEN")
BASE_URL = os.getenv("4TU_BASE_URL")
LOG_LEVEL = os.getenv("4TU_LOG_LEVEL")
LOG_FILE = os.getenv("4TU_LOG_FILE")
OUTPUT_FILE = os.getenv("4TU_OUTPUT_FILE")

class Config():
    def __init__(self, api_token=API_TOKEN, base_url=BASE_URL, log_level=LOG_LEVEL, log_file=LOG_FILE, output=OUTPUT_FILE):
        self._api_token = api_token
        self._base_url = base_url
        self._log_level = log_level
        self._log_file = log_file
        self._output = output
        
    @property
    def output(self):
        """Gets the output of this Config.  

        output for Config  

        :return: The output of this Config.  
        :rtype: str
        """
        return self._output

    @output.setter
    def log_file(self, output):
        """Sets the output for this Config.

        output for Config 

        :param output: The output for this Config.  
        :type: str
        """
        self._output = output

    @property
    def log_file(self):
        """Gets the log_file of this Config.  

        log_file for Config  

        :return: The log_file of this Config.  
        :rtype: str
        """
        return self._log_file

    @log_file.setter
    def log_file(self, log_file):
        """Sets the log_file for this Config.

        log_file for Config 

        :param log_file: The log_file for this Config.  
        :type: str
        """
        if log_file is None:
            raise ValueError("Invalid log_file value for `log_file`, must not be `None`")  

        self._log_file = log_file
        
    @property
    def log_level(self):
        """Gets the log_level of this Config.  

        log_level for Config  

        :return: The log_level of this Config.  
        :rtype: str
        """
        return self._log_level.upper()

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level for this Config.

        log_level for Config 

        :param log_level: The log_level for this Config.  
        :type: str
        """
        if log_level is None:
            raise ValueError("Invalid config value for `log_level`, must not be `None`")  

        self._log_level = log_level.upper()
        
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