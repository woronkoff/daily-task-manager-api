# Daily Task Manager API

This is a beginner Python Flask project created to practice backend development and REST API basics.

The API allows users to view daily tasks in JSON format. The project is being developed step by step as part of my daily programming practice.

## Features

- Flask API server
- Home route with welcome message
- Tasks endpoint returning a list of tasks
- JSON responses
- Simple project structure

## Skills Practiced

- Python
- Flask
- REST API basics
- JSON
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

## Tasks
	GET /tasks

Returns a list of tasks.
