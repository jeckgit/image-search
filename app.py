from flask import Flask, render_template, send_from_directory, request, jsonify
from image_utils.image_processing import search_similar_img
import os

app = Flask(__name__)


@app.route("/")
def home():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    image_folder = os.path.join(root_dir, "static/images")
    image_files = os.listdir(image_folder)
    return render_template("index.html", image_files=image_files)


@app.route("/images/<path:filename>")
def serve_image(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, "static/images"), filename)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"]
    
    if file:
        test = search_similar_img(file)
        return jsonify(success=True, message=test)
    else:
        return jsonify({"error": "No file uploaded."}), 400


if __name__ == "__main__":
    app.run()
