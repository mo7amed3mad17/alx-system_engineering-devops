#!/usr/bin/python3

""" First API dealing """

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
            TOTAL_NUMBER_OF_TASKS = len(tasks)
            NUMBER_OF_DONE_TASKS = sum(1 for task in tasks if task['completed'])

            # Get the employee name
            EMPLOYEE_NAME = user_r_j[int(i_d)]['name']

            # Print the employee TODO list progress
            print(f"Employee {EMPLOYEE_NAME} is done with " +
                  f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

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
