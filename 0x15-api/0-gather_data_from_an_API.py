#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(user_id)).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id)).json()
    done_tasks = [task for task in todos if task.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(done_tasks), len(todos)))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
