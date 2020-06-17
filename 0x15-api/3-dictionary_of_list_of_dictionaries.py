#!/usr/bin/python3
'''
data in the JSON format
'''
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    us = requests.get(url, verify=False).json()
    undoc = {}
    udoc = {}
    for user in us:
        uid = user.get("id")
        udoc[uid] = []
        undoc[uid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(url, verify=False).json()
    [udoc.get(t.get("userId")).append({"task": t.get("title"),
                                       "completed": t.get("completed"),
                                       "username": undoc.get(
                                               t.get("userId"))})
     for t in todo]
    with open("todo_all_employees.json", 'w') as jsf:
        json.dump(udoc, jsf)
