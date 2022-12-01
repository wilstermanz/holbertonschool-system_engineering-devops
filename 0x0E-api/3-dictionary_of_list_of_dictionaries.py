#!/usr/bin/python3
"""
This script uses an api to return a TODO list using
a given employee ID
"""
import json
import requests


if __name__ == "__main__":
    all_employees = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    employee_ids = []
    json_lib = {}

    for employee in all_employees:
        employee_ids.append(employee['id'])

    for employee_id in employee_ids:
        employee_info = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}"
            .format(employee_id)).json()
        for k, v in employee_info.items():
            if k == "name":
                employee_name = v
            if k == "username":
                employee_username = v

        todo_list = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos"
            .format(employee_id)).json()
        tasks_complete = []
        json_lib[employee_id] = []
        task_list = json_lib[employee_id]
        for task in todo_list:
            for k, v in task.items():
                if k == "completed" and v is True:
                    tasks_complete.append(task["title"])
            task_list.append(
                {"task": task["title"],
                 "completed": task["completed"],
                 "username": employee_username})

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(json_lib, json_file)
