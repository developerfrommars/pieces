from functools import wraps
from flask import request
from argon2 import PasswordHasher

ph = PasswordHasher()

def argon(passwd: str):
    return ph.hash(passwd)


def hash_with(method):
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = request.json
            data['password'] = {
                'argon': argon
            }.get(method)(request.json.get('password'))
            return func(*args, **kwargs)
        return wrapper
    return decorator