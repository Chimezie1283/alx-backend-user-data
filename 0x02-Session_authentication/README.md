# Session Authentication in Flask

## Overview

This project focuses on implementing Session Authentication in a Flask web application. Session Authentication is a common mechanism used to manage user sessions and enhance security in web applications. Unlike the typical practice of using existing frameworks or modules for authentication, this project explores the process of building a Session Authentication system from scratch to gain a deeper understanding of its mechanisms.

## Project Structure

The project is organized into several tasks, each building upon the previous one. Here's a brief overview of the tasks:

Et moi et moi et moi!

Copy and adapt the work from the previous Basic Authentication project.
Add a new endpoint to retrieve the authenticated user object.
Empty session

Create a SessionAuth class that initially contains no methods.
Update the main application to use SessionAuth if the environment variable AUTH_TYPE is set to session_auth.
Create a session

Implement methods in SessionAuth to create and manage user sessions.
Generate and store session IDs for user authentication.
User ID for Session ID

Extend SessionAuth to retrieve User IDs based on Session IDs.
Implement methods to link and retrieve user information using session IDs.
Session cookie

Add a method to the authentication system to extract session IDs from cookies.
Use environment variables to define the cookie name for session IDs.
Before request

Update the application to handle authentication requirements before processing requests.
Exclude certain routes from authentication checks.
Use Session ID for identifying a User

Implement a method to retrieve the current user based on session ID.
Demonstrate the usage of this method in a Flask application.
New view for Session Authentication

Create a new Flask view to handle routes specific to Session Authentication.
Implement a login route to authenticate users and create sessions.

## Getting Started

Prerequisites
```
Python 3.x
```

```
Flask (pip install flask)
```
## Installation

Clone the repository: ```git clone https://github.com/yourusername/session-auth-flask.git```
Navigate to the project directory: cd session-auth-flask
Install dependencies: ```pip install -r requirements.txt```
## Usage

Set the environment variable AUTH_TYPE to session_auth.
Run the Flask application: ```python app.py```
Access the application at ```http://127.0.0.1:5000/```
# Configuration

The application can be configured by modifying the environment variables in the .env file.
Contributing
Feel free to contribute by opening issues or submitting pull requests. Please follow the code of conduct.

# License

This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments

Special thanks to the Flask community for their excellent documentation and resources.
# Resources

Flask Documentation:
``` https://flask.palletsprojects.com/```
Python Documentation:
``` https://docs.python.org/```


# Contact

For any inquiries or feedback, please contact agbo.chimezie1283@gmail.com.
