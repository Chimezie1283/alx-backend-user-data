#!/usr/bin/env python3
""" 0x05. Personal data
How to implement a log filter that will obfuscate PII fields
How to encrypt a password and check the validity
How to authenticate to a database using environment variables
"""
import os
import re
import mysql.connector
from typing import List
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ a function called filter_datum that returns the log message
        Args:
            fields: a list of strings representing all field
            redaction: a string representing by what the field
            message: a string representing the log line
            separator: a string representing by which character is
            separating all fields in the log line (message)
        Returns: message
    """
    for format in fields:
        message = re.sub(rf"{format}=(.*?)\{separator}",
                         f'{format}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Init """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Format """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ a get_logger function that takes no arguments and
    returns a logging.Logger object
    """

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ connect to a secure holberton database to read a users table.
    """
    DB_user = os.environ.get('PERSONAL_DATA_DB_USERNAME', "root")
    DB_password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    DB_host_name = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    DB_name = os.environ.get('PERSONAL_DATA_DB_NAME')
    connection = mysql.connector.connect(
        host=DB_host_name,
        database=DB_name,
        user=DB_user,
        password=DB_password)
    return connection


def main():
    """ a main function that takes no arguments and returns
    """
    fields = "name,email,phone,ssn,password,ip,last_login,user_agent"
    columns = fields.split(',')
    query = "SELECT {} FROM users;".format(fields)
    info_logger = get_logger()
    connection = get_db()
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            record = map(
                lambda x: '{}={}'.format(x[0], x[1]),
                zip(columns, row),
            )
            msg = '{};'.format('; '.join(list(record)))
            args = ("user_data", logging.INFO, None, None, msg, None, None)
            log_record = logging.LogRecord(*args)
            info_logger.handle(log_record)


if __name__ == "__main__":
    main()
