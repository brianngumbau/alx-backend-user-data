#!/usr/bin/env python3
"""
Module for authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template for all authentication system implemented in this app.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Method to determine if authorization is required
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and excluded_path == path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Method to retrieve the authorization header from a request
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to retrieve the current user
        """
        return None
