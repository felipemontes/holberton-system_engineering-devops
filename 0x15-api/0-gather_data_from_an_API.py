#!/usr/bin/python3
""" python script to use a rest api """
import requests
from sys import argv as a

if __name__ == '__main__':
    users = 'https://jsonplaceholder.typicode.com/users/{}'.format(a[1])
    todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(a[1])
    task = 0
    done = 0
    c_tasks = []

    user = requests.get(users).json()
    name = user.get('name')

    to_do = requests.get(todos).json()
    for dic in to_do:
        task += 1
        if dic.get('completed') is True:
            done += 1
            c_tasks.append(dic.get('title'))

    print("Employee {} is done with tasks ({}/{})".format(name, done, task))
    for title in c_tasks:
        print("     {}".format(title))
