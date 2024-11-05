import pprint
from collections import namedtuple
from json import JSONEncoder

def DatasetDecoder(datasetDict):
    return namedtuple('Dataset', datasetDict.keys())(*datasetDict.values())

class DatasetEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
    

class Dataset(object):
    """
    Attributes:
      types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    types = {
        'id': 'int',
        'uuid': 'str',
        'title': 'str',
        'doi': 'str',
        'handle': 'str',
        'url': 'str',
        'url_public_html': 'str',
        'url_public_api': 'str',
        'url_private_html': 'str',
        'url_private_api': 'str',
        'timeline': 'str',
        'thumb': 'str',
        'defined_type': 'int',
        'defined_type_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'uuid': 'uuid',
        'title': 'title',
        'doi': 'doi',
        'handle': 'handle',
        'url': 'url',
        'url_public_html': 'url_public_html',
        'url_public_api': 'url_public_api',
        'url_private_html': 'url_private_html',
        'url_private_api': 'url_private_api',
        'timeline': 'timeline',
        'thumb': 'thumb',
        'defined_type': 'defined_type',
        'defined_type_name': 'defined_type_name'
    }

    def __init__(self, id=None, uuid=None, title=None, doi=None, handle=None, url=None, url_public_html=None, url_public_api=None, url_private_html=None, url_private_api=None, timeline=None, thumb=None, defined_type=None, defined_type_name=None):  
        """Article"""  
        self._id = None
        self._uuid = None
        self._title = None
        self._doi = None
        self._handle = None
        self._url = None
        self._url_public_html = None
        self._url_public_api = None
        self._url_private_html = None
        self._url_private_api = None
        self._timeline = None
        self._thumb = None
        self._defined_type = None
        self._defined_type_name = None
        self.discriminator = None
        self.id = id
        self.title = title
        self.doi = doi
        self.handle = handle
        self.url = url
        self.url_public_html = url_public_html
        self.url_public_api = url_public_api
        self.url_private_html = url_private_html
        self.url_private_api = url_private_api
        self.timeline = timeline
        self.thumb = thumb
        self.defined_type = defined_type
        self.defined_type_name = defined_type_name

    @property
    def id(self):
        """Gets the id of this Article.  

        Unique identifier for article  

        :return: The id of this Article.  
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Article.

        Unique identifier for article  

        :param id: The id of this Article.  
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  

        self._id = id

    @property
    def uuid(self):
        """Gets the uuid of this Article.  

        Unique identifier for article  

        :return: The uuid of this Article.  
        :rtype: str
        """
        return self._id

    @uuid.setter
    def uuid(self, uuid):
        """Sets the id of this Article.

        Unique identifier for article  

        :param id: The id of this Article.  
        :type: int
        """
        if uuid is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  

        self._uuid = uuid

    @property
    def title(self):
        """Gets the title of this Article.  

        Title of article  

        :return: The title of this Article.  
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Article.

        Title of article  

        :param title: The title of this Article.  
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  

        self._title = title

    @property
    def doi(self):
        """Gets the doi of this Article.  

        DOI  

        :return: The doi of this Article.  
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """Sets the doi of this Article.

        DOI  

        :param doi: The doi of this Article.  
        :type: str
        """
        if doi is None:
            raise ValueError("Invalid value for `doi`, must not be `None`")  

        self._doi = doi

    @property
    def handle(self):
        """Gets the handle of this Article.  

        Handle  

        :return: The handle of this Article.  
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this Article.

        Handle  

        :param handle: The handle of this Article.  
        :type: str
        """
        if handle is None:
            raise ValueError("Invalid value for `handle`, must not be `None`")  

        self._handle = handle

    @property
    def url(self):
        """Gets the url of this Article.  

        Api endpoint for article  

        :return: The url of this Article.  
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Article.

        Api endpoint for article  

        :param url: The url of this Article.  
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  

        self._url = url

    @property
    def url_public_html(self):
        """Gets the url_public_html of this Article.  

        Public site endpoint for article  

        :return: The url_public_html of this Article.  
        :rtype: str
        """
        return self._url_public_html

    @url_public_html.setter
    def url_public_html(self, url_public_html):
        """Sets the url_public_html of this Article.

        Public site endpoint for article  

        :param url_public_html: The url_public_html of this Article.  
        :type: str
        """
        if url_public_html is None:
            raise ValueError("Invalid value for `url_public_html`, must not be `None`")  

        self._url_public_html = url_public_html

    @property
    def url_public_api(self):
        """Gets the url_public_api of this Article.  

        Public Api endpoint for article  

        :return: The url_public_api of this Article.  
        :rtype: str
        """
        return self._url_public_api

    @url_public_api.setter
    def url_public_api(self, url_public_api):
        """Sets the url_public_api of this Article.

        Public Api endpoint for article  

        :param url_public_api: The url_public_api of this Article.  
        :type: str
        """
        if url_public_api is None:
            raise ValueError("Invalid value for `url_public_api`, must not be `None`")  

        self._url_public_api = url_public_api

    @property
    def url_private_html(self):
        """Gets the url_private_html of this Article.  

        Private site endpoint for article  

        :return: The url_private_html of this Article.  
        :rtype: str
        """
        return self._url_private_html

    @url_private_html.setter
    def url_private_html(self, url_private_html):
        """Sets the url_private_html of this Article.

        Private site endpoint for article  

        :param url_private_html: The url_private_html of this Article.  
        :type: str
        """
        if url_private_html is None:
            raise ValueError("Invalid value for `url_private_html`, must not be `None`")  

        self._url_private_html = url_private_html

    @property
    def url_private_api(self):
        """Gets the url_private_api of this Article.  

        Private Api endpoint for article  

        :return: The url_private_api of this Article.  
        :rtype: str
        """
        return self._url_private_api

    @url_private_api.setter
    def url_private_api(self, url_private_api):
        """Sets the url_private_api of this Article.

        Private Api endpoint for article  

        :param url_private_api: The url_private_api of this Article.  
        :type: str
        """
        if url_private_api is None:
            raise ValueError("Invalid value for `url_private_api`, must not be `None`")  

        self._url_private_api = url_private_api

    @property
    def timeline(self):
        """Gets the timeline of this Article.  


        :return: The timeline of this Article.  
        :rtype: str
        """
        return self._timeline

    @timeline.setter
    def timeline(self, timeline):
        """Sets the timeline of this Article.


        :param timeline: The timeline of this Article.  
        :type: str
        """
        if timeline is None:
            raise ValueError("Invalid value for `timeline`, must not be `None`")  

        self._timeline = timeline

    @property
    def thumb(self):
        """Gets the thumb of this Article.  

        Thumbnail image  

        :return: The thumb of this Article.  
        :rtype: str
        """
        return self._thumb

    @thumb.setter
    def thumb(self, thumb):
        """Sets the thumb of this Article.

        Thumbnail image  

        :param thumb: The thumb of this Article.  
        :type: str
        """
        if thumb is None:
            raise ValueError("Invalid value for `thumb`, must not be `None`")  

        self._thumb = thumb

    @property
    def defined_type(self):
        """Gets the defined_type of this Article.  

        Type of article identifier  

        :return: The defined_type of this Article.  
        :rtype: int
        """
        return self._defined_type

    @defined_type.setter
    def defined_type(self, defined_type):
        """Sets the defined_type of this Article.

        Type of article identifier  

        :param defined_type: The defined_type of this Article.  
        :type: int
        """
        if defined_type is None:
            raise ValueError("Invalid value for `defined_type`, must not be `None`")  

        self._defined_type = defined_type

    @property
    def defined_type_name(self):
        """Gets the defined_type_name of this Article.  

        Name of the article type identifier  

        :return: The defined_type_name of this Article.  
        :rtype: str
        """
        return self._defined_type_name

    @defined_type_name.setter
    def defined_type_name(self, defined_type_name):
        """Sets the defined_type_name of this Article.

        Name of the article type identifier  

        :param defined_type_name: The defined_type_name of this Article.  
        :type: str
        """
        if defined_type_name is None:
            raise ValueError("Invalid value for `defined_type_name`, must not be `None`")  

        self._defined_type_name = defined_type_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Article, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Article):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
