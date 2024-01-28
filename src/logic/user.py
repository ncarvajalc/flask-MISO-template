from models.user import User
from database.db import db_session
from schemas.user import user_schema, users_schema
from flask import abort


def get_users():
    users = db_session.query(User).all()
    return users_schema.dump(users)


def get_user_by_id(user_id):
    user = db_session.query(User).filter(User.id == user_id).first()
    if user is None:
        abort(404, description="User not found")
    return user_schema.dump(user)


def create_user(name, email):
    new_user = User(name=name, email=email)
    db_session.add(new_user)
    db_session.commit()
    return user_schema.dump(new_user), 201


def update_user(user_id, name, email):
    user = db_session.query(User).filter(User.id == user_id).first()
    if user is None:
        abort(404, description="User not found")
    if name is not None:
        user.name = name
    if email is not None:
        user.email = email
    db_session.commit()
    return user_schema.dump(user)


def delete_user(user_id):
    user = db_session.query(User).filter(User.id == user_id).first()
    if user is None:
        abort(404, description="User not found")
    db_session.delete(user)
    db_session.commit()
    return "", 204
