#!/usr/bin/python3
'''
export data in the CSV format
'''

import csv
import requests
from sys import argv

if __name__ == '__main__':
    uid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        uid)
    todo = requests.get(url, verify=False).json()
    with open("{}.csv".format(uid), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for t in todo:
            taskwriter.writerow([int(uid), user.get('username'),
                                 t.get('completed'),
                                 t.get('title')])
