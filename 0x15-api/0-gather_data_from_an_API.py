#!/usr/bin/python3
"""
For a given employee ID, returns information about their TODO list progress
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Make API request to get user data
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if user.status_code != 200:
        print("Error: Unable to fetch user data")
        return
    
    name = user.json().get('name')

    # Make API request to get TODO list data
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    if todos.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        return
    
    total_tasks = 0
    completed = 0
    completed_tasks_titles = []

    for task in todos.json():
        if task.get('userId') == int(employee_id):
            total_tasks += 1
            if task.get('completed'):
                completed += 1
                completed_tasks_titles.append(task.get('title'))

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, total_tasks))

    print('\n'.join(["\t " + title for title in completed_tasks_titles]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
        
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
