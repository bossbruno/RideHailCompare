from src.route import app


if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True, ssl_context="adhoc")
