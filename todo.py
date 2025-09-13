"""
Console-based To-Do List Manager
"""

import os
from typing import List

TODO_FILE: str = "todo.txt"


def load_tasks() -> List[str]:
    """
    Load tasks from the file if it exists.
    """
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    return []


def save_tasks(tasks: List[str]) -> None:
    """
    Save the current list of tasks to the file.
    """
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(f"{task}\n")


def add_task(tasks: List[str]) -> None:
    """
    Prompt the user to add a new task.
    """
    task = input("Enter the task to add: ").strip()
    if not task:
        print(" Task cannot be empty")
        return

    tasks.append(task)
    save_tasks(tasks)
    print(f" Task '{task}' added successfully")


def remove_task(tasks: List[str]) -> None:
    """
    Remove a task by its index.
    """
    if not tasks:
        print(" No tasks to remove")
        return

    view_tasks(tasks)

    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f" Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print(" Please enter a valid number!")


def view_tasks(tasks: List[str]) -> None:
    """
    Display all current tasks.
    """
    if not tasks:
        print(" No tasks in the list!")
    else:
        print("\n Current To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()


def main() -> None:
    """
    Main program loop for the To-Do List Manager.
    """
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List Manager ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":

    main()
