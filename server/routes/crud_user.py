from flask import Blueprint, jsonify, request, session
from models.user import User
import db

# from app import requires_admin,requires_auth
from auth.auth import requires_admin, requires_auth

user_bp = Blueprint("user", __name__)


@user_bp.route("/users")
@requires_auth
@requires_admin
def get_users():
    user_data = session.get("user").get("userinfo")
    email = user_data.get("email")
    user = db.users_collection.find({email})
    
    return user.people 


# if the user is not in the database
@user_bp.route("/create", methods=["POST"])
@requires_auth
def create_user():
    # you should do here also the session stuff
    user_data = session.get("user").get("userinfo")
    username = user_data.get("name")
    email = user_data.get("email")
    password = user_data.get("email")
    is_admin = True # manual stuff for now
    search_email=db.users_collection.find_one(email)
    if not search_email:

        # Create a User object
        user_obj = User(username, is_admin, email, password)

        # Insert the user object into MongoDB
        result = db.users_collection.insert_one(
            {
                "username": user_obj.username,
                "email": user_obj.email,
                "password": user_obj.password,
                "is_admin": user_obj.is_admin,
            }
        )

        # Check if the insertion was successful
        if result.inserted_id:
            return (
                jsonify(
                    {
                        "message": "User created successfully",
                        "user_id": str(result.inserted_id),
                    }
                ),
                201,
            )
        else:
            return jsonify({"error": "Failed to create user"}), 500
    return jsonify({"message":"User already Exists"})
