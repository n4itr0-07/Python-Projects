# def task():
#     tasks = [] #empty list
#     print("---------WELCOME TO THE TASK MANAGMENT APP------------")

#     total_task = int(input("Enter how many task you want to add = "))
#     for i in range(1, total_task+1): # 6
#         task_name = input("Enter task {i} = ")
#         tasks.append(task_name)

#     print(f"Today's task are \n{tasks}")
#     while True:
#         operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
#         if operation == 1:
#             add = input("Enter task you want to add = ")
#             tasks.append(add)
#             print(f"Task {add} successfully. Now tasks are \n{tasks}")

#         elif operation == 2:
#             updated_val = input("Enter task you want to update = ")
#             if updated_val in tasks:
#                 up = int(input("Enter new task = "))
#                 ind = tasks.index(updated_val) #2
#                 tasks[ind] = up
#                 print(f"Task {updated_val} successfully updated to {up}. Now tasks are \n{tasks}")


#         elif operation == 3:
#             deleted_val = input("Enter task you want to delete = ")
#             if deleted_val in tasks:
#                 ind = tasks.index(deleted_val)
#                 del tasks(ind)
#                 print(f"Task {deleted_val} successfully deleted. Now tasks are \n{tasks}")
#                 # else:
#                 #     print(f"{deleted_val} not found.")


#         elif operation == 4:
#             print(f"Today's task are \n{tasks}")

#         elif operation == 5:
#             print("Thank you for using the task management app.... Goodbye!")
#             break

#         else:
#             print("Invalid option. Please try again.")






#TODO: NEW CODE 

def task():
    tasks = []  # Empty list
    print("---------WELCOME TO THE TASK MANAGEMENT APP------------")

    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are \n{tasks}")
    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' added successfully. Now tasks are \n{tasks}")

        elif operation == 2:
            updated_val = input("Enter task you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task '{updated_val}' successfully updated to '{up}'. Now tasks are \n{tasks}")
            else:
                print(f"Task '{updated_val}' not found.")

        elif operation == 3:
            deleted_val = input("Enter task you want to delete = ")
            if deleted_val in tasks:
                ind = tasks.index(deleted_val)
                del tasks[ind]
                print(f"Task '{deleted_val}' successfully deleted. Now tasks are \n{tasks}")
            else:
                print(f"Task '{deleted_val}' not found.")

        elif operation == 4:
            print(f"Today's tasks are \n{tasks}")

        elif operation == 5:
            print("Thank you for using the task management app.... Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

# Call the task function to start the app
task()







