from flask import Blueprint, jsonify, request

# Create a Blueprint for organizing routes
app_routes = Blueprint('app_routes', __name__)

# In-memory storage for users
users = []

# Route to GET all users
@app_routes.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200  # Respond with the list of users

# Route to POST (add) a new user
@app_routes.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()  # Get user data from request body (JSON)
    users.append(data)  # Add the user to the in-memory list
    return jsonify({"message": "User added successfully", "user": data}), 201

# Route to delete all users (DELETE /users)
@app_routes.route('/users', methods=['DELETE'])
def delete_all_users():
    global users
    users.clear()  # Clear the in-memory list of users
    return jsonify({"message": "All users deleted successfully"}), 200
