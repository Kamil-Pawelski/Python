from file_saver import load_tasks, save_tasks

tasks = load_tasks()


def show_tasks():
    if not tasks:
        print("Your tasks list is empty.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' was added successfully.")


def remove_task():
    show_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"Task '{removed_task}' was removed successfully.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")