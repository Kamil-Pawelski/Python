from task import show_tasks, add_task, remove_task

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