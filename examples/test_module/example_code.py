from logging_module.logger import get_logger

# This logger will automatically create and write to 'logs/example_code.log'
logger = get_logger(__name__)

def do_something():
    """A simple function that logs a few messages."""
    logger.info("The 'do_something' function has started.")
    logger.debug("This is a debug message from the example_code module.")
    logger.info("The 'do_something' function is finished.")
