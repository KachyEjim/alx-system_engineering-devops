#!/usr/bin/python3
""" Python script that, using this REST API, for
a given employee ID, returns
information about his/her TODO list progress."""

import json
from sys import argv
import requests


def get_employee_tasks(id):
    """ Get employee tasks """
    url = f'https://jsonplaceholder.typicode.com/'
    users = f'users?id={id}'
    todos = f'todos?userId={id}'
    userData = requests.get(f'{url}{users}').json()
    userName = userData[0].get("username")
    todosData = requests.get(f'{url}{todos}').json()

    """Export into csv"""
    with open(f'{id}.json', 'w') as f:
        data = {id: []}
        for todo in todosData:
            temp = {id: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": userName,}]
                }
            
        json.dump(data, f)


if __name__ == "__main__":
    id = argv[1]
    get_employee_tasks(id)
