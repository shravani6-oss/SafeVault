from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db, init_db

app = Flask(__name__)
app.secret_key = "safevault-secret-key"


@app.route("/")
def home():
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]

        # Input validation
        if len(name) < 2:
            return "Name must contain at least 2 characters."

        if "@" not in email:
            return "Please enter a valid email."

        if len(password) < 6:
            return "Password must contain at least 6 characters."

        connection = get_db()

        try:
            connection.execute(
                "INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
                (name, email, generate_password_hash(password), "user")
            )

            connection.commit()

        except Exception:
            connection.close()
            return "Email already registered."

        connection.close()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip()
        password = request.form["password"]

        connection = get_db()

        # Parameterized query prevents SQL injection
        user = connection.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        connection.close()

        if user and check_password_hash(user["password"], password):

            session["user_id"] = user["id"]
            session["name"] = user["name"]
            session["role"] = user["role"]

            return redirect("/dashboard")

        return "Invalid email or password."

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        name=session["name"],
        role=session["role"]
    )


@app.route("/admin")
def admin():

    if "user_id" not in session:
        return redirect("/login")

    # Role-Based Access Control
    if session["role"] != "admin":
        return "403 Forbidden - Admin access required."

    return render_template("admin.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)