import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo Application")

        self.tasks = []
        self.load_tasks_from_file()  # Load tasks from the file

        self.task_label = tk.Label(root, text="Enter Task:")
        self.task_label.pack()

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack()

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=40, selectmode=tk.SINGLE)
        self.task_listbox.pack()

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.populate_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.save_tasks_to_file()  # Save tasks to the file
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_index] = new_task
                self.save_tasks_to_file()  # Save tasks to the file
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, new_task)
                self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            del self.tasks[selected_index]
            self.save_tasks_to_file()  # Save tasks to the file
            self.task_listbox.delete(selected_index)

    def populate_listbox(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks_from_file(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            # If the file is not found, create it (it will be empty for now)
            with open("tasks.txt", "w"):
                pass

    def save_tasks_to_file(self):
        with open("tasks.txt", "w") as file:
            file.write("\n".join(self.tasks))


if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
