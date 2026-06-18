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

    # Modification 1
    if choice == 1:
        task = input("Enter Task: ")
        priority = int(input("Enter Priority: "))

        task_list.append((priority, task))
        task_list = sorted(task_list, key=lambda x: x[0])

        print("Task Added!")

    elif choice == 2:
        if len(task_list) == 0:
            task = input("No Tasks!")
            continue
        print("All Tasks:")
        for i in range(len(task_list)):
            print(f"{i + 1}. {task_list[i][1]}")

    # Modification 2
    elif choice == 3:
        task_index = int(input("Task Index: "))
        if task_index < len(task_list):
            task_list.pop(task_index)
        else:
            print("Invalid Index!")

    elif choice == 4:
        print("Exiting the program")
        break

    else:
        print("Invalid Choice")
