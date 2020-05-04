#!/usr/bin/python3
""" python script to use a rest api """
import csv
import requests
from sys import argv as a

if __name__ == '__main__':
    users = 'https://jsonplaceholder.typicode.com/users/{}'.format(a[1])
    todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(a[1])
    file_name = '{}.csv'.format(a[1])

    user = requests.get(users).json()
    user_name = user.get('username')

    to_do = requests.get(todos).json()
    with open(file_name, mode='w') as employee:
            file_writer = csv.writer(employee, delimiter=',', quotechar='"',
                                     quoting=csv.QUOTE_ALL)
            for dic in to_do:
                file_writer.writerow([a[1], user_name, dic.get('completed'),
                                      dic.get('title')])
