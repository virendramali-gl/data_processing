import logging
import pandas as pd
from logger import create_logger
from utils import handle_exceptions

# Instantiate the custom logger
logger, filename = create_logger(__name__)


@handle_exceptions
def process_data(file_path, column_list, drop_na_column):
    """
    Reads and processes a CSV file, checking for missing column data,
    cleaning the data and converting to numeric datatype.

    This function performs the following tasks:
    1. Loads the CSV file from the given file path.
    2. Checks if all specified columns in `column_list` are present in the file. If any are missing, raises a KeyError.
    3. Drops rows from the dataset where the specified `drop_na_column` has missing values.
    4. Converts the `drop_na_column` to a numeric type, raising an error if the column contains invalid values that cannot be converted.

    The function is wrapped with the `handle_exceptions` decorator, so exceptions raised during the execution will be logged and handled appropriately.

    Parameters:
    - file_path (str): Path of the CSV file to be processed
    - column_list (list of str): List of column names that need to be checked for existence in the CSV file
    - drop_na_column (str): Name of the column to be checked for missing values and converted to a numeric type

    Returns:
    - pd.DataFrame: Processed DataFrame, with missing rows dropped and the specified column converted to numeric

    Raises:
    - KeyError: If any of the specified columns in `column_list` are missing from the CSV file, or if the `drop_na_column` does not exist.
    - ValueError: If the `drop_na_column` contains non-numeric values that cannot be converted to numeric.
    """

    df = pd.read_csv(file_path)
    logger.info(f"File loaded successfully from {file_path}.")

    missing_columns = [col for col in column_list if col not in df.columns]
    if missing_columns:
        raise KeyError(f"Missing columns: {missing_columns}")

    if drop_na_column in df.columns:
        df.dropna(subset=[drop_na_column], inplace=True)
        logger.info(f"Dropped rows with missing values in column '{drop_na_column}'")
        df[drop_na_column] = pd.to_numeric(df[drop_na_column], errors="raise")
        logger.info(f"Column '{drop_na_column}' converted to numeric")

    else:
        raise KeyError(f"Column '{drop_na_column}' does not exist in the data")

    return df


def main():
    """
    This is main entry point of the program designed to catch and
    log any unexpected errors during the execution of the program.

    The function does the following:
    1. Prompts the user to input the file path of the CSV file.
    2. Prompts the user to input a list of column names that need to be checked for existence in the CSV file.
    3. Prompts the user to input the name of the column where rows with missing values will be dropped, and the column will be converted to numeric.
    4. Calls the `process_data` function to process the CSV file using the provided inputs.
    5. Logs the results of the data processing, including success or failure.

    Returns:
    - None
    """

    try:
        file_path = input("Enter the path of CSV file: ")

        columns_input = input("Enter the column names separated by commas: ").strip()
        columns_list = [col.strip() for col in columns_input.split(",")]

        drop_na_column = input(
            "Enter the column name to drop rows with missing values & convert to numeric datatype: "
        ).strip()

        logger.info("Starting data processing....")
        df = process_data(file_path, columns_list, drop_na_column)

        if df is not None:
            logger.info("Data processing completed successfully")
        else:
            logger.warning("Data processing failed")

    except Exception as e:
        logger.error(f"Error in main function: {e}")
    finally:
        logger.info("Main function execution completed")

        with open(filename, "a") as log_file:
            log_file.write("\n")


if __name__ == "__main__":
    main()
