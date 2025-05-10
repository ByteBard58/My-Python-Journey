from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with, marshal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///datahub.db"
db = SQLAlchemy(app)
api = Api(app)     # Initializes Flask-RESTful API

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Integer primary key
    name = db.Column(db.String(100), nullable=False, unique=True)
    # Required, unique string (100 chars)
    email = db.Column(db.String(100), nullable=False, unique=True)
    # Required, unique string (100 chars)
    tag = db.Column(db.String(50), nullable=False)
    # Required string (50 chars)

    def __repr__(self):
        # Defines string representation
        return f"User name: {self.name}, email: {self.email}"
        # Returns formatted user info

user_args = reqparse.RequestParser()
# Creates parser for request arguments

user_args.add_argument("name", type=str, required=True, help="Name of the user is required")
# Adds required 'name' string argument

user_args.add_argument("email", type=str, required=True, help="Email of the user is required")
# Adds required 'email' string argument

user_args.add_argument("tag", type=str, required=True, help="Tag(GOAT/Bokri/whatever) of the user is required")
# Adds required 'tag' string argument

user_fields = {
    # Defines serialized output structure
    "id": fields.Integer,
    # Integer field for id
    "name": fields.String,
    # String field for name
    "email": fields.String,
    # String field for email
    "tag": fields.String
    # String field for tag
}

class Users(Resource):
    # Resource for '/api/users'
    @marshal_with(user_fields)
    # Serializes response
    def get(self):
        # Handles GET request
        users = UserModel.query.all()
        # Fetches all users
        return users
        # Returns serialized users
    
    @marshal_with(user_fields)
    # Serializes response
    def post(self):
        # Handles POST request
        args = user_args.parse_args()
        # Parses request arguments
        user = UserModel(name=args["name"], email=args["email"], tag=args["tag"])
        # Creates new user
        db.session.add(user)
        # Adds user to session
        db.session.commit()
        # Commits to database
        users = UserModel.query.all()
        # Fetches all users
        return users, 201
        # Returns users with 201 status

class User(Resource):
    # Resource for '/api/users/<id>'
    @marshal_with(user_fields)
    # Serializes response
    def get(self, id):
        # Handles GET request for user
        user = UserModel.query.get(id)
        # Fetches user by ID
        if not user:
            # Checks if user exists
            abort(404, message="No user with that ID could be found")
            # Returns 404 if not found
        return user, 200
        # Returns user with 200 status

    def patch(self, id):
        # Handles PATCH request
        args = user_args.parse_args()
        # Parses updated arguments
        user = UserModel.query.get(id)
        # Fetches user by ID
        if not user:
            # Checks if user exists
            abort(404, message="No user of that id could be found")
            # Returns 404 if not found
        user.name = args["name"]
        # Updates name
        user.email = args["email"]
        # Updates email
        user.tag = args["tag"]
        # Updates tag
        db.session.commit()
        # Commits changes
        userv2 = UserModel.query.get(id)
        # Fetches updated user
        return {
            # Returns update info
            "message": f"Info of User {id} was updated successfully",
            # Success message
            "Updated": marshal(userv2, user_fields)
            # Serialized updated user
        }

    def delete(self, id):
        # Handles DELETE request
        user = UserModel.query.get(id)
        # Fetches user by ID
        if not user:
            # Checks if user exists
            abort(404, message="No user of that id could be found")
            # Returns 404 if not found
        db.session.delete(user)
        # Deletes user
        db.session.commit()
        # Commits deletion
        users = UserModel.query.all()
        # Fetches remaining users
        return {
            # Returns deletion info
            "message": f"User {id} was deleted successfully",
            # Success message
            "current users": marshal(users, user_fields)
            # Serialized remaining users
        }, 200
        # Returns with 200 status

api.add_resource(Users, '/api/users')
# Registers Users resource

api.add_resource(User, "/api/users/<int:id>")
# Registers User resource

@app.route('/')
# Defines root route
def index():
    # Handles root request
    return render_template('index.html')
    # Renders index.html

if __name__ == '__main__':
    # Checks if script is run directly
    app.run(debug=True)
    # Runs app in debug mode
