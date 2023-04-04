#!/usr/bin/python3
"""
    Script for a given employee ID,
    returns information TODO list progress
"""


import json
import requests
import sys

if __name__ == "__main__":

    # define variable
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    # collect employee ID
    Emp_id = int(sys.argv[1])

    # construct url with https:.../users/Emp_id
    url_requestUser = f"https://jsonplaceholder.typicode.com/users/{Emp_id}"

    # get information
    response = requests.get(url_requestUser)
    # transform string in json dict
    fieldsUser = json.loads(response.content)

    # collect name employee in this dict
    EMPLOYEE_NAME = fieldsUser.get('name')

    # get TODO of all user
    responseTodo = requests.get("https://jsonplaceholder.typicode.com/todos")
    # transform string in json dict
    fieldsTodo = json.loads(responseTodo.content)

    for k in fieldsTodo:
        # filter by employee ID
        if k.get('userId') == Emp_id:
            # filter only task complete / increment count
            if k.get('completed') is True:
                TASK_TITLE.append(k['title'])
                NUMBER_OF_DONE_TASKS += 1
            TOTAL_NUMBER_OF_TASKS += 1

    # construct answer
    # first line
    print(f"Employee {EMPLOYEE_NAME} is done with"
          f"tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    # second to n line
    for task in TASK_TITLE:
        print(f"\t {task}")
