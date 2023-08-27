import tkinter as tk
from tkinter import messagebox


class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To do list by Nikhil Tiwari")

        self.tasks = []

        self.task_list = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_list.pack(pady=15, padx=15)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10, padx=15)

        self.add_button = tk.Button(
            root, text="Add Task", command=self.add_task)
        self.remove_button = tk.Button(
            root, text="Remove Task", command=self.remove_task)
        self.clear_button = tk.Button(
            root, text="Clear All", command=self.clear_tasks)

        self.add_button.pack(pady=7)
        self.remove_button.pack(pady=7)
        self.clear_button.pack(pady=7)

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def remove_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning(
                "Warning", "Please select a task to remove!")

    def clear_tasks(self):
        self.tasks = []
        self.update_task_list()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
