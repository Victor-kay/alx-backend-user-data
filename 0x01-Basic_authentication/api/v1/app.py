#!/usr/bin/env python3

"""
This module contains the main Flask application.
"""

from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(401)
def unauthorized(error):
    """
    Error handler for 401 Unauthorized.
    """
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
