#!/usr/bin/python3
"""
    Script script to export data in the CSV format
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""


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

    dict_user = {}
    # list of dict to all task todo for USER_ID
    values = []
    for k in fieldsTodo:
        # filter by employee ID
        if k.get('userId') == USER_ID:
            TASK_COMPLETED_STATUS = k['completed']
            TASK_TITLE = k['title']
            # dict to each task todo for USER_ID
            value_dict = {"task": TASK_TITLE, "completed":
                          TASK_COMPLETED_STATUS, "username": USERNAME}
            values.append(value_dict)
    dict_user = {USER_ID: values}
    json_object = json.dumps(dict_user)

    with open(f"{USER_ID}.json", mode='w') as f:
        f.write(json_object)
