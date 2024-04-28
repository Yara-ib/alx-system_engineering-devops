#!/usr/bin/python3
""" Script to display the employee TODO list progress """


if __name__ == '__main__':
    import requests
    from sys import argv

    # Getting the employee data
    url_employee_id = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    employee = requests.get(url_employee_id)
    json_employee = employee.json()
    employee_name = json_employee.get('name')

    # Getting the entire todo list
    url_tasks = f'https://jsonplaceholder.typicode.com/todos/'
    todo_list = requests.get(url_tasks)
    json_tasks = todo_list.json()

    # Getting the todo list for that employee
    tasks_completed, total_tasks = 0, 0
    all_tasks_4_employee = []
    for task in json_tasks:
        if task.get('userId') == int(argv[1]):
            total_tasks += 1
            if task.get('completed'):
                tasks_completed += 1
                all_tasks_4_employee.append(task.get('title'))

    if requests.get(url_employee_id):
        count = f'{tasks_completed}/{total_tasks}'
        print(f'Employee {employee_name} is done with tasks({count}):')
        for item in all_tasks_4_employee:
            print(f'\t {item}')
