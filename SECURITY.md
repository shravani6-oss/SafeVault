# Security Report

## 1. SQL Injection

### Vulnerability

SQL queries can become vulnerable when user input is directly added to
SQL statements.

### Fix

SafeVault uses parameterized SQL queries.

Example:

cursor.execute(
    "SELECT * FROM users WHERE email = ?",
    (email,)
)

This prevents user input from being interpreted as SQL commands.

---

## 2. Cross-Site Scripting (XSS)

### Vulnerability

User-controlled input can potentially contain malicious HTML or JavaScript.

### Fix

Flask/Jinja automatic HTML escaping is used when displaying user data.

---

## 3. Weak Authentication

### Vulnerability

Passwords should never be stored as plain text.

### Fix

SafeVault uses Werkzeug password hashing functions to securely hash passwords.

---

## 4. Authorization

### Vulnerability

A logged-in user should not automatically have access to administrator
resources.

### Fix

Role-Based Access Control was implemented.

Only users with the `admin` role can access `/admin`.

---

## 5. Input Validation

User input is validated during registration.

The application checks:

- Name length
- Email format
- Password length

---

## Copilot Assistance

Microsoft Copilot was used to assist with secure coding, input validation,
parameterized SQL queries, authentication, authorization, security testing,
and debugging.

The generated suggestions were reviewed, modified where necessary, and
tested before being included in the project.