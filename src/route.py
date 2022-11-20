import os
from dotenv import load_dotenv, find_dotenv
from quart import Quart, jsonify
load_dotenv(find_dotenv())

app = Quart(__name__)
app.config["SECRET_KEY"] = str(os.environ.get("secret_key"))


@app.get("/")
def index():
    pass


@app.route("/api/predict", methods=["GET"])
def project():
    return jsonify({"prediction": "Hello World!"})

