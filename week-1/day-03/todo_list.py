task_list = []

while True:
    print("""
    ======= MENU LIST =======
    1. Add New Task
    2. View All Tasks
    3. Delete Task
    4. Exit The Program
    """)
    choice = int(input("Choice: "))

    if choice == 1:
        task = input("Enter Task: ")
        task_list.append(task)        
        print("Task Added")
    elif choice == 2:
        if len(task_list) == 0:
            task = input("No tasks")
            continue
        print("All Tasks:")
        for i in range(len(task_list)):
            print(f"{i + 1}. {task_list[i]}")

    elif choice == 3:
        task = input("Enter Task Name: ")
        if task in task_list:
            task_list.remove(task)
        else: 
            print("Invalid Task Name!")
    elif choice == 4:
        print("Exiting the program")
        break
    else:
        print("Invalid Choice")
