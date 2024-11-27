import logging
import pandas as pd
from logger import create_logger

# Instantiate the custom logger
logger, _ = create_logger(__name__)


def handle_exceptions(func):
    """
    A decorator function that wraps another function to handle and log
    exceptions and prevents the program from crashing.

    This decorator is used to catch common exceptions such as:
    - FileNotFoundError: Raised when the specified file not found
    - KeyError: Raised when the particular column is missing from the dataset
    - pd.errors.EmptyDataError: Raised when the file is empty
    - ValueError: Raised when there is an invalid value
    - Exception: Catches any other unexpected errors

    Parameters:
    - func (function): The function to be wrapped by the decorator

    Returns:
    - function: A wrapped function with exception handling and logging added
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as fnf_error:
            logger.error(f"File not found: {fnf_error}")
            raise fnf_error
        except KeyError as key_error:
            logger.error(f"Missing required columns: {key_error}")
            raise key_error
        except pd.errors.EmptyDataError:
            logger.error("File is empty.")
            raise
        except ValueError as value_error:
            logger.error(f"Invalid value: {value_error}")
            raise value_error
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise
        else:
            logger.info("Function executed successfully.")
        finally:
            logger.info("Exception handling completed.")
        return None

    return wrapper
