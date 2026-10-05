import sqlite3
from werkzeug.security import generate_password_hash

DATABASE = "safevault.db"


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'user'
        )
    """)

    # Create a demo admin account
    admin_password = generate_password_hash("admin123")

    try:
        connection.execute(
            "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
            ("Admin", "admin@safevault.com", admin_password, "admin")
        )
    except sqlite3.IntegrityError:
        pass

    connection.commit()
    connection.close()