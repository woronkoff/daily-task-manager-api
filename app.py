from flask import Flask, jsonify

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

@app.route("/tasks/<int:task_id>")
def get_task_by_id(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    
    return jsonify({
        "error": "Task not found"
    }), 404



if __name__ == "__main__":
    app.run(debug=True)