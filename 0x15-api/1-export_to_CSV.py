#!/usr/bin/python3
""" Python script that, using this REST API, for
a given employee ID, returns
information about his/her TODO list progress."""

import json
from sys import argv
import requests


def get_employee_tasks(employeeId):
    """ Get employee tasks """
    url = f'https://jsonplaceholder.typicode.com/'
    users = f'users?id={id}'
    todos = f'todos?userId={id}'
    done = f'{todos}&completed=true'
    notDone = f'{todos}&completed=false'
    userData = requests.get(f'{url}{users}').json()
    Name = userData[0].get("name")
    userName = userData[0].get("username")
    todosData = requests.get(f'{url}{todos}').json()

    """Export into csv"""
    with open(f'{id}.csv', 'w') as f:
        for todo in todosData:
            data = f'"{id}","{userName}","{todo.get("completed")}",'
            data2 = f'"{todo.get("title")}"\n'
            f.write(data+data2)


if __name__ == "__main__":
    id = argv[1]
    get_employee_tasks(id)
