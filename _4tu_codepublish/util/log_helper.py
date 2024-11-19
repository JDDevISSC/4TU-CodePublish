import logging

def setup_logging(log_level=logging.INFO, log_file="4TU-CODEPUBLISH.log"):
    """Set's up logging by setting a loglevel and a path to the desired logfile.
    
    """
    # Console output
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(log_level)
    # File output
    fileHandler = logging.FileHandler(log_file)
    fileHandler.setLevel(log_level)
    
    # Basic configuration with level and format
    logging.basicConfig(
        level=log_level,  # Set a global logging level
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            streamHandler,
            fileHandler
        ]
    )