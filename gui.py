import tkinter as tk
from logic import add, subtract, multiply, divide

def create_gui():
    root = tk.Tk()
    root.title("Calculator")

    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1)

    def show_result(func):
        try:
            num1 = float(entry1.get())
            num2 = float(entry2.get())
            result_label.config(text=f"Result: {func(num1, num2)}")
        except ValueError:
            result_label.config(text="Invalid input!")

    tk.Label(root, text="First Number:").grid(row=0, column=0)
    tk.Label(root, text="Second Number:").grid(row=1, column=0)
    result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
    result_label.grid(row=3, column=0, columnspan=2)

    tk.Button(root, text="Add", command=lambda: show_result(add)).grid(row=2, column=0)
    tk.Button(root, text="Subtract", command=lambda: show_result(subtract)).grid(row=2, column=1)
    tk.Button(root, text="Multiply", command=lambda: show_result(multiply)).grid(row=2, column=2)
    tk.Button(root, text="Divide", command=lambda: show_result(divide)).grid(row=2, column=3)

    root.mainloop()
