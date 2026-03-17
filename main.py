tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

def main():
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")
def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted!")
    except:
        print("Invalid input.")
main()