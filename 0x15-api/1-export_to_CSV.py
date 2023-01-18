#!/usr/bin/python3
"""
This script will export the data from the database to a CSV file
"""

import csv
import os
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(argv[1])).json()
    todo = requests.get(url + 'todos?userId={}'.format(argv[1])).json()
    with open('{}.csv'.format(argv[1]), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo:
            writer.writerow([argv[1], user.get('username'),
                            task.get('completed'), task.get('title')])
