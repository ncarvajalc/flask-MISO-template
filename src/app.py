from flask import Flask
from database.db import init_db, db_session
from flask_restful import Api

from routes.user import UserListResource, UserResource


app = Flask(__name__)
Api = Api(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# Routes
Api.add_resource(UserListResource, "/users")
Api.add_resource(UserResource, "/users/<int:user_id>")


init_db()
