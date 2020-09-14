#!/usr/bin/python3
""" Rest api employees """
import requests
from sys import argv

users = requests.get(
        "https://jsonplaceholder.typicode.com/users?id=" + argv[1])
todos = requests.get(
    "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1])

users_json = users.json()
todos_json = todos.json()
done_tasks = 0
total_tasks = 0
task_list = []

for data in todos_json:
    if data['completed'] is True:
        done_tasks += 1
        task_list.append(data['title'])
        total_tasks += 1

employee_name = users_json[0]['name']

print("Employee {} is done with tasks({}/{}):".
      format(employee_name, done_tasks, total_tasks))

for task in task_list:
    print('\t ' + task)
