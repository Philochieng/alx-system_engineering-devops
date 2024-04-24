#!/usr/bin/python3
"""
Script to export data in the JSON format
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    # Fetching users and todos data
    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)

    # Converting to JSON format
    users = response_users.json()
    todos = response_todos.json()

    # Creating dictionary to store tasks of each user
    todo_dict = {}

    # Populating the todo_dict with user tasks
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        todo_dict[user_id] = []
        for todo in todos:
            if todo.get('userId') == user_id:
                task = {
                    "username": username,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                }
                todo_dict[user_id].append(task)

    # Writing data to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_dict, jsonfile)

