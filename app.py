from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

SIGNAL_FILE = "signals.json"

def load_signals():
    if not os.path.exists(SIGNAL_FILE):
        return {"status": "waiting"}
    
    with open(SIGNAL_FILE, "r") as f:
        return json.load(f)

@app.route("/")
def home():
    return jsonify({
        "server": "ABHI SIGNAL ENGINE",
        "status": "running"
    })

@app.route("/signal")
def signal():
    return jsonify(load_signals())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
