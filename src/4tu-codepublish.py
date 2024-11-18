import argparse
import logging
from api.dataset_api import DatasetAPI
from util import log_helper
from util import code_publisher
from util.metadata_helper import MetadataHelper
from conf.config import Config
import sys

def main():
    # Check for Python 3 or a more recent version. Fail if condition is not met.
    if sys.version_info[0] < 3:
        raise Exception("Python 3 or a more recent version is required.")
    
    # Handle the configuration
    config = Config()
    # Setup logging
    log_helper.setup_logging(config.log_level, config.log_file)
    logger = logging.getLogger(__name__)
    
    # Start the program by initilizing necesarry class objects
    logger.info("Starting 4TU-CODEPUBLISH")
    dataset_api = DatasetAPI(config)
    metadata_helper = MetadataHelper(dataset_api)

    # Parse arguments
    parser = argparse.ArgumentParser(description="4TU-CODEPUBLISH")
    parser.add_argument("--create", "-c", action="store_true", help="Start the interactive metadata creation process. Output defaults to metadata.json")
    parser.add_argument("--output", "-o", type=str, help="Specify the metadata output file.")
    args = parser.parse_args()
    
    # Set the output file if it was specified and not empty    
    if args.output is not None or args.output is not args.output == "":
        config.output(args.output)
    
    # Start the interactive metadata creation funnel if the create argument is given.
    if args.create:
        metadata_helper.start_interactive_metadata_funnel()
    else:
        #Start pushing code and metadata only if there was no create argument given.
        code_publisher.publish()
        pass

if __name__ == "__main__":
    main()