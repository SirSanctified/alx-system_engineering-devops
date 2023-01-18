#!/usr/bin/python3
"""
export data in the JSON format.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(url).json()
    data = {}
    for user in users:
        tasks = []
        for task in todos:
            if user.get("id") == task.get("userId"):
                tasks.append({"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": user.get("username")})
        data[user.get("id")] = tasks
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
