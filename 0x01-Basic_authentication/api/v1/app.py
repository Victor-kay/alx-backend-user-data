#!/usr/bin/env python3
"""
Main module for the Flask API.
"""
from flask import Flask, jsonify
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.register_blueprint(app_views)

@app.errorhandler(401)
def unauthorized(error):
    """
    Error handler for 401 Unauthorized.
    """
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
