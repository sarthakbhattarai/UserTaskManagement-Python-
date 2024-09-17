import csv
import os
import hashlib

class UserManager:
    def __init__(self):
        self.users_file = "users.csv"
        self.users = self.load_users()

    def load_users(self):
        users = {}
        if os.path.exists(self.users_file):
            with open(self.users_file, mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    username, password_hash = row
                    users[username] = password_hash
        return users

    def save_users(self):
        with open(self.users_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            for username, password_hash in self.users.items():
                writer.writerow([username, password_hash])

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        # Check if the username already exists
        if username in self.users:
            print(f"Username '{username}' already exists. Please choose a different username.")
            return False
        # Proceed with registration
        password_hash = self.hash_password(password)
        self.users[username] = password_hash
        self.save_users()
        # Create a new task file for the user
        with open(f"{username}_tasks.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task Name", "Description", "Due Date", "Priority"])
        print(f"User '{username}' registered successfully.")
        return True

    def authenticate_user(self, username, password):
        if username not in self.users:
            return False
        return self.users[username] == self.hash_password(password)
