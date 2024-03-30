from flask import Blueprint, jsonify,request
from models.user import User
import db
# from app import requires_admin,requires_auth
from auth.auth import requires_admin,requires_auth

user_bp = Blueprint("user", __name__)


@user_bp.route("/users")
def get_users():
    # if you are an admin you can see other users
    pass


# if the user is not in the database
@user_bp.route("/create", methods=["POST"])
@requires_auth
def create_user():
    user_data = request.json
    username = user_data.get("username")
    email = user_data.get("email")
    password = user_data.get("password")
    is_admin = True if user_data.get("is_admin")=="true" else False

    # Create a User object
    user_obj = User(username, email, password, is_admin)

    # Insert the user object into MongoDB
    result = db.users_collection.insert_one(
        {
            "username": user_obj.username,
            "email": user_obj.email,
            "password": user_obj.password,
            "is_admin": user_obj.is_admin,
        }
    )
    print(result)

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
