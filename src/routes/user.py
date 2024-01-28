from flask import request
from flask_restful import Resource
from models.user import User
from database.db import db_session
from schemas.user import user_schema, users_schema
from logic.user import get_users, get_user_by_id, create_user, update_user, delete_user


class UserListResource(Resource):
    def get(self):
        return get_users()

    def post(self):
        return create_user(request.json["name"], request.json["email"])


class UserResource(Resource):
    def get(self, user_id):
        return get_user_by_id(user_id)

    def put(self, user_id):
        return update_user(user_id, request.json["name"], request.json["email"])

    def delete(self, user_id):
        return delete_user(user_id)
