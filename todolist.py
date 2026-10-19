
import tkinter as tk
from tkinter import messagebox

BG = "#151525"
CARD = "#22223A"
PURPLE = "#8B5CF6"
WHITE = "#FFFFFF"

root = tk.Tk()
root.title("TaskFlow")
root.geometry("420x520")
root.configure(bg=BG)
root.resizable(False, False)

tasks = []

tk.Label(
    root, text="TaskFlow",
    font=("Segoe UI", 26, "bold"),
    bg=BG, fg=WHITE
).pack(pady=(20, 3))

tk.Label(
    root, text="Plan your day. Achieve more.",
    font=("Segoe UI", 10),
    bg=BG, fg="#A5A5C5"
).pack(pady=(0, 20))

entry = tk.Entry(
    root, font=("Segoe UI", 13),
    bg=CARD, fg=WHITE,
    insertbackground=WHITE,
    relief="flat"
)
entry.pack(fill="x", padx=25, ipady=12)

listbox = tk.Listbox(
    root, font=("Segoe UI", 12),
    bg=CARD, fg=WHITE,
    selectbackground=PURPLE,
    relief="flat", borderwidth=0
)
listbox.pack(fill="both", expand=True, padx=25, pady=18)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, "  ○  " + task)
        entry.delete(0, tk.END)
    else:
        messagebox.showinfo("TaskFlow", "Enter a task first!")

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        tasks.pop(index)

def complete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = tasks[index]
        listbox.delete(index)
        listbox.insert(index, "  ✓  " + task)
        listbox.itemconfig(index, fg="#34D399")

buttons = tk.Frame(root, bg=BG)
buttons.pack(pady=(0, 20))

tk.Button(
    buttons, text=" + Add Task ",
    command=add_task, bg=PURPLE,
    fg=WHITE, relief="flat",
    font=("Segoe UI", 11, "bold"),
    cursor="hand2", padx=10, pady=9
).pack(side="left", padx=5)

tk.Button(
    buttons, text="✓ Complete",
    command=complete_task, bg="#16876A",
    fg=WHITE, relief="flat",
    font=("Segoe UI", 11),
    cursor="hand2", padx=10, pady=9
).pack(side="left", padx=5)

tk.Button(
    buttons, text="Delete",
    command=delete_task, bg="#C2415D",
    fg=WHITE, relief="flat",
    font=("Segoe UI", 11),
    cursor="hand2", padx=10, pady=9
).pack(side="left", padx=5)

entry.bind("<Return>", lambda event: add_task())

root.mainloop()
