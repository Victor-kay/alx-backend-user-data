#!/usr/bin/env python3
"""
User view module for handling user-related routes.
"""

from flask import Flask, jsonify, request, abort
from models.user import User

@app.route('/api/v1/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    if user_id == 'me':
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict()), 200
    else:
        user = User.get(user_id)
        if not user:
            abort(404)
        return jsonify(user.to_dict()), 200
