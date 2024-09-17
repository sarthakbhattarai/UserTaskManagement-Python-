import csv
import os

class TaskManager:
    def __init__(self, username):
        self.username = username
        self.task_file = f"{username}_tasks.csv"

    def add_task(self, task_name, description, due_date, priority):
        with open(self.task_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([task_name, description, due_date, priority])
        print(f"Task '{task_name}' added successfully.")

    def view_tasks(self):
        if not os.path.exists(self.task_file):
            print("No tasks found.")
            return
        with open(self.task_file, mode="r") as file:
            reader = csv.reader(file)
            tasks = list(reader)
            if len(tasks) <= 1:
                print("No tasks available.")
            else:
                for row in tasks:
                    print(", ".join(row))

    def delete_task(self, task_name):
        tasks = []
        with open(self.task_file, mode="r") as file:
            reader = csv.reader(file)
            tasks = list(reader)
        
        with open(self.task_file, mode="w", newline="") as file:
            writer = csv
