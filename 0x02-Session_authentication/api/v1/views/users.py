#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """ GET /api/v1/users
    Return:
      - list of all User objects JSON represented
    """
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """ GET /api/v1/users/:id
    Path parameter:
      - User ID
    Return:
      - User object JSON represented
      - 404 if the User ID doesn't exist
    """
    if user_id is None:
        abort(404)
    # If the user_id is "me" and there is no current_user, return a 404 error
    if user_id == 'me':
        if request.current_user is None:
            abort(404)
        else:
            # If the user_id is "me" and there is a current_user, return the
            # JSON representation of the current_user
            return jsonify(request.current_user.to_json())
    # If user_id is None, return a 404 error
    if user_id is None:
        abort(404)
    # Retrieve the user from the database using the User.get method
    user = User.get(user_id)
    # If the user was not found, return a 404 error
    if user is None:
        abort(404)
    # Return the JSON representation of the user
    return jsonify(user.to_json())
