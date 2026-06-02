from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Study Python",
        "completed": False
    },
    {
        "id": 2,
        "title": "Practice Flask",
        "completed": False
    },
    {
        "id": 3,
        "title": "Push project to GitHub",
        "completed": True
    }
]

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Daily Task Manager API"
    })

@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({
            "error": "Title is required"
        }), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(new_task)

    return jsonify(new_task), 201

@app.route("/tasks/<int:task_id>")
def get_task_by_id(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    
    return jsonify({
        "error": "Task not found"
    }), 404

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    for task in tasks:
        if task["id"] == task_id:
            if "title" in data:
                task["title"] = data["title"]
            
            if "completed" in data:
                task["completed"] = data["completed"]

            return jsonify(data)
    
    return jsonify({
        "error": "Task not found"
    }), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({
                "message": "Task deleted successfully"
            })
        
        return jsonify({
            "error": "Task not found"
        }), 404


if __name__ == "__main__":
    app.run(debug=True)