# SafeVault

SafeVault is a simple Flask web application demonstrating secure coding,
authentication, authorization and protection against common web vulnerabilities.

## Features

- User registration
- Secure password hashing
- User login
- Session authentication
- Role-Based Access Control (RBAC)
- Input validation
- Parameterized SQL queries
- SQL injection prevention
- XSS protection
- Security testing

## Technologies

- Python
- Flask
- SQLite
- HTML
- Werkzeug
- Pytest

## Security

The application uses parameterized SQL queries instead of directly joining
user input with SQL statements.

Passwords are stored using secure password hashing.

Authentication is implemented using Flask sessions.

Role-Based Access Control prevents normal users from accessing the admin page.

Flask/Jinja template escaping is used to help prevent XSS attacks.

## Demo Accounts

Admin:

Email: admin@safevault.com

Password: admin123

Normal users can be created through the registration page.

## Testing

Security tests are included in:

tests/test_security.py

Run the tests using:

pytest