import logging
from datetime import datetime


def create_logger(name):
    """
    Creates and configures a logger instance with both console and file handlers.

    This function sets up a logger with two handlers:
    1. StreamHandler: to log messages to the console
    2. FileHandler: to log messages to a file where the filename is dynamically generated based on the current date

    Log format is configured to include the following information in each log entry:
    - Timestamp of the log entry
    - Severity level of the log (e.g., DEBUG, INFO)
    - Actual log message
    - Name of the file from which the log was generated
    - Line number where the log was created

    Args:
    - name (str): Name of the module or script where the logger is being created

    Returns:
    - tuple:
        - logger (logging.Logger): Configured logger instance
        - log_filename (str): Name of the log file
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)

    log_filename = f"log_{datetime.today().strftime('%Y-%m-%d')}.txt"
    fh = logging.FileHandler(log_filename)
    fh.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s - %(filename)s - Line:%(lineno)d"
    )
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)

    return logger, log_filename
