"""
Tasks Module
Provides the Tasks class that acts as an intermediary between the database and the user interface.
Manages task operations at the business logic level.
"""

from database import Database

class Tasks():
    """
    Tasks class for managing task operations.
    Acts as a bridge between the database layer and the user interface.
    Provides high-level methods for adding, updating, deleting, and retrieving tasks.
    """

    def __init__(self):
        """
        Initialize the Tasks object and create a Database instance.
        """
        self.db = Database()

    def add(self, task_name):
        """
        Add a new task to the database with "Unfinished" status.

        Args:
            task_name (str): Name of the task to add.
        """
        self.db.add_task(task_name, "Unfinished")

    def update(self, task_id, status):
        """
        Update the status of an existing task.

        Args:
            task_id (int): ID of the task to update.
            status (str): New status for the task ("Finished" or "Unfinished").
        """
        self.db.update_task(task_id, status)

    def delete(self, task_id):
        """
        Delete a task from the database by its ID.

        Args:
            task_id (int): ID of the task to delete.
        """
        self.db.delete_task(task_id)

    def get_all(self):
        """
        Retrieve all tasks from the database.

        Returns:
            list: List of tuples containing (id, Task, Status) for each task.
        """
        return self.db.get_all_tasks()

    def unfinished(self):
        """
        Retrieve all unfinished tasks from the database.

        Returns:
            list: List of tuples containing (id, Task, Status) for unfinished tasks.
        """
        return self.db.unfinished_task()
    
    def complete(self, task_id):
        """
        Mark a task as finished.

        Args:
            task_id (int): ID of the task to mark as finished.
        """
        self.update(task_id, "Finished")

    def incomplete(self, task_id):
        """
        Mark a task as unfinished.

        Args:
            task_id (int): ID of the task to mark as unfinished.
        """
        self.update(task_id, "Unfinished")