
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

TASKS_FILE = "data/tasks.json"

def load_tasks():
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Daily Task Manager API"
    })

@app.route("/tasks")
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route("/tasks/<int:task_id>")
def get_task_by_id(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    
    return jsonify({
        "error": "Task not found"
    }), 404

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if  data is None:
        return jsonify({
            "error": "Request body must be JSON"
        }), 400
    
    if "title" not in data:
        return jsonify({
            "error": "Task title is required"
        }), 400
    
    if not data["title"].strip():
        return jsonify({
            "error": "Task title cannot be empty"
        }), 400
    
    tasks = load_tasks()

    new_task = {
        "id": max([task["id"] for task in tasks], default=0) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify(new_task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    if  data is None:
        return jsonify({
            "error": "Request body must be JSON"
        }), 400
    
    if "title" in data and not data["title"].strip():
        return jsonify({
            "error": "Task title cannot be empty"
        }), 400
    
    if "completed" in data and type(data["completed"]) is not bool:
        return jsonify({
            "error": "Completed field must be true or false"
        }), 400

    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            if "title" in data:
                task["title"] = data["title"]
            
            if "completed" in data:
                task["completed"] = data["completed"]

            save_tasks(tasks)
            return jsonify(data)
    
    return jsonify({
        "error": "Task not found"
    }), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            
            return jsonify({
                "message": "Task deleted successfully"
            })
        
    return jsonify({
        "error": "Task not found"
    }), 404


if __name__ == "__main__":
    app.run(debug=True)