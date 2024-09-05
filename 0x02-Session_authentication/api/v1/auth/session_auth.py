#!/usr/bin/env python3
"""Session authentication module for the API.
"""


from uuid import uuid4

from models.user import User

from .auth import Auth


class SessionAuth(Auth):
    """Session Authentication class that inherits from Auth"""
    user_id_by_session_id = {}


    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id."""

        if type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
