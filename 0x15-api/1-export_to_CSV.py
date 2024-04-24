#!/usr/bin/python3

"""
Script to gather data from a REST API about an employee's TODO list progress
and export it to a CSV file.
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve information about the TODO list progress of a given employee
    and export it to a CSV file.

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

    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(todo.get("completed")),
                "TASK_TITLE": todo.get("title")
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

