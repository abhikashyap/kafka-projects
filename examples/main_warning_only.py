import logging
from logging_module.logger import get_logger

# Get a logger instance, but set the console logging level to WARNING.
# This means DEBUG and INFO messages will not be printed to the console.
logger = get_logger(__name__, level=logging.WARNING)

def run_warning_example():
    """Logs messages at different levels to demonstrate filtering."""
    logger.debug("This is a debug message. It will NOT appear on the console.")
    logger.info("This is an info message. It will also NOT appear on the console.")
    logger.warning("This is a warning. It WILL be visible on the console.")
    logger.error("This is an error. It is also visible on the console.")
    logger.critical("This is a critical error, which will definitely be shown.")

if __name__ == "__main__":
    print("--- Running Logger with WARNING Level ---")
    run_warning_example()
    print("\n✅ Logging demonstration complete.")
    print("Only messages of level WARNING and above were printed to the console.")
    print("All messages (including DEBUG and INFO) were written to 'logs/examples/main_warning_only.log'")
