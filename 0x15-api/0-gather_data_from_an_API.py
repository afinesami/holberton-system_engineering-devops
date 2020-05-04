#!/usr/bin/python3
''' module to print data from an api '''
import requests
import sys


def gather_data():
    ''' gathers data from the api '''
    try:
        userid = sys.argv[1]
    except:
        print('Usage: ./0-gather_data_from_an_API.py <employee ID>')
        return

    userurl = 'https://jsonplaceholder.typicode.com/users'

    t = requests.get(userurl+'/'+userid+'/todos')
    u = requests.get(userurl+'/'+userid)

    task_count = 0
    for task in t.json():
        task_count += 1
        for k, v in task.items():
            if k == 'completed' and v is True:
                if 'completed_task_count' not in locals():
                    completed_task_count = 0
                completed_task_count += 1

    user_dict = u.json()
    try:
        emp_name = (user_dict['name'])
    except:
        print("Employee does not exist.")
        return

    print(
        'Employee {} is done with tasks({}/{}):'.format(
            emp_name, completed_task_count, task_count))

    for task in t.json():
        task_dict = task
        if task_dict['completed'] is True:
            print('\t {}'.format(task_dict['title']))


if __name__ == '__main__':
    gather_data()
