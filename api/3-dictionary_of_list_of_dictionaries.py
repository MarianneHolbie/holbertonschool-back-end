#!/usr/bin/python3
"""
    Script to export all tasks from all employees in the JSON format
    Format must be: { "USER_ID": [ {"username": "USERNAME", "task":
        "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username":
        "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
         ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
         "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
           "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: todo_all_employees.json
"""


import json
import requests

if __name__ == "__main__":

    # get information
    response = requests.get("https://jsonplaceholder.typicode.com/users/")
    # transform string in json
    fieldsUser = response.json()

    # create list of tupple (user_id, username)
    USER = []
    for user in fieldsUser:
        USER.append((user.get('id'), user.get('username')))

    # get TODO of all user
    responseTodo = requests.get("https://jsonplaceholder.typicode.com/todos")
    # transform string in json
    fieldsTodo = responseTodo.json()
    # list of list to all task todo for USER_ID
    values = []
    for task in fieldsTodo:
        values.append((task.get('userId'), task.get(
            'title'), task.get('completed')))

    dict_user = dict()

    # for each USER
    for user in USER:
        user_v = []
        # screen value, and construct dict of task
        for k in values:
            if k[0] == user[0]:
                # dict to each task todo for USER_ID
                user_v.append({"username": user[1], "task": k[1], "completed":
                              k[2]})
        dict_user[str(user[0])] = user_v

    with open("todo_all_employees.json", mode='w') as f:
        json.dump(dict_user, f)
