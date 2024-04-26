#!/usr/bin/env python3

"""
This module contains routes for the API.
"""

from flask import Blueprint, abort

app_views = Blueprint('app_views', __name__)

@app_views.route('/api/v1/unauthorized')
def unauthorized_route():
    """
    Route to raise a 401 error.
    """
    abort(401)
