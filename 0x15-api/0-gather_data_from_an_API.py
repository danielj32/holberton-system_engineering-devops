#!/usr/bin/python3
""" Rest api employees """
import requests
from sys import argv

try:
    int(argv[1])
    id_user = argv[1]
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id_user))
    user_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={
            'userId': id_user})

    username = user_data.json()['name']
    user_tasks_json = user_tasks.json()

    tasks_completed = []
    total_tasks = len(user_tasks_json)
    for task in user_tasks_json:
        if task['completed']:
            tasks_completed.append(task['title'])

    print('Employee {} is done with tasks({}/{}):'.format(username,
                                                          len(tasks_completed),
                                                          total_tasks))
    for task in tasks_completed:
        print('\t {}'.format(task))
except Exception:
    print('Not a valid argument')
