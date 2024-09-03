#!/usr/bin/env python3
""" BasicAuth module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization
        header for Basic Authentication.

        Args:
            authorization_header (str): The authorization header string.

        Returns:
            str: The Base64 encoded part of the header, or
            None if conditions are not met.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]


     def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 authorization header string.

        Args:
            base64_authorization_header (str): The Base64 encoded string.

        Returns:
            str: The decoded string as UTF-8, or None if decoding fails.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
