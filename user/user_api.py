from flask import Flask, Blueprint, url_for, json,request, Response, jsonify
from werkzeug.exceptions import BadRequest
import sys
import sqlalchemy
import psycopg2
import os
import uuid

from user.utils.db import get_engine
from user.utils.validators import validate_new_user
from user.utils.hashes import hash_with

from user.models.user import User

user_api = Blueprint('user_api', __name__)


@user_api.route('/new', methods=['POST'])
@hash_with('argon')
@validate_new_user
def new(*args, **kwargs) -> tuple:
    req_data = request.json
    user = User(user_id=str(uuid.uuid4()), **req_data)
    engine = get_engine()
    try:
        Session = sqlalchemy.orm.sessionmaker(bind=engine)
        sess = Session()    
        user_id = sess.query(User.user_id).filter_by(email=req_data.get('email')).first()
        if user_id is None:
            sess.add(user)
            sess.commit()
            return {'success': 'you registered successfully'}, 200
        else:
            raise(BadRequest)
    except sqlalchemy.exc.OperationalError as e:
        return {'error': 'service down'}, 500
    except BadRequest as e:
        return {'error': 'email already in use'}, 400

