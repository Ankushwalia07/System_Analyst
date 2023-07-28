'''A command-line tool that allows users to create and manage their task list with
additional features for priority and due dates. This tool can be useful for personal
task management or small team collaboration.'''

import json
import os

def load_tasks():
    if os.path.exists('task.json'):
        with open('tasks.json',"r") as file:
            return json.load(file)
    return[]

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    print("TASK LIST:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']} - Priority: {task['priority']} - Due Date: {task['due_date']}")
    print()

def add_task(tasks):
    title = input("Enter the task title: ")
    priority = input("Enter the priority (High/Medium/Low): ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")

    tasks.append({
        "title": title,
        "priority": priority,
        "due_date": due_date
    })

    print("Task added successfully!\n")

def delete_task(tasks):
    show_tasks(tasks)
    index_to_delete = int(input("Enter the task number to delete: ")) - 1

    if 0 <= index_to_delete < len(tasks):
        del tasks[index_to_delete]
        print("Task deleted successfully!\n")
    else:
        print("Invalid task number!\n")

def main():
    tasks = load_tasks()

    while True:
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Task list saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()