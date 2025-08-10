from flask import Flask, request, jsonify
app = Flask(__name__)
users = {}
next_id = 1
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    data = request.get_json()
    user_id = next_id
    users[user_id] = {"id": user_id, "name": data["name"],"email": data["email"]}
    next_id += 1
    return jsonify(users[user_id]), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    if "name" in data:
        users[user_id]["name"] = data["name"]
    if "email" in data:
        users[user_id]["email"] = data["email"]
    return jsonify(users[user_id]), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted","user":deleted_user}), 200

if __name__ == '__main__':
    app.run(debug=True)