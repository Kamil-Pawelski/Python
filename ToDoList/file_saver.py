TASKS_FILE = "tasks.txt"


def load_tasks():
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")
