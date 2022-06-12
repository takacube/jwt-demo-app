from flask import Flask
import json
from flask_cors import CORS
app = Flask(__name__)
CORS(
    app
)
@app.route("/")
def index():

    return json.dumps({"title": "thanks"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81, debug=True)