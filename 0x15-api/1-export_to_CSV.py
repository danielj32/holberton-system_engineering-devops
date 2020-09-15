#!/usr/bin/python3
""" tasks that are owned by this employee """
from requests import get
from sys import argv
import csv


def record_tasks(input):
    """record of task """
    user = get('https://jsonplaceholder.typicode.com/users/' + input).json()
    if not user:
        return
    all_tasks = get('https://jsonplaceholder.typicode.com/todos/').json()
    emp_id = user.get('id')
    emp_username = user.get('username')
    tasks = [t for t in all_tasks if t['userId'] == emp_id]
    to_csv = [{"id": emp_id,
               "name": emp_username,
               "completed": t.get('completed'),
               "title": t.get('title')} for t in tasks]
    keys = ['id', 'name', 'completed', 'title']
    with open("{}.csv".format(emp_id), "w") as f:
        dict_writer = csv.DictWriter(f, keys, quoting=csv.QUOTE_ALL)
        dict_writer.writerows(to_csv)


if __name__ == '__main__':
    if len(argv) == 2 and argv[1].isdigit():
        record_tasks(argv[1])
