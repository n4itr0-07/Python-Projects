# Task Management App

Welcome to the Task Management App! This guide will walk you through creating and using the task management app from start to finish.

## Step 1: Initialize the App

Create a function named `task` to initialize the app and set up an empty list to store tasks.

```python
def task():
    tasks = []  # Empty list
    print("---------WELCOME TO THE TASK MANAGEMENT APP------------")
```

## Step 2: Add Initial Tasks

Prompt the user to input the number of tasks they want to add initially. Loop through the input to collect task names and append them to the `tasks` list.

```python
    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are \n{tasks}")
```

## Step 3: Create the Main Menu

Create a loop to continuously prompt the user for operations to manage tasks. The operations include adding, updating, deleting, viewing tasks, and exiting the app.

```python
    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
```

## Step 4: Add a Task

Allow the user to add a new task to the `tasks` list.

```python
        if operation == 1:
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' added successfully. Now tasks are \n{tasks}")
```

## Step 5: Update a Task

Enable the user to update an existing task by entering the task to be updated and the new task value.

```python
        elif operation == 2:
            updated_val = input("Enter task you want to update = ")
            if updated_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task '{updated_val}' successfully updated to '{up}'. Now tasks are \n{tasks}")
            else:
                print(f"Task '{updated_val}' not found.")
```

## Step 6: Delete a Task

Provide functionality to delete a task by entering the task to be deleted.

```python
        elif operation == 3:
            deleted_val = input("Enter task you want to delete = ")
            if deleted_val in tasks:
                ind = tasks.index(deleted_val)
                del tasks[ind]
                print(f"Task '{deleted_val}' successfully deleted. Now tasks are \n{tasks}")
            else:
                print(f"Task '{deleted_val}' not found.")
```

## Step 7: View Tasks

Allow the user to view the current list of tasks.

```python
        elif operation == 4:
            print(f"Today's tasks are \n{tasks}")
```

## Step 8: Exit the App

Provide an option to exit the app.

```python
        elif operation == 5:
            print("Thank you for using the task management app.... Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")
```

## Step 9: Start the App

Call the `task` function to start the app.

```python
# Call the task function to start the app
task()
```

## Follow Me

If you found this guide helpful, follow me for more tutorials and projects on GitHub and other social media platforms!

- [GitHub](https://github.com/Salik-Seraj)
- [X](https://twitter.com/code_with_ssn)
- [LinkedIn](https://linkedin.com/in/salik-seraj-naik)
- [Personal Website](https://linktr.ee/SalikSerajNaik)
