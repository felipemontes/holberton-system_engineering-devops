#!/usr/bin/python3
""" python script to use a rest api and export to json"""
import json
import requests

if __name__ == '__main__':
    users = 'https://jsonplaceholder.typicode.com/users'
    todos = 'https://jsonplaceholder.typicode.com/todos'
    data = {}
    file_name = "todo_all_employees.json"

    users = requests.get(users).json()
    todos = requests.get(todos).json()
    for user in users:
        data[user.get('id')] = []
        for todo in todos:
            data[user.get('id')].append({
                'username': user.get('username'),
                'task': todo.get('title'),
                'completed': todo.get('completed')
            })

    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)
