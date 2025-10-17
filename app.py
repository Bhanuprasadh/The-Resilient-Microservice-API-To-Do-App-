from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Simple in-memory storage for demo
todos = []
next_id = 1

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    global next_id
    data = request.get_json()
    todo = {
        'id': next_id,
        'task': data['task'],
        'completed': False
    }
    todos.append(todo)
    next_id += 1
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)