
import tkinter as tk
import secrets
import string

BG = "#12121F"
CARD = "#25253A"
PURPLE = "#9B72F2"
WHITE = "#FFFFFF"

root = tk.Tk()
root.title("PassCraft")
root.geometry("380x350")
root.configure(bg=BG)
root.resizable(False, False)

tk.Label(
    root, text="PassCraft",
    font=("Segoe UI", 26, "bold"),
    bg=BG, fg=PURPLE
).pack(pady=(25, 5))

tk.Label(
    root, text="Create a strong password",
    font=("Segoe UI", 11),
    bg=BG, fg="#BBBBCC"
).pack(pady=(0, 20))

length = tk.IntVar(value=16)

tk.Label(
    root, text="Password length",
    bg=BG, fg=WHITE
).pack()

tk.Spinbox(
    root, from_=8, to=40,
    textvariable=length,
    font=("Segoe UI", 12),
    width=8
).pack(pady=8)

password = tk.Entry(
    root, font=("Consolas", 13),
    bg=CARD, fg=WHITE,
    insertbackground=WHITE,
    justify="center", relief="flat"
)
password.pack(fill="x", padx=25, ipady=12, pady=12)

def generate():
    chars = string.ascii_letters + string.digits + "!@#$%&*?"
    result = "".join(
        secrets.choice(chars) for _ in range(length.get())
    )
    password.delete(0, tk.END)
    password.insert(0, result)

def copy_password():
    value = password.get()
    if value:
        root.clipboard_clear()
        root.clipboard_append(value)

tk.Button(
    root, text="Generate Password",
    command=generate,
    bg=PURPLE, fg=WHITE,
    font=("Segoe UI", 11, "bold"),
    relief="flat", cursor="hand2", pady=10
).pack(fill="x", padx=25, pady=5)

tk.Button(
    root, text="Copy Password",
    command=copy_password,
    bg=CARD, fg=WHITE,
    font=("Segoe UI", 10),
    relief="flat", cursor="hand2", pady=8
).pack(fill="x", padx=25)

root.mainloop()
