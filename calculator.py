
import tkinter as tk

BG = "#10131A"
CARD = "#202735"
TEXT = "#FFFFFF"
GREEN = "#28B889"
PURPLE = "#7C5CFC"
BUTTON = "#293348"

root = tk.Tk()
root.title("Nova Calculator")
root.geometry("340x480")
root.configure(bg=BG)
root.resizable(False, False)

expression = tk.StringVar(value="")

display = tk.Entry(
    root,
    textvariable=expression,
    font=("Segoe UI", 26),
    bg=CARD,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    justify="right",
    bd=0
)
display.pack(fill="x", padx=16, pady=20, ipady=20)


def press(value):
    if value == "AC":
        expression.set("")
    elif value == "DEL":
        expression.set(expression.get()[:-1])
    elif value == "=":
        try:
            # Evaluate only a limited set of arithmetic operations.
            import ast
            import operator

            ops = {
                ast.Add: operator.add,
                ast.Sub: operator.sub,
                ast.Mult: operator.mul,
                ast.Div: operator.truediv,
                ast.Mod: operator.mod,
            }

            def calc(node):
                if isinstance(node, ast.Expression):
                    return calc(node.body)
                if isinstance(node, ast.Constant) and type(node.value) in (int, float):
                    return node.value
                if isinstance(node, ast.BinOp) and type(node.op) in ops:
                    right = calc(node.right)
                    if isinstance(node.op, ast.Div) and right == 0:
                        raise ZeroDivisionError
                    return ops[type(node.op)](calc(node.left), right)
                if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
                    val = calc(node.operand)
                    return -val if isinstance(node.op, ast.USub) else val
                raise ValueError("Invalid expression")

            result = calc(ast.parse(expression.get(), mode="eval"))
            expression.set(str(result))
        except Exception:
            expression.set("Error")
    else:
        if expression.get() == "Error":
            expression.set("")
        expression.set(expression.get() + value)


buttons = [
    ["AC", "DEL", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "(", ")"],
    ["="]
]

frame = tk.Frame(root, bg=BG)
frame.pack(fill="both", expand=True, padx=12, pady=5)

for r, row in enumerate(buttons):
    frame.grid_rowconfigure(r, weight=1)
    for c in range(4):
        frame.grid_columnconfigure(c, weight=1)

    for c, value in enumerate(row):
        color = (
            GREEN if value == "="
            else PURPLE if value in ["+", "-", "*", "/", "%"]
            else "#E85D75" if value in ["AC", "DEL"]
            else BUTTON
        )

        btn = tk.Button(
            frame,
            text=value,
            font=("Segoe UI", 15, "bold"),
            bg=color,
            fg=TEXT,
            activebackground="#46536A",
            activeforeground=TEXT,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda v=value: press(v)
        )

        if value == "=":
            btn.grid(
                row=r, column=0, columnspan=4,
                sticky="nsew", padx=4, pady=4
            )
            break
        else:
            btn.grid(
                row=r, column=c,
                sticky="nsew", padx=4, pady=4
            )

root.bind("<Return>", lambda event: press("="))
root.bind("<BackSpace>", lambda event: press("DEL"))
root.bind("<Escape>", lambda event: press("AC"))

root.mainloop()
