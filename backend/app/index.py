from flask import Flask, request
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(
    app
)
@app.route("/")
def index():
    print()
    return json.dumps({"title": "thanks"})

@app.route("/subscription", methods=["POST"])
def subscribe():
    req = request.json
    print(req)
    print("test")
    return json.dumps({"title": "subscription"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)