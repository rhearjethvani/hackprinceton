from flask import Blueprint, jsonify, request
from models.user import User
import db
import os
import os
from flask import request, jsonify
from werkzeug.utils import secure_filename


qns_route = Blueprint("questions", __name__)




@qns_route.route("/submit-video", methods=["POST"])
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
        return jsonify({"message": "Video successfully uploaded"})
    except Exception as e:
        return jsonify({"error": str(e)})


@qns_route.route("/createqns", methods=["POST"])
def create_qns():
    # if the person is admin then only he will be able to create questions
    # fetch the content from the frontend and send to the backend
    # professor adds the content and based on that it will generate the question
    # user to transfer qns to all the associated users for the specific company or the team
    pass
