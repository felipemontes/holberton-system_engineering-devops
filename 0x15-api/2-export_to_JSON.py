#!/usr/bin/python3
""" python script to use a rest api and export to json"""
import json
import requests
from sys import argv as a

if __name__ == '__main__':
    users = 'https://jsonplaceholder.typicode.com/users/{}'.format(a[1])
    todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(a[1])
    data = {}
    file_name = "{}.json".format(a[1])

    user = requests.get(users).json()
    user_name = user.get('username')

    to_do = requests.get(todos).json()

    data[a[1]] = []
    for dic in to_do:

        data[a[1]].append({
            'task': dic.get('title'),
            'completed': dic.get('completed'),
            'username': user_name
            })

    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)
