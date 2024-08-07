#!/usr/bin/python3
"""Script to get todos for a user from API"""

import requests
import sys

def main():
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Error: Failed to retrieve todos")
        sys.exit(1)

    total_questions = 0
    completed = []
    for todo in response.json():
        if todo['userId'] == user_id:
            total_questions += 1
            if todo['completed']:
                completed.append(todo['title'])

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Failed to retrieve user information")
        sys.exit(1)

    user_name = user_response.json()['name']

    printer = ("Employee {} is done with tasks({}/{}):".format(user_name,
               len(completed), total_questions))
    print(printer)
    for q in completed:
        print("\t {}".format(q))


if __name__ == '__main__':
    main()
