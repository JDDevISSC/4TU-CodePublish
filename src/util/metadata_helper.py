import json
import logging
import os
import questionary
from urllib.parse import urlparse

from api import dataset_api

class MetadataHelper():
    def __init__(self, dataset_api=dataset_api):
        self._dataset_api = dataset_api
        self._logger = logging.getLogger(__name__)

    @property
    def dataset_api(self):
        """Gets the DatasetAPI of this MetadataHelper.  

        DatasetAPI for MetadataHelper  

        :return: The DatasetAPI of this MetadataHelper.  
        :rtype: DatasetAPI
        """
        return self._dataset_api

    @dataset_api.setter
    def dataset_api(self, dataset_api):
        """Sets the DatasetAPI of this MetadataHelper.

        DatasetAPI for MetadataHelper  

        :param DatasetAPI: The DatasetAPI of this MetadataHelper.  
        :type: DatasetAPI
        """
        if dataset_api is None:
            raise ValueError("dataset_api value for `dataset_api`, must not be `None`")  

        self._dataset_api = dataset_api

    @property
    def logger(self):
        """Gets the logger of this MetadataHelper.  

        Logger for MetadataHelper  

        :return: The logger of this MetadataHelper.  
        :rtype: Logger
        """
        return self._logger

    @logger.setter
    def logger(self, logger):
        """Sets the logger of this MetadataHelper.

        Logger for MetadataHelper  

        :param logger: The logger of this MetadataHelper.  
        :type: Logger
        """
        if logger is None:
            raise ValueError("logger value for `logger`, must not be `None`")  

        self._logger = logger

    def prepare_dataset_metadata(self, metadata_path):
        """Prepares metadata for use with the DatasetAPI by reading JSON from a file
        
        """
        self.logger.info(f"Preparing dataset metadata with metadata path: {metadata_path}")
        metadata = self._load_metadata_from_file(metadata_path)
        if metadata != None or metadata == "":
            self.logger.debug("Loaded metadata:")
            self.logger.debug(metadata)
            return metadata
        else:
            raise Exception("Metadata cannot be None or empty.")
        
    def retrieve_dataset_id_from_response(self, response):
        """Retrieve dataset_id from from response
        
        """
        self.logger.debug("Retrieving dataset_id from response:")
        self.logger.debug(response)
        parsed_url = urlparse(response['location'])
        uuid = parsed_url.path.split('/')[-1]
        self.logger.debug(f"Found uuid ({uuid})")
        return uuid

    def _load_metadata_from_file(self, path):
        self.logger.debug(f"Loading metadatafile at ({path})")
        with open(path, "r") as file:
            metadata = file.read()
            file.close
        return metadata

    def _create_metadatafile(self, path, metadata):
        self.logger.debug(f"Creating metadatafile at ({path})")
        self.logger.debug(json.dump(metadata))
        with open(path, "w") as file:
            json.dump(metadata, path)
            
    def start_interactive_metadata_funnel(self):
        self.logger.info(f"Starting interactive metadata funnel with output path ({self.config.output})")
        title = self._prompt_for_title()
        authors = self._prompt_for_authors()
        description = self._prompt_for_description()
        license = self._prompt_for_license()
        print(json.dumps(authors) + 
              json.dumps(title) + 
              json.dumps(description) +
              json.dumps(license))
        # print(self.config.output)
        # metadata = self._prompt_user_for_input()
        # metadata = None
        # self._create_metadatafile(output_path, metadata)

    def _prompt_for_title(self):
        title = questionary.text(message=f"""Enter a title.{os.linesep}
Give your research a title that is more descriptive 
than just a file name. This will help making your items discoverable 
via search engines such as Google. The title should have at least 
three characters.{os.linesep}""").ask()
        return {"title": title}
        
    def _prompt_for_authors(self):
        questionary.print(
            "The following questions will populate the author(s) in our metadata.")
        done_prompting = False
        authors = []
        while not done_prompting:
            search_query = questionary.text("Search for author:").ask()
            results = self.dataset_api.search_authors(search_query)
            choices = self._create_choices_from_data(data=results, title_key="full_name", value_key="uuid")
            if len(choices) > 0:
                author = questionary.select("Select author:", choices=choices).ask()
                if author not in authors:
                    authors.append(author)
            else:
                questionary.print("No results found.")
            # Keep asking until all authors are added. We need at least one author.
            if len(authors) > 0:
                done_prompting = not questionary.confirm("Do you want to keep adding authors?",).ask()
        # Return author dict
        return [{"uuid": author} for author in authors]

    def _prompt_for_description(self):
        description = questionary.text(message=f"""Enter a description.{os.linesep}
Add as much context as possible so that 
others can interpret your research and reproduce it. 
Make sure you include methodology, techniques used, 
and if relevant information about approval for data 
collection to confirm adherence to legal or ethical 
requirements. The description should have at least 
four characters.{os.linesep}""", multiline=True).ask()
        return {"description": f"<p>{description}</p>"}

    def _prompt_for_license(self):
        # TODO: Add support for embargoed access and Restricted access
        questionary.print(text="WARNING: Only open access licenses are supported for now.")
        results = self.dataset_api.get_licenses()
        choices = self._create_choices_from_data(data=results, title_key="name", value_key="value")
        # Throw an exception when there are no licenses to choose from.
        if len(choices) > 0:
            license_id = questionary.select("Select license:", choices=choices).ask()
            # Pick license from result
            for result in results:
                if result.get("value") == license_id:
                    license = result
            # Render metadata from license
            return {"license": {"value": license.get("value"), 
                                "name": license.get("name"),
                                "url": license.get("url")}}
        else:
            raise Exception("Couldn't fetch licenses from server.")

    def _prompt_for_language(self):
        languages = {
        "af": "Afrikaans",
        "ar": "Arabic",
        "ast": "Asturian, Asturleonese, Bable, Leonese",
        "az": "Azerbaijani",
        "bg": "Bulgarian",
        "be": "Belarusian",
        "bn": "Bengali, Bangla",
        "br": "Breton",
        "bs": "Bosnian",
        "ca": "Catalan, Valencian",
        "cs": "Czech",
        "cy": "Welsh",
        "da": "Danish",
        "de": "German",
        "dsb": "Lower Sorbian",
        "el": "Modern Greek (1453-)",
        "en": "English",
        "en-au": "English, Australian",
        "en-gb": "English, British",
        "en-us": "English, American",
        "eo": "Esperanto",
        "es": "Spanish, Castilian",
        "es-ar": "Spanish, Argentina",
        "es-co": "Spanish, Colombia",
        "es-mx": "Spanish, Mexico",
        "es-ni": "Spanish, Nicaragua",
        "es-ve": "Spanish, Venezuela",
        "et": "Estonian",
        "eu": "Basque",
        "fa": "Farsi",
        "fi": "Finnish",
        "fr": "French",
        "fy": "Western Frisian",
        "ga": "Irish",
        "gd": "Scottish Gaelic, Gaelic",
        "gl": "Galician",
        "he": "Hebrew",
        "hi": "Hindi",
        "hr": "Croatian",
        "hsb": "Upper Sorbian",
        "hu": "Hungarian",
        "ia": "Interlingua",
        "id": "Indonesian",
        "io": "Ido",
        "is": "Icelandic",
        "it": "Italian",
        "ja": "Japanese",
        "ka": "Georgian",
        "kk": "Kazakh",
        "km": "Khmer, Central Khmer",
        "kn": "Kannada",
        "ko": "Korean",
        "lb": "Luxembourgish, Letzeburgesch",
        "lt": "Lithuanian",
        "lv": "Latvian",
        "mk": "Macedonian",
        "ml": "Malayalam",
        "mn": "Mongolian",
        "mr": "Marathi",
        "my": "Burmese",
        "nb": "Norwegian Bokmål",
        "ne": "Nepali",
        "nl": "Dutch, Flemish",
        "nn": "Norwegian Nynorsk",
        "os": "Ossetian, Ossetic",
        "pa": "Panjabi, Punjabi",
        "pl": "Polish",
        "pt": "Portuguese",
        "pt-br": "Portuguese, Brazil",
        "ro": "Romanian",
        "ru": "Russian",
        "sk": "Slovak",
        "sl": "Slovenian",
        "sq": "Albanian",
        "sr": "Serbian",
        "sr-latn": "Serbian, Latin",
        "sv": "Swedish",
        "sw": "Swahili",
        "ta": "Tamil",
        "te": "Telugu",
        "th": "Thai",
        "tr": "Turkish",
        "tt": "Tatar",
        "udm": "Udmurt",
        "uk": "Ukrainian",
        "ur": "Urdu",
        "vi": "Vietnamese",
        "zh-hans": "Chinese, Simplified",
        "zh-hant": "Chinese, Traditional"
        }
        
        answer = self._prompt_for_selection(languages)
        for key in answer:
            return key
        raise Exception("No key in answer.")
        
    def _create_choices_from_data(self, data, title_key, value_key):
        choices = []
        # Create choices from result
        for d in data:
            choices.append(
                questionary.Choice(
                    title=d.get(title_key), 
                    value=d.get(value_key))
                )
        return choices        
        
    def _prompt_user_for_input(self):
        metadata = {}
        return metadata
        

    def _prompt_for_multiple_selection(self, options):
        selected_options = questionary.checkbox(
            "Please select options (use space to select, enter to confirm):",
            choices=options
        ).ask()
        return selected_options

    def _prompt_for_selection(self, options):
        selected_option = questionary.select(
            "Please select an option (use space to select, enter to confirm):",
            choices=options
        ).ask()