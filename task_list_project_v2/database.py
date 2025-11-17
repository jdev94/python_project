"""
Database Module
Handles all SQLite database operations including task creation, updating, deletion, and retrieval.
"""

import sqlite3 as sq

class Database:

    """
    Database class for managing SQLite database operations.
    Handles connection, task creation, updating, deletion, and retrieval.
    """

    CREATE_TABLE_SQL_TASKS = """CREATE TABLE IF NOT EXISTS Tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Task VARCHAR(50) UNIQUE,
                            Status VARCHAR(20)
                            )"""
    
    ADD_TASK_SQL = '''INSERT INTO Tasks
                            (Task, Status)
                            VALUES(?, ?)'''
        
    def __init__(self, db_name= "task_list.db"):

        """
        Initialize the Database object and create the table if it doesn't exist.
        
        Args:
            db_name (str): Name of the SQLite database file. Defaults to "task_list.db"
        """
         
        self.db_name = db_name
        self.create_table()
    
    def _get_db_tools(self):

        """
        Create and return a database connection and cursor.
        
        Returns:
            tuple: (connection, cursor) for database operations
        """

        connect = sq.connect(self.db_name)
        cursor = connect.cursor()
        return connect, cursor

    def create_table(self):

        """
        Create the Tasks table if it doesn't already exist.
        Handles any errors that occur during table creation.
        """

        connect, cursor = self._get_db_tools()
        try:
            cursor.execute(self.CREATE_TABLE_SQL_TASKS)
            connect.commit()
            print("Tasks table created or already exists!")
        except Exception as e:
            print(f"An error occurred while creating the table: {e}")
        finally:
            cursor.close()
            connect.close()
    
    def add_task(self, Task, Status):

        """
        Add a new task to the database.
        
        Args:
            Task (str): Name of the task
            Status (str): Status of the task ("Finished" or "Unfinished")
        
        Raises:
            IntegrityError: If a task with the same name already exists
        """

        connect, cursor = self._get_db_tools()
        try:
            cursor.execute(self.ADD_TASK_SQL, (
                Task, Status
            ))
            connect.commit()
            print("Task added successfully!")
        except sq.IntegrityError:
            print(f"Error: A task named '{Task}' already exists!")
        except Exception as e:
            print(f"An error occurred while adding the task: {e}")
        finally:
            cursor.close()
            connect.close()
    
    def update_task(self, task_id, status):

        """
        Update the status of an existing task.
        
        Args:
            task_id (int): ID of the task to update
            status (str): New status for the task ("Finished" or "Unfinished")
        """

        connect, cursor = self._get_db_tools()
        try:
            cursor.execute("""UPDATE Tasks SET Status = ? WHERE id = ?""", (status, task_id,))
            connect.commit()
            print("Task updated successfully!")
        except Exception as e:
            print(f"An error occurred while updating the task: {e}")
        finally:
            cursor.close()
            connect.close()
    
    def delete_task(self, task_id):

        """
        Delete a task from the database by its ID.
        
        Args:
            task_id (int): ID of the task to delete
        """

        connect, cursor = self._get_db_tools()
        try:
            cursor.execute("""DELETE FROM Tasks
                           WHERE id =?""", (task_id,))
            connect.commit()
            if cursor.rowcount == 0:
                print(f"No task found.")
            else:
                print("Task deleted successfully!")
        except Exception as e:
            print(f"An error occurred while deleting the task: {e}")
        finally:
            cursor.close()
            connect.close()
    

    def get_all_tasks(self):

        """
        Retrieve all tasks from the database.
        
        Returns:
            list: List of tuples containing (id, Task, Status) for each task
        """

        connect, cursor = self._get_db_tools()
        try:
            cursor.execute("""SELECT id, Task, Status FROM Tasks""")
            tasks = cursor.fetchall()
            return tasks
        except Exception as e:
            print(f"An error occurred while retrieving tasks: {e}")
            return []
        finally:
            cursor.close()
            connect.close()
    
    def unfinished_task(self):

        """
        Retrieve all unfinished tasks from the database.
        
        Returns:
            list: List of tuples containing (id, Task, Status) for unfinished tasks
        """

        connect, cursor = self._get_db_tools()
        try:
            cursor.execute("""SELECT id, Task, Status FROM Tasks WHERE Status = 'Unfinished'""")
            tasks = cursor.fetchall()
            return tasks
        except Exception as e:
            print(f"An error occurred while retrieving tasks: {e}")
            return []
        finally:
            cursor.close()
            connect.close()
