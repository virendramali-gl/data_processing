## **Data Processing with Exception Handling**

This Python program is designed to process a CSV file, ensuring that necessary columns exist, cleaning the data by removing rows with missing values, and converting specified columns to numeric types. It includes exception handling using a decorator and detailed logging to track the flow and errors.

## **Features**
- **File Handling**: Loads a CSV file from a specified file path.
- **Column Validation**: Ensures that all required columns are present in the dataset.
- **Data Cleaning**: Removes rows with missing values in a specified column and converts that column to numeric.
- **Logging**: Logs every step of the process, including success and failure messages, to a date-specific log file.
- **Exception Handling**: Catches and logs specific exceptions such as missing file, missing columns, empty file, invalid values, and unexpected errors.

## **File Structure**
- **log_YYYY-MM-DD.txt**: Logs generated for the current date.
- **logger.py**: Contains the logic for configuring and creating a custom logger that writes logs to both the console and a log file.
- **utils.py**: Defines the `handle_exceptions` decorator function to handle and log various exceptions.
- **data_processing.py**: Main logic for processing CSV files, validating columns, cleaning data, and handling exceptions. It also contains the `main()` function that serves as the entry point for the program.

## **Requirements**
- Python 3.x
- Pandas library (`pip install pandas`)

## **How to Use**

1. **Run the script**:
   - Ensure that you have the required CSV file and the necessary columns in it.
   - Execute the script in your terminal or preferred Python environment.

2. **Follow the prompts**:
   - The program will ask for:
     - **CSV File Path**: Specify the location of the CSV file.
     - **Column Names**: Provide a comma-separated list of columns to check in the file.
     - **Column for NA Removal**: Enter the column name that will be checked for missing values (rows with missing values in this column will be dropped).
    
3. **Processing**:
   - The script will attempt to process the CSV file according to the rules, logging every step. If an error occurs it will be logged into a log file.

## **Functions**

### **`handle_exceptions(func)`**
This is a decorator function that wraps the `process_data` function to handle and log various exceptions. It prevents the program from crashing by catching common exceptions:

- **FileNotFoundError**: Raised when the specified file path does not exist.
- **KeyError**: Raised when required columns are missing from the dataset.
- **pd.errors.EmptyDataError**: Raised when the CSV file is empty.
- **ValueError**: Raised when the `drop_na_column` contains invalid values that can't be converted to a numeric type.
- **Exception**: Catches any unexpected errors.

**Parameters**:
- `func`: The function to be wrapped by the decorator.

**Returns**:
- A wrapped function that includes exception handling and logging.

### **`process_data(file_path, column_list, drop_na_column)`**
This function reads a CSV file, validates that specified columns exist, removes rows with missing values in a given column, and converts the column to a numeric type.

**Parameters**:
- `file_path`: Path of the CSV file to process.
- `column_list`: List of column names that must exist in the CSV file.
- `drop_na_column`: Column name to drop rows with missing values and convert to numeric.

**Returns**:
- A Pandas DataFrame containing the cleaned data.

**Exceptions**:
- **KeyError**: If required columns are missing or if the specified column for NA removal does not exist.
- **ValueError**: If the specified column cannot be converted to numeric.

### **`main()`**
The entry point of the program, which prompts the user for necessary input and calls the `process_data` function to process the CSV file.

**Functionality**:
- Prompts the user for the file path, column names, and column to drop NA.
- Calls `process_data` and logs the result.
- Handles unexpected errors and logs them.

**Returns**:
- None

### **`create_logger(name)`**
This function creates and configures a logger with both a console (`StreamHandler`) and a file handler (`FileHandler`). It formats the logs to include the timestamp, log level, message, file name, and line number.

**Parameters**:
- `name`: The name of the logger, typically the module name where the logger is created.

**Returns**:
- A tuple containing:
  - `logger`: The configured `logging.Logger` instance.
  - `log_filename`: The name of the log file where logs will be saved.

## **Logging**
Logs are written to a date-specific log file (e.g., `log_2024-11-26.txt`). The log entries include:
- **Info**: Successful steps such as file loading, column validation, and data cleaning.
- **Warnings**: If processing fails or if there's an issue but not a critical error.
- **Error**: Detailed information about any errors that occurred, including exception types and messages.
