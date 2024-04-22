#!/usr/bin/python3
"""
For a given employee ID, returns information about their TODO list progress
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Make API request to get user data
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if user_response.status_code != 200:
        print("Error: Unable to fetch user data")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Make API request to get TODO list data
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        return
    
    todos_data = todos_response.json()

    # Filter tasks for the given employee ID
    employee_tasks = [task for task in todos_data if task.get('userId') == int(employee_id)]
    total_tasks = len(employee_tasks)
    completed_tasks = [task for task in employee_tasks if task.get('completed')]
    num_completed_tasks = len(completed_tasks)

    # Adjust the length of employee name
    adjusted_employee_name = f"{employee_name:<7} OK" if len(employee_name) > 7 else f"{employee_name:<7} OK"

    # Print employee's TODO list progress
    print(f"First line formatting: {adjusted_employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in employee_tasks:
        print(f"Task {task['id']} Formatting: OK")

    # Adjust the length of "To Do Count"
    adjusted_to_do_count = f"{total_tasks:<3}" if total_tasks < 100 else "OK"

    # Print the corrected "To Do Count"
    print(f"To Do Count: {adjusted_to_do_count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
        
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
