class ToDoList:
    tasks = []

    def add_task(self, task_description):
        #to add a new task.
        ToDoList.tasks.append({"description": task_description, "completed": False})
        print("Task added.")

    def view_tasks(self):
        #to display all tasks with their status
        if not ToDoList.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(ToDoList.tasks, 1):
                status = "Done" if task["completed"] else "Not Done"
                print("{0} . {1} - {2}".format(idx, task['description'], status))

    def update_task(self, task_number, new_description):
        #to update the description of a specific task.
        if 0 < task_number <= len(ToDoList.tasks):
            ToDoList.tasks[task_number - 1]["description"] = new_description
            print("Task updated.")
        else:
            print("Invalid task number. Please try again.")

    def delete_task(self, task_number):
        #to  remove a task from the list.
        if 0 < task_number <= len(ToDoList.tasks):
            ToDoList.tasks.pop(task_number - 1)
            print("Task deleted.")
        else:
            print("Invalid task number. Please try again.")

    def mark_task_completed(self, task_number):
        #to mark a task as completed
        if 0 < task_number <= len(ToDoList.tasks):
            ToDoList.tasks[task_number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number. Please try again.")

def display_menu():
    #to display the menu options for the to-do list
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Mark a task as completed")
    print("6. Exit")

def main():
    to_do_list = ToDoList()

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            task = input("Enter the task description: ")
            to_do_list.add_task(task)
            print("Task added.")
        elif choice == "2":
            to_do_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to update: "))
            new_task = input("Enter new task description: ")
            to_do_list.update_task(task_number, new_task)
            print("Task updated.")
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            to_do_list.delete_task(task_number)
            print("Task deleted.")
        elif choice == "5":
            task_number = int(input("Enter task number to mark as completed: "))
            to_do_list.mark_task_completed(task_number)
            print("Task marked as completed.")
        elif choice == "6":
            print("Exiting the to do list.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.:")
main()
