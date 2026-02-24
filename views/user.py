from flask import Blueprint, request, jsonify
from helper.user import read_user, write_user

users_blueprint = Blueprint('users', __name__) 

# user

# INDEX USER
@users_blueprint.route('/users')
def get_user():
    # inisiasi data dari users.json
    users = read_user()
    return jsonify({"users" : users})

# CREATE USER
@users_blueprint.route('/users', methods = ['POST'])
def add_user():
    # inisiasi data dari users.json
    users = read_user()
    data = request.get_json()
    
    if data:
        # new user
        new_user = {
        "id" : len(users) + 1,
        "name" : data['name'],
        "age" : data['age']
        }
        users.append(new_user)

        # tulis ulang semuanya
        write_user(users)
        # users.append(data)
        return jsonify({'message' : 'user added', 'user' : data}), 200
    else:
        return jsonify({'message' : 'kamu tidak menginputkan apapun'}), 400

# HANDLE UPDATE, VIEW, DELETE
@users_blueprint.route('/users/<int:user_id>' , methods = ['GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    if request.method == "GET":
        # inisiasi data dari users.json
        users = read_user()
        for user in users:
            if user["id"] == user_id:
                return jsonify({
                    "message" : "user barhasil di temukan",
                    "user" : user
                }), 201
        else:
            return jsonify({
                "message" : "user tidak ditemukan"
            }), 400
        
    elif request.method == "PUT":
        # inisiasi data dari users.json
        users = read_user()
        data = request.get_json()

        for user in users:
            if user["id"] == user_id:
                user["name"] = data.get("name", user["name"])
                user["age"] = data.get("age", user["age"])

                write_user(users)
                return jsonify(user)

        return jsonify({"error": "user not found"}), 404
    
    elif request.method == "DELETE":
        # inisiasi data dari users.json
        users = read_user()
        new_users = [u for u in users if u["id"] != user_id]

        if len(new_users) == len(users):
            return jsonify({"error": "user not found"}), 404

        write_user(new_users)
        return jsonify({"message": "user deleted"})
    
    else:
        return jsonify({'error' : "method not allowd"}), 403

