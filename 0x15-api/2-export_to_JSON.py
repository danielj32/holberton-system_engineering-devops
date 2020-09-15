#!/usr/bin/python3
""" Records all tasks that are owned by this employee """
from requests import get
from sys import argv
import json


def record_all(input):
    """ Record all tasks by emp_id """
    user = get('https://jsonplaceholder.typicode.com/users/' + input).json()
    if not user:
        return
    all_tasks = get('https://jsonplaceholder.typicode.com/todos/').json()
    emp_id = user.get('id')
    emp_username = user.get('username')
    tasks = [t for t in all_tasks if t['userId'] == emp_id]
    task_list = [{"task": t.get('title'),
                  "completed": t.get('completed'),
                  "username": emp_username} for t in tasks]
    to_json = {str(emp_id): task_list}
    with open("{}.json".format(emp_id), "w") as f:
        json.dump(to_json, f)


if __name__ == '__main__':
    if len(argv) == 2 and argv[1].isdigit():
        record_all(argv[1])
