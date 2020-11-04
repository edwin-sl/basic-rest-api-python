from flask import Blueprint, jsonify, request
import db.db as db

todos_blueprint = Blueprint('todos', __name__, url_prefix='/todos')


@todos_blueprint.route('/', methods=['GET'])
def get_todos():
    return jsonify(db.select('todos'))


@todos_blueprint.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    return jsonify(db.select('todos', todo_id))


@todos_blueprint.route('/', methods=['POST'])
def post_todos():
    body = request.get_json()
    return jsonify(db.insert('todos', body))


@todos_blueprint.route('/<int:todo_id>', methods=['PUT'])
def put_todos(todo_id):
    body = request.get_json()
    body['id'] = todo_id
    return jsonify(db.update('todos', body))


@todos_blueprint.route('/<int:todo_id>', methods=['DELETE'])
def delete_todos(todo_id):
    return jsonify(db.delete('todos', todo_id))

