from flask import Flask, request
import json
from flask_cors import CORS
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['holoduledb']
usersCollection = db['users']

app = Flask(__name__)
CORS(
    app
)
@app.route("/")
#this method is just for a test
def index():
    print()
    return json.dumps({"title": "thanks"})

@app.route("/subscription", methods=["POST"])
def subscribe():
    name = request["name"]
    password = request["password"]
    print(name)
    print(password)
    return json.dumps({"name": name, "password": password})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)