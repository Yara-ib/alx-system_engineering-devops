#!/usr/bin/python3
""" Script to export data in the CSV format. """


if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    # Getting the employee data
    url_employee_id = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    employee = requests.get(url_employee_id)
    username = employee.json().get('username')

    # Getting the entire todo list
    url_tasks = f'https://jsonplaceholder.typicode.com/todos/'
    json_tasks = requests.get(url_tasks).json()

    # Preparing the CSV file
    with open(f'{argv[1]}.csv', 'w', newline='') as file:
        write_file = csv.writer(file, quoting=csv.QUOTE_ALL)

    # Inserting data into the fields in CSV file
        if requests.get(url_employee_id):
            for task in json_tasks:
                if task.get('userId') == int(argv[1]):
                    task_completed_status = task.get('completed')
                    task_title = task.get('title')
                    write_file.writerow([
                        argv[1], username,
                        task_completed_status, task_title
                        ])
