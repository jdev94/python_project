# Class that manages the logic of the to-do list (add, delete, complete, display tasks)

class Tasks():

    def __init__(self):
        # List of task names
        self.tasks = []
         # List of booleans: True if done, False if still to do
        self.done = []

    def add(self, task):
        """Add a new task (starts as not completed)."""
        self.tasks.append(task)
        self.done.append(False)

    def complete(self, idx):
        """Mark a task as completed (✔️) by its index if it exists."""
        if 0 <= idx < len(self.done):
            self.done[idx] = True
        else:
            print("This task doesn't exist.")

    def delete(self, idx):
        """Remove a task and its status from the lists, using the given index."""
        if 0 <= idx < len(self.tasks):
            del self.tasks[idx]
            del self.done[idx]
        else:
            print("This task doesn't exist.")

    def display(self):
        """Print the current list of tasks with their status: checkmark if done, cross if not."""
        print("\n--------------------------\n")
        print("\n--------------------------\n")
        for i, t in enumerate(self.tasks):
            status = "✔️" if self.done[i] else "❌"
            print(f"{i}. {t} : {status}")
        print("\n--------------------------\n")

# Class that handles the user interface (command-line menu loop)
class IU():

    def __init__(self, manager):
        # Store a Tasks instance to manage task operations
        self.tasks = manager

    def invit_command(self):
        """Main input loop - shows menu, receives and processes user choices."""
        while True:
            # Display menu and get user input (spaces & case are ignored)
            choice = input("\n| + : Add a task | - : Delete a task | c : Complète a task | d = Display your tasks | q : Quit | \n\nType your choice here : ").strip().lower()

            if choice == "+":
                # Add a task
                addtasks = input("Type the task : ")
                self.tasks.add(addtasks)

            elif choice == "-":
                # Delete a task by index, with input validation
                deltasks = input("Type the number's task you want to delete : ").strip()
                try:
                    idx = int(deltasks)
                    if 0 <= idx < len(self.tasks.tasks):
                        self.tasks.delete(idx)
                    else:
                        print("This task doesn't exist.")
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "c":
                # Complete a task by index, with input validation
                comptasks = input("Type the number of the task you want to complete : ").strip()
                try:
                    idx = int(comptasks)
                    if 0 <= idx < len(self.tasks.tasks):
                        self.tasks.complete(idx)
                    else:
                        print("This task doesn't exist.")
                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "d":
                # Show all tasks and their completion status
                self.tasks.display()

            elif choice == "q":
                # Exit the menu/program
                print("Hope to see you soon. :)")
                break

            else:
                # Handle invalid option
                print("Please enter a valid option.")
                

# Program startup: create the list manager and interface, then start the menu
manager = Tasks()
interface = IU(manager)
interface.invit_command()

