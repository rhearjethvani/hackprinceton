from flask import Blueprint, jsonify, request, session, render_template
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
    admin = db.users_collection.find_one({"email": email})

    if not admin:
        return jsonify({"error": "Admin not found"})

    if "people" not in admin:
        return jsonify([])  # Return an empty list if 'people' list doesn't exist

    peeps = admin["people"]

    # Extract required fields from each user in 'peeps' list
    user_list = []
    for user in peeps:
        user_info = {
            "username": user.get("username"),
            "email": user.get("email"),
            # Include other fields as needed
        }
        user_list.append(user_info)

    return jsonify(user_list)


@user_bp.route("/add-user/",methods=["POST","GET"])
@requires_auth
@requires_admin
def add_user():
    if request.method == "POST":
        email = request.form.get("email")
        usertobeAdded = db.users_collection.find_one({"email": email})
        if not usertobeAdded:
            return jsonify({"error": "User with specified email not found"}), 404

        user_data = session.get("user").get("userinfo")
        email_admin = user_data.get("email")

        admin = db.users_collection.find_one({"email": email_admin})
        if not admin:
            return jsonify({"error": "Admin not found"}), 404

        # Ensure admin has a 'people' list
        if 'people' not in admin:
            admin['people'] = []

        # Append usertobeAdded to admin's 'people' list
        admin['people'].append(usertobeAdded)

        # Save the updated admin
        db.users_collection.update_one({"email": email_admin}, {"$set": admin})
        return jsonify({"message": "User added successfully"}), 200
    else:
        return render_template("adduser.html")


# if the user is not in the database
# @user_bp.route("/create", methods=["POST"])
# @requires_auth
def create_user():
    # you should do here also the session stuff
    user_data = session.get("user").get("userinfo")
    username = user_data.get("name")
    email = user_data.get("email")
    password = user_data.get("email")
    is_admin = True # manual stuff for now
    search_email=db.users_collection.find_one({"email":email})
    # print('search email',search_email)
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
                "tests":[],
                "people":[]
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
