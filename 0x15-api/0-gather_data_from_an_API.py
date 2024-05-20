#!/usr/bin/python3
""" Python script that, using this REST API, for
a given employee ID, returns
information about his/her TODO list progress."""

import json
from sys import argv
import urllib
import urllib.request


def get_employee_tasks(employeeId):
    """ Get employee tasks """
    url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        employeeId)
    url_users_name = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employeeId)
    response_todos = urllib.request.urlopen(url_todos).read()
    response_user = urllib.request.urlopen(url_users_name).read()
    data_todos = json.loads(response_todos)
    data_user = json.loads(response_user)

    tasks = []
    for task in data_todos:
        if task.get('completed') is True:
            tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        data_user.get('name'), len(tasks), len(data_todos)))
    for task in tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    id = argv[1]
    get_employee_tasks(id)
