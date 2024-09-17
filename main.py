from UserManager import UserManager
from TaskManager import TaskManager
from datetime import datetime

def main():
    user_manager = UserManager()

    while True:
        print("\nTask Management System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            user_manager.register_user(username, password)

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if user_manager.authenticate_user(username, password):
                print(f"Welcome {username}!")
                task_manager = TaskManager(username)
                while True:
                    print("\nTask Manager")
                    print("1. Add Task")
                    print("2. View Tasks")
                    print("3. Delete Task")
                    print("4. Logout")
                    task_choice = input("Enter your choice: ")

                    if task_choice == "1":
                        task_name = input("Enter task name: ")
                        description = input("Enter task description: ")
                        due_date = input("Enter task due date (YYYY-MM-DD): ")
                        priority = input("Enter task priority (Low, Medium, High): ")
                        try:
                            datetime.strptime(due_date, "%Y-%m-%d")
                            task_manager.add_task(task_name, description, due_date, priority)
                        except ValueError:
                            print("Invalid date format. Please use YYYY-MM-DD.")

                    elif task_choice == "2":
                        task_manager.view_tasks()

                    elif task_choice == "3":
                        task_name = input("Enter task name to delete: ")
                        task_manager.delete_task(task_name)

                    elif task_choice == "4":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice, please try again.")

            else:
                print("Invalid username or password.")

        elif choice == "3":
            print("Exiting Task Management System.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
