#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    try:
        # Retrieve user information
        user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                                     .format(employee_id))
        user_data = user_response.json()
        name = user_data.get('name')

        # Retrieve TODO list for the employee
        todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
        todos_data = todos_response.json()

        # Filter tasks for the given employee
        employee_tasks = [task for task in todos_data if task.get('userId') == int(employee_id)]
        total_tasks = len(employee_tasks)
        completed_tasks = [task for task in employee_tasks if task.get('completed')]
        num_completed_tasks = len(completed_tasks)

        # Format and return output
        output = f'Employee {name} is done with tasks({num_completed_tasks}/{total_tasks}):\n'
        completed_tasks_titles = [task.get('title') for task in completed_tasks]
        output += '\n'.join(["\t " + title for title in sorted(completed_tasks_titles)])
        return output
        
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
        
    employee_id = sys.argv[1]
    print(get_employee_todo_progress(employee_id))
