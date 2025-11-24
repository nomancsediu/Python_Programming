task = [] #Empty List

def menu():
    print("---To Do List---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Tasks")
    print("4. View Completed")
    print("5. Remove Task")
    print("6. Clear All")
    print("7. Exit")

while True:
    menu()

    choice = input("Enter your choice: ") #[String]

    if choice == '1':
        task_name = input("Enter the task: ")
        priority = input("Enter your priority: ")
        category = input("Enter the category: ")

        task.append([task_name,priority,category])
    print("Task added successfully!")





