from logging_module.logger import get_logger
import test_module.example_code as example_code

# This logger will automatically create and write to 'logs/main.log'
logger = get_logger(__name__)

def run_main_example():
    """Logs messages from the main module and calls another module."""
    logger.info("Main function is starting.")
    # This will trigger logging in the example_code module
    example_code.do_something()
    logger.info("Main function has finished.")

if __name__ == "__main__":
    logger.info("Application starting up.")
    run_main_example()
    logger.info("Application has finished.")
    print("\n✅ Multi-module logging demonstration complete.")
    print("Logs from main.py were sent to 'logs/main.log'")
    print("Logs from example_code.py were sent to 'logs/example_code.log'")
