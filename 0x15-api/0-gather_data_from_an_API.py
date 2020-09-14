#!/usr/bin/python3
""" Rest api employees """
if __name__ == "__main__":
    import requests
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    req = requests.get(url).json()
    EMPLOYEE_NAME = req.get('name')
    url_2 = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
            .format(argv[1])
    reqt = requests.get(url_2).json()
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    for ct in reqt:
        if ct.get("completed") is True:
            TASK_TITLE.append(ct.get("title"))
            NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS = len(reqt)
    print("employee {} is done with tasks({}/{}):".format
          (EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for ct2 in TASK_TITLE:
        print("\t {}".format(ct2))
