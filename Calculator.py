import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x300")
        self.root.configure(bg="#f3f6f9")

        # --- Title ---
        tk.Label(
            root,
            text="Simple Calculator",
            font=("Arial", 16, "bold"),
            bg="#f3f6f9",
            fg="#333"
        ).pack(pady=15)

        # --- Input Frame ---
        input_frame = tk.Frame(root, bg="#f3f6f9")
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="Number 1:", bg="#f3f6f9", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5)
        self.entry_num1 = tk.Entry(input_frame, width=10, font=('Arial', 12))
        self.entry_num1.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Number 2:", bg="#f3f6f9", font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=5)
        self.entry_num2 = tk.Entry(input_frame, width=10, font=('Arial', 12))
        self.entry_num2.grid(row=1, column=1, padx=5, pady=5)

        # --- Result Label ---
        self.result_label = tk.Label(
            root,
            text="Result: ",
            font=("Arial", 12, "bold"),
            bg="#f3f6f9",
            fg="#2e7d32"
        )
        self.result_label.pack(pady=10)

        # --- Buttons Frame ---
        button_frame = tk.Frame(root, bg="#f3f6f9")
        button_frame.pack(pady=10)

        operations = [
            ("Addition", "#4CAF50"),
            ("Subtraction", "#2196F3"),
            ("Multiplication", "#FF9800"),
            ("Division", "#F44336")
        ]

        row_val, col_val = 0, 0
        for text, color in operations:
            tk.Button(
                button_frame,
                text=text,
                width=14,
                height=2,
                bg=color,
                fg="white",
                font=("Arial", 10, "bold"),
                relief="raised",
                bd=2,
                activebackground="#333",
                command=lambda op=text: self.calculate(op)
            ).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 1:
                col_val = 0
                row_val += 1

        # --- Footer ---
        tk.Label(
            root,
            text="Designed for HCI Lab",
            font=("Arial", 9, "italic"),
            bg="#f3f6f9",
            fg="#666"
        ).pack(pady=5)

    def calculate(self, operation):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())

            if operation == 'Addition':
                result = num1 + num2
            elif operation == 'Subtraction':
                result = num1 - num2
            elif operation == 'Multiplication':
                result = num1 * num2
            elif operation == 'Division':
                result = num1 / num2

            self.result_label.config(text=f"Result: {result}")
        except Exception:
            self.result_label.config(text="Error: Invalid Input")

def main():
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
