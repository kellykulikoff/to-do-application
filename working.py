def display_menu():
    """Display the main menu options to the user."""
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task(tasks):
    """Add a new task to the task list."""
    task = input("Enter the task description: ").strip()
    if task:
        tasks.append(task)
        print(f'Task "{task}" added.')
    else:
        print("Error: Task description cannot be empty.")

def view_tasks(tasks):
    """View all tasks in the task list."""
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nCurrent Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(tasks):
    """Delete a task from the task list."""
    if not tasks:
        print("No tasks to delete.")
        return
    user_input = input("Enter the task number or description to delete: ").strip()
    found = False
    try:
        task_num = int(user_input)
    except ValueError:
        # Try to match by description (case-insensitive)
        lower_input = user_input.lower()
        for i, task in enumerate(tasks):
            if task.lower() == lower_input:
                removed_task = tasks.pop(i)
                print(f'Task "{removed_task}" deleted.')
                found = True
                break  # Delete only the first matching task
        if not found:
            print("Error: Task not found.")
    else:
        # Input was a valid integer, check if in range
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" deleted.')
            found = True
        else:
            print("Error: Task number does not exist.")
    finally:
        if found:
            print("Delete operation completed successfully.")
        else:
            print("Delete operation completed.")

def main():
    """Main function to run the task manager application."""
    tasks = []
    while True:
        display_menu()
        try:
            choice = int(input("Select an option (1-4): "))
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            continue
        else:
            if choice == 1:
                add_task(tasks)
                view_tasks(tasks)  # Show updated list after adding
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                delete_task(tasks)
                view_tasks(tasks)  # Show updated list after deleting
            elif choice == 4:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Error: Invalid selection. Please choose between 1 and 4.")
        finally:
            pass  # Can be used for cleanup if needed in the future

if __name__ == "__main__":
    main()