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
        return False

    def authorization_header(self, request=None) -> str:
        """
        Method to retrieve the authorization header from a request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method to retrieve the current user
        """
        return None
