import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority, due_date):
        self.tasks.append({"task": task, "priority": priority, "due_date": due_date})
        print("Task added successfully!")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task removed successfully!")
        else:
            print("Invalid task index!")

    def display_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for index, task_info in enumerate(self.tasks):
                print(f"{index + 1}. {task_info['task']} (Priority: {task_info['priority']}, Due Date: {task_info['due_date']})")
        else:
            print("Your To-Do List is empty!")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task_info in self.tasks:
                file.write(f"{task_info['task']},{task_info['priority']},{task_info['due_date']}\n")
        print("Tasks saved to file successfully!")

class TodoListGUI:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.todo_list = TodoList()

        self.task_label = tk.Label(master, text="Task:")
        self.task_label.grid(row=0, column=0)

        self.task_entry = tk.Entry(master)
        self.task_entry.grid(row=0, column=1)

        self.priority_label = tk.Label(master, text="Priority:")
        self.priority_label.grid(row=1, column=0)

        self.priority_entry = tk.Entry(master)
        self.priority_entry.grid(row=1, column=1)

        self.due_date_label = tk.Label(master, text="Due Date:")
        self.due_date_label.grid(row=2, column=0)

        self.due_date_entry = tk.Entry(master)
        self.due_date_entry.grid(row=2, column=1)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.display_button = tk.Button(master, text="Display Tasks", command=self.display_tasks)
        self.display_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.save_button = tk.Button(master, text="Save to File", command=self.save_to_file)
        self.save_button.grid(row=6, column=0, columnspan=2, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        priority = self.priority_entry.get()
        due_date = self.due_date_entry.get()
        self.todo_list.add_task(task, priority, due_date)
        self.clear_entries()

    def remove_task(self):
        index = self.get_selected_index()
        if index is not None:
            self.todo_list.remove_task(index)
        else:
            messagebox.showinfo("Error", "Please select a task to remove.")

    def display_tasks(self):
        self.todo_list.display_tasks()

    def save_to_file(self):
        filename = "todo_list.txt"
        self.todo_list.save_to_file(filename)

    def clear_entries(self):
        self.task_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)

    def get_selected_index(self):
        try:
            index = int(self.listbox.curselection()[0])
            return index
        except IndexError:
            return None

def main():
    root = tk.Tk()
    app = TodoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
