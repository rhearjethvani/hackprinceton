# TODO in the session store the infos so that we can access it

# from AI.speech_to_text import speech_to_text
# from AI.zerogpt import find_ai_human

from pymongo import MongoClient
from flask import Flask, redirect, url_for, request, redirect, render_template, session,jsonify
from authlib.integrations.flask_client import OAuth
from functools import wraps
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from functools import wraps
from six.moves.urllib.request import urlopen
from flask_cors import cross_origin
import db
from routes.crud_user import user_bp
from routes.crud_qns import qns_route
from auth.auth import requires_auth,requires_admin
import os
from flask import Flask, render_template, request, redirect, url_for
from routes.crud_user import create_user,get_users
import sys, os

from server.models.test import Test

sys.path.append(os.path.abspath("../"))
from AI.zerogpt import find_ai_human
from AI.speech_to_text import speech_to_text

# ENV setup
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


app = Flask(__name__)


# AUTH-0 setup
app.secret_key = env.get("APP_SECRET_KEY")
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


app.register_blueprint(user_bp)
app.register_blueprint(qns_route)


# test admin/auth routes
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
    users=[]
    if "role" in session and session["role"] == "admin":
        user = db.users_collection.find_one(
            {"email": session.get("user").get("userinfo").get("email")}
        )
        users=user.get("people",[])

    return render_template(
        "home.html",
        session=session,
        users=users,
        l=len(users),
        pretty=json.dumps(session.get("user"), indent=4),
    )


@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    
    session["user"] = token
    session["role"]="admin"
    print(session)

    create_user()
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


@app.route("/video")
def index():
    return render_template("indexCopy.html")


@app.route("/save_video", methods=["POST"])
@requires_auth
def save_video():
    try:
        video_file = request.files["video"]
        video_file.save("./videos/recorded_video.webm")

        text = speech_to_text("./videos/recorded_video.webm")
        print(text)

        ai_human = find_ai_human(text)
        passed = "human" in ai_human
        print(passed)

        user_email = session.get("user").get("userinfo").get("email")
        user = db.users_collection.find_one({"email": user_email})

        if user is not None and user.get("is_admin", False):
            # Update user's latest test result in the database
            test = Test(is_completed=True, questions=[], has_passed=passed)
            test.response.append(text)
            user.tests.append(test)
            db.users_collection.update_one(
                {"email": user_email}, {"$set": {"tests": user.tests}}
            )
            return (
                jsonify({"message": "Video and test result saved successfully."}),
                200,
            )
        else:
            return jsonify({"error": "User is not an admin or does not exist."}), 403
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="localhost", port=env.get("PORT", 3000))
