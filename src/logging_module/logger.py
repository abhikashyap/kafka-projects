import logging
import os
import inspect

def get_logger(name: str, log_filename: str = None, log_directory: str = 'logs', level=logging.INFO) -> logging.Logger:
    """
    Creates a logger that logs to both the console and a file.

    The log file's path is dynamically generated to mirror the calling module's
    location within the log_directory. This can be overridden by providing
    a custom log_filename.

    Args:
        name: The name for the logger, typically the __name__ of the calling module.
        log_filename: (Optional) A custom name for the log file. If provided,
                      this will be used instead of the auto-generated path.
        log_directory: (Optional) The name of the top-level directory for logs.
                       Defaults to 'logs'.
        level: (Optional) The minimum logging level for the console handler.
               Defaults to logging.INFO.

    Returns:
        A configured logging.Logger instance.
    """
    logger = logging.getLogger(name)
    
    # Avoid adding duplicate handlers if the logger is already configured
    if logger.hasHandlers():
        return logger

    logger.setLevel(level)  # Capture all levels at the logger
    
    project_root = os.getcwd()

    if log_filename:
        # Use the custom filename if provided
        log_file_name = log_filename
    else:
        # Fallback to the automatic path generation
        try:
            caller_frame = inspect.stack()[1]
            # Get an absolute path to the caller's file
            caller_path = os.path.abspath(caller_frame.filename)
            
            # Check if the caller's path is within the project root.
            # If not, it's likely an interactive session (e.g., a notebook).
            if caller_path.startswith(project_root):
                # Create a relative path for the log file to mirror the project structure
                relative_path = os.path.relpath(caller_path, project_root)
                log_file_name, _ = os.path.splitext(relative_path)
            else:
                # Fallback for notebooks or other interactive environments
                safe_name = name.replace('.', '_')
                log_file_name = f"notebooks/{safe_name}"

        except Exception:
            # General fallback if path inspection fails for any reason
            safe_name = name.replace('.', '_')
            log_file_name = f"unresolved/{safe_name}"
        
    # Construct the final log file path inside the specified log_directory
    log_file_path = os.path.join(project_root, log_directory, f"{log_file_name}.log")
    
    # Ensure the directory for the log file exists
    log_dir = os.path.dirname(log_file_path)
    os.makedirs(log_dir, exist_ok=True)

    # Create a shared formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Set up the console handler with the specified level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler still captures everything at DEBUG level and above
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
