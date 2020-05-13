#!/usr/bin/python3
# exports data in the JSON format

import json
import requests
import sys
from collections import OrderedDict


def gather_data():
    ''' retrieves data from the api '''
    userurl = 'https://jsonplaceholder.typicode.com/users'

    u = requests.get(userurl)

    user_list = u.json()
    user_task_dict = {}

    for user in user_list:
        task_dict = {}
        task_vals = []
        t = requests.get(
            'https://jsonplaceholder.typicode.com/users/' + str(user['id']) +
            '/todos')
        for i in t.json():
            std = OrderedDict()
            std['username'] = user['username']
            std['task'] = i['title']
            std['completed'] = i['completed']
            task_vals.append(std)
        user_task_dict[user['id']] = task_vals

    return user_task_dict


def save_to_json(data):
    ''' saves data to JSON '''
    f = 'todo_all_employees.json'
    with open(f, mode='w', encoding="UTF8") as fd:
        json.dump(data, fd)


if __name__ == '__main__':
    task_dict = gather_data()
    save_to_json(task_dict)
