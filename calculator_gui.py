"""
GUI Calculator (Tkinter)
Basic arithmetic + scientific operations (sqrt, power, trig).
"""

import tkinter as tk
from tkinter import messagebox
import math


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        # Display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            root, textvariable=self.display_var,
            font=("Arial", 20), justify="right",
            bd=8, relief=tk.RIDGE
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Button layout: (label, row, col, colspan)
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("^", 5, 1), ("sqrt", 5, 2), ("(", 5, 3),
            ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), (")", 6, 3),
        ]

        for (label, row, col) in buttons:
            btn = tk.Button(
                root, text=label, font=("Arial", 14),
                width=5, height=2,
                command=lambda l=label: self.on_button_click(l)
            )
            btn.grid(row=row, column=col, padx=3, pady=3)

    def on_button_click(self, label):
        if label == "C":
            self.display_var.set("")
        elif label == "=":
            self.evaluate()
        elif label == "sqrt":
            self.apply_unary(math.sqrt, "Cannot take square root of a negative number.")
        elif label == "sin":
            self.apply_unary(lambda x: math.sin(math.radians(x)))
        elif label == "cos":
            self.apply_unary(lambda x: math.cos(math.radians(x)))
        elif label == "tan":
            self.apply_unary(lambda x: math.tan(math.radians(x)))
        elif label == "^":
            self.display_var.set(self.display_var.get() + "**")
        else:
            self.display_var.set(self.display_var.get() + label)

    def apply_unary(self, func, error_msg=None):
        """Apply a one-argument function (sqrt, sin, cos, tan) to the current display value."""
        current = self.display_var.get()
        try:
            value = float(current)
            result = func(value)
            self.display_var.set(str(result))
        except ValueError:
            messagebox.showerror("Error", error_msg or "Invalid input for this operation.")
        except Exception:
            messagebox.showerror("Error", "Could not compute result.")

    def evaluate(self):
        expression = self.display_var.get()
        try:
            # Restrict eval to basic math operators only, no builtins access
            result = eval(expression, {"__builtins__": {}}, {})
            self.display_var.set(str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero.")
            self.display_var.set("")
        except Exception:
            messagebox.showerror("Error", "Invalid expression.")
            self.display_var.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()