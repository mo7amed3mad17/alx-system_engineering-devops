#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves the TODO list progress for the given employee ID.
    """
    i_d = sys.argv[1]

    try:
        # API endpoint URL
        url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        user = f"https://jsonplaceholder.typicode.com/users"

        # Send a GET request to the API
        res = requests.get(url)
        user_r = requests.get(user)
        user_r_j = user_r.json()

        # Check if the request was successful
        if res.status_code == 200:
            # Get the list of tasks for the employee
            tasks = res.json()

            # Count the number of completed and total tasks
            total_tasks = len(tasks)
            completed_tasks = sum(1 for task in tasks if task['completed'])

            # Get the employee name
            employee_name = user_r_j[int(i_d)]['name']

            # Print the employee TODO list progress
            print(f"Employee {employee_name} is done with " +
                  f"tasks({completed_tasks}/{total_tasks}):")

            # Print the titles of the completed tasks
            for task in tasks:
                if task['completed']:
                    print(f"\t {task['title']}")

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Check if the user provided an employee ID as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
