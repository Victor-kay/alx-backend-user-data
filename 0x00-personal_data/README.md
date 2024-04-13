# Personal Data Filtering and Logging

This project provides a set of Python scripts for handling personal data filtering, logging, password encryption, and database operations.

## Project Structure

The project consists of the following files:

- `filtered_logger.py`: Main script containing functions for data filtering, logging, and database operations.
- `encrypt_password.py`: Script for hashing and validating passwords.
- `README.md`: This file providing an overview of the project.

## Usage

To use the scripts, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone <repository-url>
Tasks
Task 0: Regex-ing
Script: filtered_logger.py
Function: filter_datum
Description: Returns the log message obfuscated using regular expressions.
Task 1: Log formatter
Script: filtered_logger.py
Class: RedactingFormatter
Description: Formats log records and redacts sensitive information.
Task 2: Create logger
Script: filtered_logger.py
Function: get_logger
Description: Creates a logger object for logging user data with redacted fields.
Task 3: Connect to secure database
Script: filtered_logger.py
Function: get_db
Description: Connects to a secure database to retrieve user data.
Task 4: Read and filter data
Script: filtered_logger.py
Function: main
Description: Reads user data from a database, filters it, and logs the filtered data.
Task 5: Encrypting passwords
Script: encrypt_password.py
Functions: hash_password, is_valid
Description: Provides functions for hashing and validating passwords using bcrypt.
Task 6: Check valid password
Script: encrypt_password.py
Function: is_valid
Description: Validates a password against a hashed password.
