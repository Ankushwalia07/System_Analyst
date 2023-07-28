'''A Python code example for this step by creating a command-line task
 management application with a focus on code organization, modularization,
 and error handling.

We will use Object-Oriented Programming (OOP) to design
the application, and the argparse module to handle command
-line arguments. The application will allow users to add, view, update, and complete
tasks.'''

import argparse
import json
import os
import uuid

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status
        self.task_id = str(uuid.uuid4())

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file)

    def add_task(self, title, description):
        new_task = Task(title, description, "Todo")
        self.tasks.append(new_task.__dict__)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(f"ID: {task['task_id']}, Title: {task['title']}, Description: {task['description']}, Status: {task['status']}")

    def update_task(self, task_id, title, description):
        for task in self.tasks:
            if task["task_id"] == task_id:
                task["title"] = title
                task["description"] = description
                print("Task updated successfully!")
                return
        print("Task not found!")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["task_id"] == task_id:
                task["status"] = "Completed"
                print("Task marked as completed!")
                return
        print("Task not found!")

def main():
    parser = argparse.ArgumentParser(description="Command-line Task Manager")
    parser.add_argument("filename", default="tasks.json", nargs="?", help="Specify the tasks data file (default: tasks.json)")
    args = parser.parse_args()

    task_manager = TaskManager(args.filename)

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the task title: ")
            description = input("Enter the task description: ")
            task_manager.add_task(title, description)

        elif choice == "2":
            task_manager.view_tasks()

        elif choice == "3":
            task_id = input("Enter the task ID to update: ")
            title = input("Enter the updated title: ")
            description = input("Enter the updated description: ")
            task_manager.update_task(task_id, title, description)

        elif choice == "4":
            task_id = input("Enter the task ID to mark as completed: ")
            task_manager.complete_task(task_id)

        elif choice == "5":
            task_manager.save_tasks()
            print("Tasks saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
