import pandas as pd
import pytest
from unittest.mock import mock_open, patch
from data_processing import process_data

# Sample CSV data for different test cases
mock_csv_data = """
name,age,city
John,25,New York
Alice,30,Los Angeles
Bob,22,Boston
"""

# Sample data for empty CSV file
mock_empty_csv_data = ""

# Sample CSV data with an invalid value
mock_csv_invalid_value = """
name,age,city
John,25,New York
Alice,thirty,Los Angeles
Bob,22,Boston
"""


# Test case to simulate KeyError (missing column)
def test_missing_column_keyerror():
    """
    Tests the process_data function when a required column is missing in the CSV file, expecting a KeyError to be raised.
    """

    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        required_columns = ["name", "age", "salary"]
        drop_na_column = "age"

        with pytest.raises(KeyError):
            process_data("fake_path.csv", required_columns, drop_na_column)


# Test case to simulate ValueError (invalid value in column for numeric conversion)
def test_value_error_in_column_conversion():
    """
    Tests the process_data function when a column contains an invalid value (non-numeric), expecting a ValueError during conversion.
    """

    with patch("builtins.open", mock_open(read_data=mock_csv_invalid_value)):
        required_columns = ["name", "age", "city"]
        drop_na_column = "age"

        with pytest.raises(ValueError):
            process_data("fake_path.csv", required_columns, drop_na_column)


# Test case to simulate FileNotFoundError (file does not exist)
def test_file_not_found_error():
    """
    Tests the process_data function when the file does not exist, expecting a FileNotFoundError to be raised.
    """

    with patch("builtins.open", side_effect=FileNotFoundError):
        required_columns = ["name", "age", "city"]
        drop_na_column = "age"

        with pytest.raises(FileNotFoundError):
            process_data("fake_non_existent_path.csv", required_columns, drop_na_column)


# Test case to simulate EmptyDataError (empty CSV file)
def test_empty_data_error():
    """
    Tests the process_data function when the CSV file is empty, expecting a pd.errors.EmptyDataError to be raised.
    """

    with patch("builtins.open", mock_open(read_data=mock_empty_csv_data)):
        required_columns = ["name", "age", "city"]
        drop_na_column = "age"

        with pytest.raises(pd.errors.EmptyDataError):
            process_data("fake_empty_path.csv", required_columns, drop_na_column)
