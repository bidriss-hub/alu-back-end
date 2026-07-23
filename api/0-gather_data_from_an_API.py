#!/usr/bin/env python3
"""
Script that, for a given employee ID, returns information about
his/her TODO list progress, using a REST API.
"""
import sys
import json
import urllib.request
import urllib.parse


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("employee_id must be an integer")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    with urllib.request.urlopen(
            "{}/users/{}".format(base_url, employee_id)) as response:
        user_data = json.loads(response.read().decode())

    if not user_data:
        print("Employee not found")
        sys.exit(1)

    employee_name = user_data.get("name")

    query = urllib.parse.urlencode({"userId": employee_id})
    with urllib.request.urlopen(
            "{}/todos?{}".format(base_url, query)) as response:
        todos_data = json.loads(response.read().decode())

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
