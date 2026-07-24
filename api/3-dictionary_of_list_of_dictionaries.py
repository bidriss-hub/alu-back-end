#!/usr/bin/python3
"""Gathers data from a REST API for a given employee's TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    ).json()

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(todos)))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
