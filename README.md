# Daily Task Manager API

This is a beginner Python Flask project created to practice backend development and REST API basics.

The API allows users to view daily tasks, get a specific task by ID, and create new tasks using JSON data. The project is being developed step by step as part of my daily programming practice.

## Project Status

This project is complete as a beginner Flask REST API practice project.

It includes CRUD operations, JSON file storage, input validation, error handling, and priority support.

## Features

- Flask API server
- Home route with welcome message
- Tasks endpoint returning a list of tasks
- Endpoint to get one task by ID
- Endpoint to create new tasks using POST requests
- JSON responses
- Simple project structure
- Endpoint to update existing tasks using PUT requests
- Endpoint to delete tasks using DELETE requests
- Saves tasks in a JSON file
- Input validation for task creation and updates
- Clear error messages for invalid requests
- Task priority support with low, medium, and high levels

## Skills Practiced

- Python
- Flask
- REST API basics
- JSON
- HTTP GET requests
- HTTP POST requests
- Git and GitHub
- Linux server practice
- HTTP PUT requests
- HTTP DELETE requests
- Reading and writing JSON files
- Input validation
- API error handling
- Data validation
- Working with optional JSON fields

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/<task_id>` | Get one task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/<task_id>` | Update a task |
| DELETE | `/tasks/<task_id>` | Delete a task |

## How to Run

Install the requirements:


	pip install -r requirements.txt


Run the app:

	python3 app.py

Test the API:

	curl http://127.0.0.1:5000/

Test the tasks endpoint:

	curl http://127.0.0.1:5000/tasks

## Current Endpoints
## Home
	GET /
Returns a welcome message.

Example:

	curl http://127.0.0.1:5000/

## Get All Tasks
	GET /tasks

Returns a list of tasks.

Example:

	curl http://127.0.0.1:5000/tasks

## Get Task by ID

	GET /tasks/<task_id>

Returns one task by its ID.

Example:

	curl http://127.0.0.1:5000/tasks/1

if the task does not exist, the API returns:

	{
		"error": "Task not found"
	}

## Create Task

	POST /tasks

Create a new task

	curl -X POST http://127.0.0.1:5000/tasks \
-H "Content-Type: application/json" \
-d '{"title": "Practice priority feature", "priority": "high"}'

Example response:

	{
		"completed": false,
		"id": 4,
		"priority": "high",
		"title": "Practice priority feature"
	}

## Update Task

	PUT /tasks/<task_id>

Update task 1:

	curl -X PUT http://127.0.0.1:5000/tasks/1 \
	-H "Content-Type: application/json" \
	-d '{"title": "Study Flask routes", "completed": true}'

Example response:

	{
  		"completed": true,
  		"id": 1,
  		"title": "Study Flask routes"
	}

## Delete Task

	DELETE /tasks/<task_id>

Delete tasks by id:

	curl -X DELETE http://127.0.0.1:5000/tasks/1

Example response:

	{
  		"message": "Task deleted successfully"
	}

## Notes

This repo is intentionally simple.
It is not abandoned.
It is finished for its learning purpose.
