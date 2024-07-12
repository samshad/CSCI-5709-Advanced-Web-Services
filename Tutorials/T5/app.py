import json
import os
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_FILE = 'DB.json'


def initialize_db():
    """Initialize the DB.json file if it doesn't exist."""
    if not os.path.isfile(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump({"users": []}, f, indent=4)


def fetch_users():
    """Load users from the DB.json file."""
    with open(DB_FILE, 'r') as f:
        return json.load(f)["users"]


def save_users(users):
    """Save users to the DB.json file."""
    with open(DB_FILE, 'w') as f:
        json.dump({"users": users}, f, indent=4)


def get_user_by_id(user_id):
    """Get a user by their ID."""
    users = fetch_users()
    for user in users:
        if user["id"] == user_id:
            return user
    return None


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "message": "Healthy",
        "success": True
    }), 200


@app.route("/users", methods=["GET"])
def get_users():
    """
    Get a list of all users.

    Returns:
        JSON response with a message, success status, and list of users.
    """
    try:
        users = fetch_users()
        return jsonify({
            "message": "Users retrieved",
            "success": True,
            "users": users
        }), 200
    except Exception as e:
        return jsonify({
            "message": f"Error retrieving users: {str(e)} !!!",
            "success": False
        }), 500


@app.route("/add", methods=["POST"])
def add_user():
    """
    Add a new user.

    Returns:
        JSON response with a message and success status.
    """
    try:
        new_user = request.json
        users = fetch_users()
        new_user['id'] = str(len(users) + 1)
        users.append(new_user)
        save_users(users)
        return jsonify({
            "message": "User added",
            "success": True
        }), 201
    except Exception as e:
        return jsonify({
            "message": f"Error adding user: {str(e)} !!!",
            "success": False
        }), 500


@app.route("/update/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    """
    Update an existing user by ID.

    Args:
        user_id (str): The ID of the user to update.

    Returns:
        JSON response with a message and success status.
    """
    try:
        updated_data = request.json
        users = fetch_users()
        for user in users:
            if user["id"] == user_id:
                user.update(updated_data)
                save_users(users)
                return jsonify({
                    "message": "User updated",
                    "success": True
                }), 200
        return jsonify({
            "message": "User not found",
            "success": False
        }), 404
    except Exception as e:
        return jsonify({
            "message": f"Error updating user: {str(e)} !!!",
            "success": False
        }), 500


@app.route("/user/<string:user_id>", methods=["GET"])
def get_user(user_id):
    """
    Get a user by their ID.

    Args:
        user_id (str): The ID of the user to retrieve.

    Returns:
        JSON response with a success status and the user object.
    """
    try:
        user = get_user_by_id(user_id)
        if user:
            return jsonify({
                "success": True,
                "user": user
            }), 200
        return jsonify({
            "message": "User not found",
            "success": False
        }), 404
    except Exception as e:
        return jsonify({
            "message": f"Error retrieving user: {str(e)} !!!",
            "success": False
        }), 500


if __name__ == "__main__":
    initialize_db()
    app.json.sort_keys = False
    app.run(host="0.0.0.0", port=5000, debug=True)
