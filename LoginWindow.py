import tkinter as tk
from tkinter import messagebox

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("User Authentication System")
        self.root.geometry("350x350")
        self.root.configure(bg="#f0f4f7")

        self.current_mode = "login"  # Track current view: login/signup

        # Title Label
        self.title_label = tk.Label(
            root, text="Welcome!", font=("Arial", 18, "bold"), bg="#f0f4f7", fg="#333"
        )
        self.title_label.pack(pady=15)

        # Frame for form inputs
        self.form_frame = tk.Frame(root, bg="#f0f4f7")
        self.form_frame.pack(pady=10)

        # Username
        self.label_username = tk.Label(self.form_frame, text="Username:", font=("Arial", 11), bg="#f0f4f7")
        self.label_username.grid(row=0, column=0, pady=10, padx=5, sticky="e")
        self.entry_username = tk.Entry(self.form_frame, width=25, font=("Arial", 11))
        self.entry_username.grid(row=0, column=1, pady=10, padx=5)

        # Password
        self.label_password = tk.Label(self.form_frame, text="Password:", font=("Arial", 11), bg="#f0f4f7")
        self.label_password.grid(row=1, column=0, pady=10, padx=5, sticky="e")
        self.entry_password = tk.Entry(self.form_frame, show="*", width=25, font=("Arial", 11))
        self.entry_password.grid(row=1, column=1, pady=10, padx=5)

        # Login / Signup button
        self.button_action = tk.Button(
            root,
            text="Login",
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            pady=5,
            command=self.handle_action
        )
        self.button_action.pack(pady=20)

        # Switch mode label
        self.switch_label = tk.Label(
            root,
            text="Don't have an account?",
            bg="#f0f4f7",
            font=("Arial", 10)
        )
        self.switch_label.pack()

        self.switch_button = tk.Button(
            root,
            text="Sign Up",
            bg="#2196F3",
            fg="white",
            font=("Arial", 10, "bold"),
            command=self.toggle_mode
        )
        self.switch_button.pack(pady=5)

        # Footer
        tk.Label(
            root,
            text="Simple Login System for HCI Lab",
            font=("Arial", 9, "italic"),
            bg="#f0f4f7",
            fg="#666"
        ).pack(pady=10)

        # Simulated user storage
        self.registered_users = {"admin": "password"}

    def handle_action(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Please fill in both fields.")
            return

        if self.current_mode == "login":
            if username in self.registered_users and self.registered_users[username] == password:
                messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
        else:  # Signup mode
            if username in self.registered_users:
                messagebox.showerror("Error", "Username already exists! Please choose another.")
            else:
                self.registered_users[username] = password
                messagebox.showinfo("Success", f"Account created successfully for {username}!")
                self.toggle_mode()  # Switch back to login mode after signup

        # Clear input fields
        self.entry_username.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def toggle_mode(self):
        if self.current_mode == "login":
            self.current_mode = "signup"
            self.title_label.config(text="Create Account")
            self.button_action.config(text="Sign Up", bg="#2196F3")
            self.switch_label.config(text="Already have an account?")
            self.switch_button.config(text="Login", bg="#4CAF50")
        else:
            self.current_mode = "login"
            self.title_label.config(text="Welcome Back!")
            self.button_action.config(text="Login", bg="#4CAF50")
            self.switch_label.config(text="Don't have an account?")
            self.switch_button.config(text="Sign Up", bg="#2196F3")

def main():
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
