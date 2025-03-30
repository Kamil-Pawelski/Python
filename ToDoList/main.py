tasks = []


def show_tasks():
    if not tasks:
        print("Your tasks list is empty.")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print(f"Task {task} was added succesfully.")


def remove_task():
    show_tasks()
    if not tasks:
        return

    try:
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' was removed successfully.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")


def main():
    while True:
        print("\n1. Show tasks list\n2. Add task\n3. Remove task\n4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Wrong option! Try again.")


if __name__ == "__main__":
    main()
