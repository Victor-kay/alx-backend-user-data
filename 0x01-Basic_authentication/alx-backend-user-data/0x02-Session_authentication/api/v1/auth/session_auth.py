#!/usr/bin/env python3

"""
This module provides the session-based authentication class.
"""

from api.v1.auth.auth import Auth

class SessionAuth(Auth):
    """
    Session-based authentication class.
    """

    def authenticate(self, request):
        """
        Authenticate the request using session-based mechanism.

        :param request: The request object.
        """
        pass
