#!/usr/bin/python3

"""
Script to gather data from a REST API about an employee's TODO list progress
and export it to a JSON file.
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve information about the TODO list progress of a given employee
    and export it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data from the API")
        return

    todos = response.json()

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("Failed to fetch user data from the API")
        return

    user_data = user_response.json()
    employee_name = user_data.get("username")

    tasks_data = {
        str(employee_id): [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee_name
            }
            for todo in todos
        ]
    }

    filename = f"{employee_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump(tasks_data, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

