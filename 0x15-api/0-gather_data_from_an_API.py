#!/usr/bin/python3
"""
For a given employee ID, returns information about their TODO list progress
"""

import sys
import requests

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

    # Print employee's TODO list progress
    print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
        
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
