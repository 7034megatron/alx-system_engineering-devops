#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":

  userId = sys.argv[1]
  url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(userId)

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
  except requests.exceptions.RequestException as e:
    print(f"Error: An error occurred while fetching data: {e}")
    sys.exit(1)

  tasks = response.json()
  name = None
  totalTasks = 0
  completed = 0

  for task in tasks:
    if task.get('userId') == int(userId):
      totalTasks += 1
      if task.get('completed'):
        completed += 1
      name = name or task.get('name')  # Assign name only once if available

  if not name:
    print(f"Error: User with ID {userId} not found.")
    sys.exit(1)

  print('Employee {} is done with tasks({}/{}):'.format(name, completed, totalTasks))
  print('\n'.join(["\t " + task.get('title') for task in tasks if task.get('completed')]))
