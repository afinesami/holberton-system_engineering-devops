#!/usr/bin/python3
# Gather data from an api

import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    todo = requests.get(url, verify=False).json()
    completed_tasks = [task.get("title")
                       for task in todo if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todo)))
    for task in completed_tasks:
        print("\t {}".format(task))
