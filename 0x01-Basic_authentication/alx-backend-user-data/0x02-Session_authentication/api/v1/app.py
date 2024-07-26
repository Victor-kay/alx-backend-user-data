#!/usr/bin/env python3
"""
Main application module.
"""

import base64
from flask import Flask, jsonify, request, abort
from api.v1.auth import auth
from models.user import User

app = Flask(__name__)


@app.before_request
def before_request():
    request.current_user = auth.current_user(request)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
