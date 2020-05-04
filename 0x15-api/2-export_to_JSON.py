#!/usr/bin/python3
# exports data in the JSON format
import json
import requests
import sys
from collections import OrderedDict


def gather_data():
    ''' retrieves data from the api '''
    userurl = 'https://jsonplaceholder.typicode.com/users'

    t = requests.get(userurl+'/'+userid+'/todos')
    u = requests.get(userurl+'/'+userid)

    user_dict = u.json()
    try:
        emp_name = (user_dict['username'])
    except:
        print("Employee does not exist.")
        return

    task_dict = {}
    task_vals = []

    for i in t.json():
        std = OrderedDict()
        std['task'] = i['title']
        std['completed'] = i['completed']
        std['username'] = emp_name
        task_vals.append(std)

    task_dict[str(userid)] = task_vals

    return task_dict


def save_to_json(data, userid):
    ''' saves data to JSON '''
    f = str(userid)+'.json'
    with open(f, mode='w', encoding="UTF8") as fd:
        json.dump(data, fd)


if __name__ == '__main__':
    try:
        userid = sys.argv[1]
    except:
        raise NameError('Usage: ./2-export_to_JSON.py <employee ID>')

    task_dict = gather_data()
    save_to_json(task_dict, userid)
