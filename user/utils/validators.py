from functools import wraps
from flask import request, jsonify, json

from ..models.user import User


def validate_new_user(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_fields = User.get_fields()
        if not request.json or all(val in request.get_json().keys() for val in user_fields):
            return func(args, kwargs)
        else:
            return jsonify({"error": "bad request"}), 400
    return wrapper