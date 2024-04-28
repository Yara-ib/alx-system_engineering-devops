#!/usr/bin/python3
""" Script to export data in the JSON format. """


if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    # Getting the employee data
    url_employee_id = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    employee = requests.get(url_employee_id)
    username = employee.json().get('username')

    # Getting the entire todo list
    url_tasks = f'https://jsonplaceholder.typicode.com/todos/'
    json_tasks = requests.get(url_tasks).json()

    # Preparing the JSON file
    with open(f'{argv[1]}.json', 'w') as file:
        data_dict = {}
        list_tasks_titles = []

    # Preparing data to be written to the JSON file
        if requests.get(url_employee_id):
            for task in json_tasks:
                if task.get('userId') == int(argv[1]):
                    task_completed_status = task.get('completed')
                    task_title = task.get('title')
                    list_tasks_titles.append({
                        "task": task_title,
                        "completed": task_completed_status,
                        "username": username
                        })
            data_dict[argv[1]] = list_tasks_titles

        json.dump(data_dict, file)
