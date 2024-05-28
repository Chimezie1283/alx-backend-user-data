# user_authentication_service


# Alx Backend User Data

## Project Overview

This project is a user authentication service implemented in Python using Flask and SQLAlchemy. It provides a User model with secure password storage using bcrypt and follows the specified coding style and requirements.

## Project Structure

- **main.py**: Entry point of the application for testing the User model.
- **user.py**: Contains the SQLAlchemy User model and its attributes.

## Setup

1. Install required dependencies:

    ```bash
    pip3 install bcrypt
    ```

2. Run the application:

    ```bash
    python3 main.py
    ```

## User Model

### Attributes

- **id**: Integer, primary key
- **email**: Non-nullable string
- **hashed_password**: Non-nullable string
- **session_id**: Nullable string
- **reset_token**: Nullable string

### Usage Example

```python
from user import User

# Create a new user instance
user = User(email="user@example.com", hashed_password="hashed_password")

# Accessing user attributes
print(user.id)
print(user.email)
print(user.hashed_password)
print(user.session_id)
print(user.reset_token)


Coding Style
The project follows the PEP 8 coding style, and the code is checked using pycodestyle version 2.5.

Dependencies
Flask
SQLAlchemy 1.3.x
bcrypt
Additional Notes
The Flask app should only interact with Auth and never with DB directly.
Only public methods of Auth and DB should be used outside these classes.
Author
Agbo Chimezie Emmanuel
