import os
from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI, tls=True, tlsAllowInvalidCertificates=True)

db = client['Tutorial7']
collection = db['users']


@app.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint.

    Returns:
        JSON response with a message and success status.
    """
    return jsonify({"message": "Healthy", "success": True}), 200


@app.route("/db-health", methods=["GET"])
def db_health_check():
    """
    Database health check endpoint.

    Returns:
        JSON response with a message and success status.
    """

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        server_info = client.server_info()
        print(server_info)
        return jsonify({"message": "Database connection is healthy", "success": True}), 200
    except PyMongoError as e:
        return jsonify({"message": f"Database connection failed: {str(e)}", "success": False}), 500


@app.route("/users", methods=["GET"])
def get_users():
    """
    Get a list of all users.

    Returns:
        JSON response with a message, success status, and list of users.
    """
    try:
        result = collection.find()
        users = []

        for user in result:
            user["_id"] = str(user["_id"])
            users.append(user)

        return jsonify({"message": "Users retrieved", "success": True, "users": users}), 200
    except PyMongoError as e:
        return jsonify({"message": f"Error retrieving users: {str(e)}", "success": False}), 500


@app.route("/add", methods=["POST"])
def add_user():
    """
    Add a new user.

    Returns:
        JSON response with a message and success status.
    """
    if not request.json or 'email' not in request.json or 'firstName' not in request.json:
        return jsonify({"message": "Invalid request data", "success": False}), 400
    try:
        user_data = request.json
        result = collection.insert_one(user_data)
        return jsonify({"message": "User added", "success": True, "user_id": str(result.inserted_id)}), 201
    except PyMongoError as e:
        return jsonify({"message": f"Error adding user: {str(e)}", "success": False}), 500


@app.route("/update/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    """
    Update an existing user by ID.

    Args:
        user_id (str): The ID of the user to update.

    Returns:
        JSON response with a message and success status.
    """
    if not request.json or ('email' not in request.json and 'firstName' not in request.json):
        return jsonify({"message": "Invalid request data", "success": False}), 400
    try:
        update_data = request.json
        result = collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
        if result.matched_count > 0:
            return jsonify({"message": "User updated", "success": True}), 200
        return jsonify({"message": "User not found", "success": False}), 404
    except PyMongoError as e:
        return jsonify({"message": f"Error updating user: {str(e)}", "success": False}), 500


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
        user = collection.find_one({"_id": ObjectId(user_id)})
        if user:
            user["_id"] = str(user["_id"])
            return jsonify({"success": True, "user": user}), 200
        return jsonify({"message": "User not found", "success": False}), 404
    except PyMongoError as e:
        return jsonify({"message": f"Error retrieving user: {str(e)}", "success": False}), 500


@app.route("/delete/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Delete a user by their ID.

    Args:
        user_id (str): The ID of the user to delete.

    Returns:
        JSON response with a message and success status.
    """
    try:
        result = collection.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count > 0:
            return jsonify({"message": "User deleted", "success": True}), 200
        return jsonify({"message": "User not found", "success": False}), 404
    except PyMongoError as e:
        return jsonify({"message": f"Error deleting user: {str(e)}", "success": False}), 500


@app.errorhandler(405)
def method_not_allowed(error):
    """
    Handle Method Not Allowed errors.

    Returns:
        JSON response with a message and success status.
    """
    return jsonify({"message": "Method Not Allowed", "success": False}), 405


@app.errorhandler(404)
def not_found(error):
    """
    Handle Not Found errors.

    Returns:
        JSON response with a message and success status.
    """
    return jsonify({"message": "Not Found", "success": False}), 404


if __name__ == "__main__":
    # Run the app
    app.run(host="0.0.0.0", port=5000, debug=True)
