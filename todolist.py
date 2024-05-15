import os

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Your tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, new_task):
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully.")

    def update_task(self, index, updated_task):
        try:
            self.tasks[index - 1] = updated_task
            self.save_tasks()
            print("Task updated successfully.")
        except IndexError:
            print("Invalid task index.")

    def delete_task(self, index):
        try:
            del self.tasks[index - 1]
            self.save_tasks()
            print("Task deleted successfully.")
        except IndexError:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.show_tasks()
        elif choice == "2":
            new_task = input("Enter the task to add: ")
            todo_list.add_task(new_task)
        elif choice == "3":
            index = int(input("Enter the task number to update: "))
            updated_task = input("Enter the updated task: ")
            todo_list.update_task(index, updated_task)
        elif choice == "4":
            index = int(input("Enter the task number to delete: "))
            todo_list.delete_task(index)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
