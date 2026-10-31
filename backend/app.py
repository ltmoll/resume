"""Small Flask API that serves the resume as JSON."""

import os

from flask import Flask, jsonify
from flask_cors import CORS

from backend.profile import PROFILE

app = Flask(__name__)

# In production, set FRONTEND_ORIGINS to the URL(s) hosting the React app.
allowed_origins = os.getenv("FRONTEND_ORIGINS", "http://localhost:5173").split(",")
CORS(app, resources={r"/api/*": {"origins": allowed_origins}})


@app.get("/api/health")
def health():
    """A lightweight endpoint for checking that the API is running."""
    return jsonify({"status": "ok"})


@app.get("/api/profile")
def profile():
    """Return all resume sections in one response for the frontend."""
    return jsonify(PROFILE)


if __name__ == "__main__":
    # The built-in server is for local learning and development, not production.
    app.run(
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", "5000")),
        debug=os.getenv("FLASK_DEBUG", "0") == "1",
    )
