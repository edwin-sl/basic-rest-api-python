from flask import Blueprint, jsonify, request
import db.db as db

users_blueprint = Blueprint('users', __name__, url_prefix='/users')


@users_blueprint.route('/', methods=['GET'])
def get_users():
    return jsonify(db.select('users'))


@users_blueprint.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify(db.select('users', user_id))


@users_blueprint.route('/', methods=['POST'])
def post_users():
    body = request.get_json()
    return jsonify(db.insert('users', body))


@users_blueprint.route('/<int:user_id>', methods=['PUT'])
def put_users(user_id):
    body = request.get_json()
    body['id'] = user_id
    return jsonify(db.update('users', body))


@users_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_users(user_id):
    return jsonify(db.delete('users', user_id))


@users_blueprint.route('/<int:user_id>/todos', methods=['GET'])
def get_user_todos(user_id):
    return jsonify(db.select('todos', None, { 'userId': user_id }))