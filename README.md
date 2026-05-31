# Daily Task Manager API

This is a beginner Python Flask project created to practice backend development and REST API basics.

The API allows users to view daily tasks, get a specific task by ID, and create new tasks using JSON data. The project is being developed step by step as part of my daily programming practice.

## Features

- Flask API server
- Home route with welcome message
- Tasks endpoint returning a list of tasks
- Endpoint to get one task by ID
- Endpoint to create new tasks using POST requests
- JSON responses
- Simple project structure

## Skills Practiced

- Python
- Flask
- REST API basics
- JSON
- HTTP GET requests
- HTTP POST requests
- Git and GitHub
- Linux server practice

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
		"error": "Task not fount"
	}

## Create Task

	POST /tasks

Create a new task

	curl -X POST http://127.0.0.1:5000/tasks \
	-H "Content-type: application/json" \
	-d '{"title": "Pratice POST requests"}'

Example response:

	{
		"completed": false,
		"id": 4,
		"title": "Pratice POST requests"
	}

## Notes

This project is still in progress. I am building it step by step to practice Python, Flask, APIs, JSON, Git and backend development.

Currently the tasks are stored in a Python list. This means new tasks disappear when the server restarts. A future improvement will be savings tasks in JSON File or database.
