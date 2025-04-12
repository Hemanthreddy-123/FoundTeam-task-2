import datetime

class Task:
    def __init__(self, title, description, due_date, priority, tags=None, recurring_interval=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.tags = tags if tags else []
        self.recurring_interval = recurring_interval  # daily, weekly, etc.

    def __str__(self):
        tags_str = ', '.join(self.tags)
        return f"{self.title} - {self.description} - Due: {self.due_date} - Priority: {self.priority} - Tags: {tags_str} - Recurs: {self.recurring_interval if self.recurring_interval else 'No'}"

task_list = []

def add_task(title, description, due_date, priority, tags=None, recurring_interval=None):
    new_task = Task(title, description, due_date, priority, tags, recurring_interval)
    task_list.append(new_task)

def view_tasks():
    if not task_list:
        print("No tasks available.\n")
    for i, task in enumerate(task_list, start=1):
        print(f"{i}. {task}")
    print()

def update_task(index, title=None, description=None, due_date=None, priority=None, tags=None, recurring_interval=None):
    if 0 <= index < len(task_list):
        task = task_list[index]
        if title: task.title = title
        if description: task.description = description
        if due_date: task.due_date = due_date
        if priority: task.priority = priority
        if tags is not None: task.tags = tags
        if recurring_interval: task.recurring_interval = recurring_interval
        print("Task updated successfully.\n")
    else:
        print("Invalid task number.\n")

def delete_task(index):
    if 0 <= index < len(task_list):
        task_list.pop(index)
        print("Task deleted successfully.\n")
    else:
        print("Invalid task number.\n")

def search_tasks(keyword):
    results = [task for task in task_list if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
    if results:
        for i, task in enumerate(results, start=1):
            print(f"{i}. {task}")
    else:
        print("No matching tasks found.\n")

def sort_tasks(by='due_date'):
    if by == 'priority':
        task_list.sort(key=lambda task: task.priority)
    elif by == 'due_date':
        task_list.sort(key=lambda task: datetime.datetime.strptime(task.due_date, "%Y-%m-%d"))
    print(f"Tasks sorted by {by}.\n")

def menu():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search Tasks")
        print("6. Sort Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (YYYY-MM-DD): ")
            priority = input("Priority (High/Medium/Low): ")
            tags = input("Tags (comma-separated): ").split(",") if input("Add tags? (y/n): ").lower() == 'y' else []
            recurring = input("Recurring (daily/weekly/monthly) or leave blank: ")
            add_task(title, description, due_date, priority, tags, recurring)

        elif choice == '2':
            view_tasks()

        elif choice == '3':
            view_tasks()
            index = int(input("Enter task number to update: ")) - 1
            title = input("New Title (leave blank to keep): ")
            description = input("New Description (leave blank to keep): ")
            due_date = input("New Due Date (leave blank to keep): ")
            priority = input("New Priority (leave blank to keep): ")
            tags = input("New Tags (comma-separated, leave blank to keep): ")
            recurring = input("New Recurring (leave blank to keep): ")
            update_task(
                index,
                title if title else None,
                description if description else None,
                due_date if due_date else None,
                priority if priority else None,
                tags.split(",") if tags else None,
                recurring if recurring else None
            )

        elif choice == '4':
            view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)

        elif choice == '5':
            keyword = input("Enter keyword to search: ")
            search_tasks(keyword)

        elif choice == '6':
            sort_by = input("Sort by 'priority' or 'due_date': ")
            sort_tasks(sort_by)

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
