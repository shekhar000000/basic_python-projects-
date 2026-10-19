
import tkinter as tk
from tkinter import messagebox
import csv
import os

BG = "#101820"
CARD = "#202D3A"
GREEN = "#2DD4A7"
WHITE = "#FFFFFF"
FILE = "expenses.csv"

root = tk.Tk()
root.title("My Expense Tracker")
root.geometry("480x580")
root.configure(bg=BG)
root.resizable(False, False)

expenses = []

tk.Label(
    root, text="Expense Tracker",
    font=("Segoe UI", 24, "bold"),
    bg=BG, fg=GREEN
).pack(pady=(20, 5))

tk.Label(
    root, text="Track your daily spending",
    font=("Segoe UI", 11),
    bg=BG, fg="#AAB8C5"
).pack(pady=(0, 15))

form = tk.Frame(root, bg=BG)
form.pack(fill="x", padx=25)

tk.Label(form, text="Expense name", bg=BG, fg=WHITE).grid(
    row=0, column=0, sticky="w", pady=5
)
name_entry = tk.Entry(form, bg=CARD, fg=WHITE,
                      insertbackground=WHITE, relief="flat")
name_entry.grid(row=1, column=0, sticky="ew", ipady=8, padx=(0, 8))

tk.Label(form, text="Amount (₹)", bg=BG, fg=WHITE).grid(
    row=0, column=1, sticky="w", pady=5
)
amount_entry = tk.Entry(form, bg=CARD, fg=WHITE,
                        insertbackground=WHITE, relief="flat")
amount_entry.grid(row=1, column=1, sticky="ew", ipady=8)

form.columnconfigure(0, weight=2)
form.columnconfigure(1, weight=1)

total_label = tk.Label(
    root, text="Total Spent: ₹0.00",
    font=("Segoe UI", 16, "bold"),
    bg=BG, fg=GREEN
)
total_label.pack(pady=15)

items = tk.Listbox(
    root, bg=CARD, fg=WHITE,
    font=("Segoe UI", 11),
    selectbackground=GREEN,
    relief="flat", borderwidth=0
)
items.pack(fill="both", expand=True, padx=25, pady=5)

def refresh():
    items.delete(0, tk.END)
    for name, amount in expenses:
        items.insert(tk.END, f"{name}   —   ₹{amount:.2f}")
    total = sum(amount for _, amount in expenses)
    total_label.config(text=f"Total Spent: ₹{total:.2f}")

def add_expense():
    name = name_entry.get().strip()

    try:
        amount = float(amount_entry.get())
        if not name or amount <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Enter an expense name and a positive amount."
        )
        return

    expenses.append((name, amount))

    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, amount])

    name_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    refresh()

def load_expenses():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r", newline="", encoding="utf-8") as f:
                for row in csv.reader(f):
                    if len(row) == 2:
                        expenses.append((row[0], float(row[1])))
        except (ValueError, OSError, csv.Error):
            messagebox.showwarning(
                "File Warning", "Some saved expenses could not be loaded."
            )
    refresh()

def delete_expense():
    selected = items.curselection()
    if not selected:
        messagebox.showinfo("Select Expense", "Choose an expense to delete.")
        return

    expenses.pop(selected[0])

    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(expenses)

    refresh()

buttons = tk.Frame(root, bg=BG)
buttons.pack(pady=15)

tk.Button(
    buttons, text=" + Add Expense ",
    command=add_expense, bg=GREEN, fg=BG,
    relief="flat", font=("Segoe UI", 10, "bold"),
    cursor="hand2", pady=9
).pack(side="left", padx=5)

tk.Button(
    buttons, text="Delete Selected",
    command=delete_expense, bg="#E45C70", fg=WHITE,
    relief="flat", font=("Segoe UI", 10),
    cursor="hand2", pady=9
).pack(side="left", padx=5)

load_expenses()
root.mainloop()
