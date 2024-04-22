# 0x03. User Authentication Service

## Project Description
This project aims to build a user authentication service with a focus on backend development. The service will handle user registration, login, password hashing, session management, and profile retrieval using Flask, SQLAlchemy, and bcrypt.

## Project Details

### Authentification

- **Weight:** 1
- **Project Timeline:** Apr 22, 2024, 6:00 AM - Apr 26, 2024, 6:00 AM
- **Checker Release:** Apr 23, 2024, 6:00 AM
- **Auto Review:** Launched at the deadline

### Resources
- Flask documentation
- Requests module
- HTTP status codes

### Learning Objectives
- Declare API routes in Flask
- Get and set cookies
- Retrieve request form data
- Return various HTTP status codes

## Requirements

### Allowed Editors
- vi
- vim
- emacs

### Environment
- Ubuntu 18.04 LTS
- Python 3.7

### Coding Standards
- pycodestyle (version 2.5)
- SQLAlchemy 1.3.x
- Type annotations for all functions
- Documentation for all modules, classes, and functions

## Tasks

### 0. User model
Create a SQLAlchemy model for the User table with attributes: id, email, hashed_password, session_id, reset_token.

### 1. Create user
Implement the `add_user` method in the DB class to add a new user to the database.

### 2. Find user
Implement the `find_user_by` method in the DB class to find a user by keyword arguments.

### 3. Update user
Implement the `update_user` method in the DB class to update a user's attributes.

### 4. Hash password
Implement the `_hash_password` method to hash a password using bcrypt.

### 5. Register user
Implement the `register_user` method in the Auth class to register a new user.

### 6. Basic Flask app
Create a basic Flask app with a single GET route ("/") returning a JSON payload.

### 7. Register user
Implement the POST /users route to register a user.

### 8. Credentials validation
Implement the `valid_login` method in the Auth class to validate user credentials.

### 9. Generate UUIDs
Implement the `_generate_uuid` function in the auth module to generate a UUID.

### 10. Get session ID
Implement the `create_session` method in the Auth class to create a session ID.

### 11. Log in
Implement the POST /sessions route to log in a user.

### 12. Find user by session ID
Implement the `get_user_from_session_id` method in the Auth class to find a user by session ID.

### 13. Destroy session
Implement the `destroy_session` method in the Auth class to destroy a session.

### 14. Log out
Implement the DELETE /sessions route to log out a user.

### 15. User profile
Implement the GET /profile route to retrieve a user's profile.

### 16. Generate reset password token
Implement the `get_reset_password_token` method in the Auth class to generate a reset password token.

### 17. Get reset password token
Implement the POST /reset_password route to get a reset password token.

### 18. Update password
Implement the `update_password` method in the Auth class to update a user's password.

### 19. Update password end-point
Implement the PUT /reset_password route to update a user's password.

### 20. End-to-end integration test
Create a main.py module to perform end-to-end integration tests for all the implemented features.

## Repository Information
- **GitHub Repository:** alx-backend-user-data
- **Directory:** 0x03-user_authentication_service
