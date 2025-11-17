"""
User Interface Module
Handles all user interactions and command-line interface for the Task Manager application.
Displays menus, collects user input, and manages application flow.
"""

from tasks import Tasks

class User_Interface():
    """
    User_Interface class for managing the command-line interface.
    Handles all user interactions, menu display, and task management operations.
    """
    def __init__(self):
        """
        Initialize the User_Interface object and create a Tasks instance.
        """
        self.tk = Tasks()

    def interface(self):
        """
        Display the main menu with all available options.
        """
        print("\n" + "=" * 50 + "\n")
        print("Welcome to your Task Manager App.".center(50))
        print("""\n--------------------------
1 - Add a Task
2 - Delete a task
3 - Display all tasks
4 - Show unfinished tasks
5 - Change the status of your task
6 - Quit
--------------------------\n""")
        print("=" * 50)
    
    def run(self):
        """
        Run the main application loop.
        Continuously displays the menu and processes user choices until the user quits.
        """
        while True:
            self.interface()

            choice = input("\nChoose an option (1-6): ").strip()
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.delete_task()
            elif choice == "3":
                self.display_all()
            elif choice == "4":
                self.display_unfinished()
            elif choice == "5":
                self.change_status()
            elif choice == "6":
                print("Thank you for using Task Manager. Goodbye!")
                break
            else:
                print("Invalid option! Please choose 1-6.")
    
    def add_task(self):
        """
        Prompt the user to enter a task name and add it to the database.
        Validates that the task name is not empty before adding.
        """
        task_name = input("Enter task name: ").strip().title()
        if task_name:
            self.tk.add(task_name)
        else:
            print("Task name cannot be empty!")

    def delete_task(self):
        """
        Display all tasks and allow the user to delete a task by its ID.
        Requires user confirmation before deleting.
        """
        tasks = self.tk.get_all()
        if not tasks:
            print("No tasks found!")
            return
        
        print("\n↓↓↓↓ Select a task ↓↓↓↓")
        for id, name, status in tasks:
            print(f"{id}. {name} - {status}")

        try:
            task_id = int(input("\nEnter task ID to delete: ").strip())
        except ValueError:
            print("Please enter a valid number!")
            return
        
        task_name = None
        for id, name, status in tasks:
            if id == task_id:
                task_name = name
                break
        
        if task_name is None:
            print("Task ID not found!")
            return
        
        while True:
            confirm = input(f"Are you sure you want to delete '{task_name}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                self.tk.delete(task_id)
                print("Task deleted!")
                break
            elif confirm == "no":
                print("Deletion cancelled.")
                break
            else:
                print("Please answer 'yes' or 'no'!")


    def display_all(self):
        """
        Display all tasks from the database with their ID, name, and status.
        """
        tasks = self.tk.get_all()
        if tasks:
            print("\n↓↓↓↓ Task List ↓↓↓↓")
            for id, name, status in tasks:
                print(f"{id}. {name} - {status}")
        else:
            print("No tasks found!")
    
    def display_unfinished(self):
        """
        Display all unfinished tasks from the database with their ID, name, and status.
        """
        tasks = self.tk.unfinished()
        if tasks:
            print("\n↓↓↓↓ Unfinished Tasks ↓↓↓↓")
            for id, name, _ in tasks:
                print(f"{id}. {name} - Unfinished")
        else:
            print("No unfinished tasks!")
    
    def change_status(self):
        """
        Display all tasks and allow the user to change the status of a task.
        User selects a task by ID and chooses between "Finished" or "Unfinished" status.
        """
        tasks = self.tk.get_all()
        if not tasks:
            print("No tasks found!")
            return
        
        print("\n↓↓↓↓ Select a task ↓↓↓↓")
        for id, name, status in tasks:
            print(f"{id}. {name} - {status}")

        try:
            task_id = int(input("\nEnter task ID: ").strip())
        except ValueError:
            print("Please enter a valid number!")
            return
        if not any(id == task_id for id, _, _ in tasks):
            print("Task ID not found!")
            return
            
        print("1 - Mark as Finished")
        print("2 - Mark as Unfinished")
        status_choice = input("Choose (1 or 2): ").strip()

        if status_choice == "1":
            self.tk.complete(task_id)
            print(f"Task '{task_id}' marked as Finished!")
        elif status_choice == "2":
            self.tk.incomplete(task_id)
            print(f"Task '{task_id}' marked as Unfinished!")
        else:
            print("Invalid option!")
        
