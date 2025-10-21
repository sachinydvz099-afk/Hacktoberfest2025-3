import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        lines = f.readlines()
    tasks = []
    for line in lines:
        status, text = line.strip().split(":::", 1)
        tasks.append({"task": text, "done": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            line = "done" if task["done"] else "todo"
            f.write(f"{line}:::{task['task']}\n")

def add_task(tasks, task_desc):
    tasks.append({"task": task_desc, "done": False})
    save_tasks(tasks)

def list_tasks(tasks):
    print("\nYour To-Do List:")
    for i, t in enumerate(tasks, 1):
        status = "✔️" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")
    print()

def mark_complete(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed!\n")
    else:
        print("Invalid task number.\n")
        
def delete_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['task']}\n")
    else:
        print("Invalid task number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("Choose an option:")
        print("1. Add new task")
        print("2. List all tasks")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            desc = input("Task description: ")
            add_task(tasks, desc)
            print("Task added.\n")
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks)
            idx = int(input("Enter task number to complete: "))
            mark_complete(tasks, idx)
        elif choice == "4":
            list_tasks(tasks)
            idx = int(input("Enter task number to delete: "))
            delete_task(tasks, idx)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.\n")

if __name__ == "__main__":
    main()
