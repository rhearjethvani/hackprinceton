# TODO in the session store the infos so that we can access it


from pymongo import MongoClient


from flask import Flask, redirect, url_for, session, request
from authlib.integrations.flask_client import OAuth

import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for
from functools import wraps
import json
from six.moves.urllib.request import urlopen
from functools import wraps
from flask_cors import cross_origin


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


client = MongoClient("mongodb://localhost:27017/")  # your connection string
db = client["mydatabase"]
users_collection = db["users"]


app = Flask(__name__)

app.secret_key = env.get("APP_SECRET_KEY")

print(app.secret_key)
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)

from functools import wraps
from flask import redirect, url_for, session


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
        if "user" not in session:
            return redirect(url_for("login"))
        user_info = session.get("role")
        print(user_info)
        if user_info and user_info == "admin":
            return f(*args, **kwargs)
        else:
            return "Access denied. Admin privileges required."

    return decorated


@app.route("/dashboard")
@requires_auth
@requires_admin
def dashboard():
    user_info = session.get("user")
    if user_info:
        user_name = user_info.get("name")
        return f"Welcome to the dashboard, {user_name}!"
    else:
        return "Welcome to the dashboard!"


@app.route("/")
def home():
    return render_template(
        "home.html",
        session=session.get("user"),
        pretty=json.dumps(session.get("user"), indent=4),
    )


@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    session["role"]="admin"
    return redirect("/")


@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )


if __name__ == "__main__":
    app.run(host="localhost", port=env.get("PORT", 3000))
