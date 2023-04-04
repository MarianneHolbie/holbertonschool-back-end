#!/usr/bin/python3
"""
    Script for a given employee ID,
    returns information TODO list progress
"""


import csv
import json
import requests
import sys

if __name__ == "__main__":

    # collect employee ID
    USER_ID = int(sys.argv[1])

    # construct url with https:.../users/Emp_id
    url_requestUser = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"

    # get information
    response = requests.get(url_requestUser)
    # transform string in json dict
    fieldsUser = json.loads(response.content)

    # collect name employee in this dict
    USERNAME = fieldsUser.get('username')

    # get TODO of all user
    responseTodo = requests.get("https://jsonplaceholder.typicode.com/todos")
    # transform string in json dict
    fieldsTodo = json.loads(responseTodo.content)

    with open(f"{USER_ID}.csv", mode='w') as f:
        task = csv.writer(f, delimiter=',', quotechar='"',
                          quoting=csv.QUOTE_ALL)
        for k in fieldsTodo:
            # filter by employee ID
            if k.get('userId') == USER_ID:
                TASK_COMPLETED_STATUS = k['completed']
                TASK_TITLE = k['title']
                task.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS,
                               TASK_TITLE])
