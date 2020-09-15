#!/usr/bin/python3
""" export data json """
from requests import get
import json
from pprint import pprint


def record_all():
    """ all tasks by emp_id """
    users = get('https://jsonplaceholder.typicode.com/users/').json()
    if not users:
        return
    all_tasks = get('https://jsonplaceholder.typicode.com/todos/').json()
    to_json = {}
    for u in users:
        emp_id = u.get('id')
        emp_username = u.get('username')
        tasks = [t for t in all_tasks if t['userId'] == emp_id]
        task_list = [{"task": t.get('title'),
                      "completed": t.get('completed'),
                      "username": emp_username} for t in tasks]
        to_json[str(emp_id)] = task_list
    with open("todo_all_employees.json", "w") as f:
        json.dump(to_json, f)


if __name__ == '__main__':
    record_all()
