
import tkinter as tk
from tkinter import messagebox

BG = "#101827"
CARD = "#1E293B"
ACCENT = "#38BDF8"
WHITE = "#FFFFFF"

root = tk.Tk()
root.title("Student Result")
root.geometry("380x570")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(
    root, text="STUDENT RESULT",
    font=("Segoe UI", 22, "bold"),
    bg=BG, fg=ACCENT
).pack(pady=20)

entries = []

for subject in ["Mathematics", "Programming",
                "Database", "Networks", "English"]:
    tk.Label(
        root, text=subject,
        bg=BG, fg=WHITE,
        font=("Segoe UI", 11)
    ).pack(anchor="w", padx=35, pady=(8, 3))

    e = tk.Entry(
        root, font=("Segoe UI", 12),
        bg=CARD, fg=WHITE,
        insertbackground=WHITE,
        relief="flat"
    )
    e.pack(fill="x", padx=35, ipady=7)
    entries.append(e)

result = tk.Label(
    root, text="Enter marks out of 100",
    font=("Segoe UI", 12),
    bg=BG, fg=WHITE,
    justify="left"
)
result.pack(pady=20)

def calculate():
    try:
        marks = [float(e.get()) for e in entries]

        if any(m < 0 or m > 100 for m in marks):
            raise ValueError

        total = sum(marks)
        percentage = total / len(marks)
        status = "PASS" if all(m >= 35 for m in marks) else "FAIL"

        result.config(
            text=f"Total: {total:g} / 500\n"
                 f"Percentage: {percentage:.2f}%\n"
                 f"Result: {status}",
            fg="#34D399" if status == "PASS" else "#FB7185"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Marks",
            "Enter valid marks between 0 and 100."
        )

tk.Button(
    root, text="Calculate Result",
    command=calculate,
    bg=ACCENT, fg="#101827",
    font=("Segoe UI", 12, "bold"),
    relief="flat", cursor="hand2",
    pady=12
).pack(fill="x", padx=35)

root.mainloop()
