#!/usr/bin/python3
# module to print data from an api
import urllib.request
import csv
import json
import sys


if __name__ == "__main__":
    numbertask = 0
    taskcomplete = 0
    tasksdone = []
    userid = sys.argv[1]
    url1 = 'https://jsonplaceholder.typicode.com/todos'
    with urllib.request.urlopen(url1) as response:
        html = response.read()
    dattod = json.loads(html.decode('utf-8'))
    with urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/' +
                                sys.argv[1]) as response:
        html = response.read()
    datuser = json.loads(html.decode('utf-8'))
    for item in dattod:
        if int(item['userId']) == int(userid):
            tasksdone.append(item)
    file1 = "{}.csv".format(userid)
    with open(file1, mode='w') as emplo_file:
        employee_writer = csv.writer(
            emplo_file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_NONNUMERIC)
        for taks in tasksdone:
            employee_writer.writerow([str(datuser['id']),
                                      datuser['username'],
                                      str(taks['completed']), taks['title']])
