from flask import session, redirect, url_for
from functools import wraps


# Decorator to check if user is authenticated
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)

    return decorated


# Decorator to check if user is an admin
def requires_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "role" not in session or session["role"] != "admin":
            return "Access denied. Admin privileges required."
        return f(*args, **kwargs)

    return decorated
