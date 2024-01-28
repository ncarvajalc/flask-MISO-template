from flask import request
from flask_restful import Resource
from models.user import User
from database.db import db_session
from schemas.user import user_schema, users_schema


class UserListResource(Resource):
    def get(self):
        users = db_session.query(User).all()
        return users_schema.dump(users)

    def post(self):
        new_user = User(name=request.json["name"], email=request.json["email"])
        db_session.add(new_user)
        db_session.commit()
        return user_schema.dump(new_user), 201


class UserResource(Resource):
    def get(self, user_id):
        user = db_session.query(User).filter(User.id == user_id).first()

        if user is None:
            return {"message": "User not found"}, 404

        return user_schema.dump(user)

    def put(self, user_id):
        user = db_session.query(User).filter(User.id == user_id).first()

        if user is None:
            return {"message": "User not found"}, 404

        if "name" in request.json:
            user.name = request.json["name"]
        if "email" in request.json:
            user.email = request.json["email"]

        db_session.commit()
        return user_schema.dump(user)

    def delete(self, user_id):
        user = db_session.query(User).filter(User.id == user_id).first()

        if user is None:
            return {"message": "User not found"}, 404

        db_session.delete(user)
        db_session.commit()
        return "", 204
