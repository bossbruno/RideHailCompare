import os
from dotenv import load_dotenv, find_dotenv
from quart import Quart, jsonify, request

load_dotenv(find_dotenv())

app = Quart(__name__)
app.config["SECRET_KEY"] = str(os.environ.get("secret_key"))


@app.get("/")
async def index():
    return jsonify({"message": "Hello World!"})


@app.route("/api/predict", methods=["GET"])
async def project():
    data = await request.get_json()
    print(f"Data: {data.get('name')}")
    return jsonify({"prediction": data})
