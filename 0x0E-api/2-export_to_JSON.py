#!/usr/bin/python3
"""
This script uses an api to return a TODO list using
a given employee ID
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    employee_info = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(argv[1])).json()
    for k, v in employee_info.items():
        if k == "name":
            employee_name = v
        if k == "username":
            employee_username = v

    todo_list = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(argv[1])).json()
    tasks_complete = []
    json_lib = {argv[1]: []}
    task_list = json_lib[argv[1]]
    for task in todo_list:
        for k, v in task.items():
            if k == "completed" and v is True:
                tasks_complete.append(task["title"])
        task_list.append(
            {"task": task["title"],
             "completed": task["completed"],
             "username": employee_username})

    with open(argv[1]+".json", 'w') as json_file:
        json.dump(json_lib, json_file)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(tasks_complete), len(todo_list)))
    for task in tasks_complete:
        print("\t {}".format(task))
