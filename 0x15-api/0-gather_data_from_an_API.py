#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <user_id>")
    sys.exit(1)

user_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/"

# Fetch user data
user = requests.get(url + "users/{}".format(user_id)).json()

# Fetch todos for the user
todos = requests.get(url + "todos", params={"userId": user_id}).json()

# Process the data
user_name = user.get('name')
completed_tasks = [task['title'] for task in todos if task['completed']]

print("Employee {} is done with tasks({}/{}):".format(
    user_name, len(completed_tasks), len(todos)))

for task in completed_tasks:
    print("\t", task)

