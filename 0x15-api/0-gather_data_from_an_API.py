#!/usr/bin/python3

"""
Script to gather data from a REST API about an employee's TODO list progress.
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieve and display information about the TODO list progress of a given employee.

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
    employee_name = user_data.get("name")
    total_tasks = len(todos)
    completed_tasks = sum(todo.get("completed", False) for todo in todos)

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo.get("completed"):
            print(f"\t{todo.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

