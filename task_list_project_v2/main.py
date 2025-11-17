"""
Task Manager Application
A simple task management system using SQLite database.
Allows users to create, read, update, and delete tasks with status tracking.
"""
from user_interface import User_Interface

if __name__ == "__main__":
    """
    Main Entry Point
    Initializes and launches the Task Manager Application.
    """
    manager = User_Interface()
    manager.run()