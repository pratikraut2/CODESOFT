import tkinter as tk 
from tkinter import messagebox
import json
import os

# This file stores tasks between runs
DATA_FILE = "my_tasks.json"

# Load old tasks from file (if any)
def get_saved_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save current tasks to file
def store_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)

# Main to-do app class
class MyToDoApp:
    def __init__(self, screen):
        self.screen = screen
        self.screen.title("My Task Tracker 📝")

        self.all_tasks = get_saved_tasks()

        # Input field for typing tasks
        self.task_input = tk.Entry(screen, width=50 , font=("Arial", 13))
        self.task_input.pack(pady=10)

        # Add task button
        tk.Button(screen, text="Add", command=self.add_new_task).pack()

        # Where tasks will be shown
        self.task_list_frame = tk.Frame(screen)
        self.task_list_frame.pack(pady=10)

        self.show_all_tasks()

    def add_new_task(self):
        typed = self.task_input.get().strip()
        if typed == "":
            messagebox.showwarning("Oops!", "Please write something before adding.")
            return
        self.all_tasks.append({"title": typed, "done": False})
        self.task_input.delete(0, tk.END)
        store_tasks(self.all_tasks)
        self.show_all_tasks()

    def toggle_done(self, index):
        self.all_tasks[index]["done"] = not self.all_tasks[index]["done"]
        store_tasks(self.all_tasks)
        self.show_all_tasks()

    def remove_task(self, index):
        del self.all_tasks[index]
        store_tasks(self.all_tasks)
        self.show_all_tasks()

    def show_all_tasks(self):
        # Clean the area first
        for item in self.task_list_frame.winfo_children():
            item.destroy()

        for i, task in enumerate(self.all_tasks):
            task_text = task["title"]
            is_done = task["done"]

            text_color = "green" if is_done else "black"

            label = tk.Label(self.task_list_frame, text=task_text, fg=text_color, font=("Arial", 12))
            label.grid(row=i, column=0, sticky="w", padx=5, pady=2)

            done_btn = tk.Button(self.task_list_frame, text="✔️" if not is_done else "↩️", command=lambda i=i: self.toggle_done(i))
            done_btn.grid(row=i, column=1)

            del_btn = tk.Button(self.task_list_frame, text="🗑️", command=lambda i=i: self.remove_task(i))
            del_btn.grid(row=i, column=2)

# Start the app
if __name__ == "__main__":
    root = tk.Tk()
    my_app = MyToDoApp(root)
    root.mainloop()
