#!/usr/bin/env python3
"""
Filtered Logger
"""

import logging
import re
import mysql.connector
import os
import bcrypt

# Task 0: Regex-ing
def filter_datum(fields, redaction, message, separator):
    """ Returns the log message obfuscated """
    regex = "|".join(fields)
    return re.sub(f'({regex})=[^;]+', f'\\1={redaction}', message)

# Task 1: Log formatter
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format the log record """
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)

# Task 2: Create logger
PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def get_logger() -> logging.Logger:
    """ Return a logging.Logger object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger

# Task 3: Connect to secure database
def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Return a connector to the database """
    config = {
        'user': os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        'password': os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        'host': os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        'database': os.getenv('PERSONAL_DATA_DB_NAME'),
        'raise_on_warnings': True
    }
    return mysql.connector.connect(**config)

# Task 4: Read and filter data
def main():
    """ Main function """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()

    for row in cursor:
        log_data = "; ".join([f"{cursor.description[i][0]}={row[i]}" for i in range(len(row))])
        logger.info(log_data)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
