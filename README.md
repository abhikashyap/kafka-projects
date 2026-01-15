# Custom Python Logger

A flexible Python logging module that can be easily imported into any project.

## Features

- **Console and File Logging**: Logs messages to both the console and a log file.
- **Automatic File Structure**: Creates log files in a structured directory that mirrors your project's file structure.
- **Customizable Log Files**: You can specify a custom log file name.
- **Customizable Log Directory**: You can specify a custom top-level directory for logs.

## Installation

To install this library from your GitHub repository, use pip:

```bash
pip install git+https://github.com/abhikashyap/mirror-log.git
```

## Usage

```python
from logging_module.logger import get_logger

# Automatic path based on the calling module
logger = get_logger(__name__)
logger.info("This will be logged to logs/your_module.log")

# Custom log file name
custom_logger = get_logger("my_app", log_filename="custom.log")
custom_logger.info("This will be logged to logs/custom.log")
```
