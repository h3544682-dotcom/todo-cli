"""Tkinter GUI for the todo-cli task manager."""

import tkinter as tk
from tkinter import messagebox
from todo import load_tasks, save_tasks


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo CLI")
        self.root.geometry("400x500")
        self.root.configure(bg="#1e1e2e")

        # Title
        title = tk.Label(
            root, text="My Tasks",
            font=("Helvetica", 18, "bold"),
            bg="#1e1e2e", fg="#cdd6f4"
        )
        title.pack(pady=(15, 5))

        # Entry + Add button
        entry_frame = tk.Frame(root, bg="#1e1e2e")
        entry_frame.pack(pady=5, padx=15, fill="x")

        self.entry = tk.Entry(
            entry_frame, font=("Helvetica", 12),
            bg="#313244", fg="#cdd6f4",
            insertbackground="#cdd6f4", relief="flat"
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 6))
        self.entry.bind("<Return>", lambda e: self.add_task())

        add_btn = tk.Button(
            entry_frame, text="Add", command=self.add_task,
            bg="#89b4fa", fg="#1e1e2e", relief="flat",
            font=("Helvetica", 11, "bold"), padx=14
        )
        add_btn.pack(side="left")

        # Task list
        list_frame = tk.Frame(root, bg="#1e1e2e")
        list_frame.pack(pady=10, padx=15, fill="both", expand=True)

        self.listbox = tk.Listbox(
            list_frame, font=("Helvetica", 12),
            bg="#313244", fg="#cdd6f4",
            selectbackground="#89b4fa", selectforeground="#1e1e2e",
            relief="flat", activestyle="none", highlightthickness=0
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Buttons
        btn_frame = tk.Frame(root, bg="#1e1e2e")
        btn_frame.pack(pady=10, padx=15, fill="x")

        done_btn = tk.Button(
            btn_frame, text="Mark Done", command=self.mark_done,
            bg="#a6e3a1", fg="#1e1e2e", relief="flat",
            font=("Helvetica", 11, "bold"), padx=14, pady=4
        )
        done_btn.pack(side="left", expand=True, fill="x", padx=(0, 5))

        del_btn = tk.Button(
            btn_frame, text="Delete", command=self.delete_task,
            bg="#f38ba8", fg="#1e1e2e", relief="flat",
            font=("Helvetica", 11, "bold"), padx=14, pady=4
        )
        del_btn.pack(side="left", expand=True, fill="x", padx=(5, 0))

        self.refresh()
        self.entry.focus_set()

    def refresh(self):
        self.listbox.delete(0, tk.END)
        self.tasks = load_tasks()
        for t in self.tasks:
            mark = "✓" if t["done"] else "○"
            self.listbox.insert(tk.END, f" {mark}  {t['text']}")

    def add_task(self):
        text = self.entry.get().strip()
        if not text:
            return
        self.tasks.append({"text": text, "done": False})
        save_tasks(self.tasks)
        self.entry.delete(0, tk.END)
        self.refresh()

    def mark_done(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("No selection", "Select a task first.")
            return
        self.tasks[sel[0]]["done"] = True
        save_tasks(self.tasks)
        self.refresh()

    def delete_task(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("No selection", "Select a task first.")
            return
        removed = self.tasks.pop(sel[0])
        save_tasks(self.tasks)
        self.refresh()
        messagebox.showinfo("Deleted", f"Removed: {removed['text']}")


if __name__ == "__main__":
    root = tk.Tk()
    TodoApp(root)
    root.mainloop()
