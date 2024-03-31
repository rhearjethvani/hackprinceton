from flask import Blueprint, jsonify, request, session,render_template
from models.user import User
import db
import os
from flask import request, jsonify
from werkzeug.utils import secure_filename
from auth.auth import requires_auth, requires_admin
import sys

from models.test import Test

import sys, os

sys.path.append(os.path.abspath("../"))
from AI.zerogpt import find_ai_human
from AI.gpt import generate_education_questions, generate_job_questions
from AI.speech_to_text import speech_to_text

qns_route = Blueprint("questions", __name__)


# INPUT
# {file: path of the file}


@qns_route.route("/submit-video", methods=["POST"])
# @requires_auth
def submit_video():
    # Check if the request contains files
    if "file" not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files["file"]

    # Check if the file name is empty
    if file.filename == "":
        return jsonify({"error": "No selected file"})

    # Save the file to the movie directory
    try:
        filename = secure_filename(file.filename)
        file_path = os.path.join(
            qns_route.root_path, "../videos", filename
        )  # Assuming 'movie' is the directory name
        file.save(file_path)
        text = speech_to_text(file_path)
        # generate text
        ai_human = find_ai_human(text)
        passed = "human" in ai_human

        # Get user email
        user_email = session.get("user").get("userinfo").get("email")
        user = db.users_collection.find_one({"email": user_email})

        # Update user's latest test result in the database
        db.users_collection.update_one(
            {user},
            {"$set": {user.is_completed: True, user.has_passed: passed}},
        )

        return jsonify({"message": "Video successfully uploaded"})
    except Exception as e:
        return jsonify({"error": str(e)})


# @qns_route.route("/submit-video", methods=["POST"])
# @requires_auth
# def submit_video():
#     # Check if the request contains files
#     if "file" not in request.files:
#         return jsonify({"error": "No file part"})

#     file = request.files["file"]

#     # Check if the file name is empty
#     if file.filename == "":
#         return jsonify({"error": "No selected file"})

#     # Save the file to the movie directory
#     try:
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(
#             qns_route.root_path, "../videos", filename
#         )  # Assuming 'movie' is the directory name
#         file.save(file_path)
#         text=speech_to_text(file_path)
#         # generate text
#         ai_human = find_ai_human(text)
#         passed = "human" in ai_human

#         # Get user email
#         user_email = session.get("user").get("userinfo").get("email")
#         user=db.users_collection.find_one({"email":user_email})

#         # Update user's latest test result in the database
#         db.users_collection.update_one(
#             {user},
#             {"$set": {user.is_completed: True,user.has_passed:passed}},
#         )

#         return jsonify({"message": "Video successfully uploaded"})
#     except Exception as e:
#         return jsonify({"error": str(e)})


# @qns_route.route("/add-question", methods=["POST", "GET"])
# @requires_auth
# @requires_admin
# def create_qns():
#     # Extracting email of the user from the session
#     user_email = session.get("user").get("userinfo").get("email")

#     if request.method == "POST":
#         text = request.form.get("text")
#         if not text:
#             return jsonify({"error": "Invalid request. 'text' field is missing."}), 400

#         # Generating education question from the provided text
#         question = generate_education_questions(str(text))
#         questions = [question]

#         # Creating a dictionary representation of the Test object
#         test_dict = {
#             "is_completed": False,  # Assuming is_completed is set to False by default
#             "questions": questions,
#             "has_passed": False,  # Assuming has_passed is set to False by default
#             "response": [],  # Assuming response is an empty list by default
#         }

#         # Updating user's document in the database
#         result = db.users_collection.find_one({"email": user_email})
#         if result:
#             for person in result.get("people", []):
#                 person_tests = person.get("tests", [])
#                 person_tests.append(test_dict)
#                 person["tests"] = person_tests

#             db.users_collection.update_one(
#                 {"email": user_email}, {"$set": {"people": result["people"]}}
#             )

#         return f"<h1>This is the education question portal. Question: {question}</h1>"
#     else:
#         return render_template("addquestion.html")

    # # hiring manager
    # else:
    #     # number=getfrom the html
    #     number=request.data.number
    #     questions = generate_job_questions(text,int(number))
    #     questions=questions.split("\n")
    #     t = Test(False, questions)
    #     result = db.users_collection.find_one({"email": created_by})
    #     if result:
    #         for item in result.people:
    #             item.tests.append(t)
    #         db.users_collection.update_one(
    #             {"email": created_by}, {"$set": {"people": result.people}}
    #         )

    #     return "<h1>This is education {question} portal<h1>"
    # if the person is admin then only he will be able to create questions
    # fetch the content from the frontend and send to the backend
    # professor adds the content and based on that it will generate the question
    # user to transfer qns to all the associated users for the specific company or the team
