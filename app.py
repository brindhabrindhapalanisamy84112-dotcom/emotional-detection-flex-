"""
EmotionSense AI — Flask Backend (v3)
Serves static HTML files only.
All AI inference runs in the browser via TF.js + face-api.js.
No model files required on the server.
"""
import os
from flask import Flask, send_from_directory

APP_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=APP_DIR, static_url_path="")

@app.get("/")
def index():
    return send_from_directory(APP_DIR, "index.html")

@app.get("/detect")
@app.get("/detect.html")
def detect():
    return send_from_directory(APP_DIR, "detect.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
