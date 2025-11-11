import tkinter as tk
from tkinter import messagebox

class SignUpWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("User Sign Up Form")
        self.root.geometry("450x380")
        self.root.configure(bg="#f0f4f7")

        # ====== Title Label ======
        self.title_label = tk.Label(
            root,
            text="Create Your Account",
            font=("Arial", 18, "bold"),
            bg="#f0f4f7",
            fg="#2c3e50"
        )
        self.title_label.pack(pady=15)

        # ====== Main Frame ======
        self.frame = tk.Frame(root, bg="#ffffff", relief="ridge", bd=2)
        self.frame.pack(padx=25, pady=10, fill="both", expand=True)

        # ====== Name Field ======
        self.label_name = tk.Label(
            self.frame, text="Full Name:", font=("Arial", 12, "bold"), bg="#ffffff", anchor="w"
        )
        self.label_name.pack(pady=(15, 5), padx=25, fill="x")
        self.entry_name = tk.Entry(self.frame, font=("Arial", 12), width=35, bd=2, relief="groove")
        self.entry_name.pack(padx=25, pady=5)

        # ====== Email Field ======
        self.label_email = tk.Label(
            self.frame, text="Email Address:", font=("Arial", 12, "bold"), bg="#ffffff", anchor="w"
        )
        self.label_email.pack(pady=(10, 5), padx=25, fill="x")
        self.entry_email = tk.Entry(self.frame, font=("Arial", 12), width=35, bd=2, relief="groove")
        self.entry_email.pack(padx=25, pady=5)

        # ====== Password Field ======
        self.label_password = tk.Label(
            self.frame, text="Password:", font=("Arial", 12, "bold"), bg="#ffffff", anchor="w"
        )
        self.label_password.pack(pady=(10, 5), padx=25, fill="x")
        self.entry_password = tk.Entry(self.frame, font=("Arial", 12), show="*", width=35, bd=2, relief="groove")
        self.entry_password.pack(padx=25, pady=5)

        # ====== Submit Button ======
        self.submit_button = tk.Button(
            root,
            text="Sign Up",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            width=20,
            pady=8,
            command=self.sign_up
        )
        self.submit_button.pack(pady=20)

        # ====== Footer Label ======
        self.footer_label = tk.Label(
            root,
            text="Already have an account? Contact support to log in.",
            font=("Arial", 10, "italic"),
            bg="#f0f4f7",
            fg="#555"
        )
        self.footer_label.pack(pady=(0, 10))

    def sign_up(self):
        """Handles sign-up validation and feedback."""
        name = self.entry_name.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get().strip()

        # Basic validation
        if not name or not email or not password:
            messagebox.showerror("Error ", "Please fill in all the fields.")
            return

        if "@" not in email or "." not in email:
            messagebox.showwarning("Invalid Email", "Please enter a valid email address.")
            return

        if len(password) < 6:
            messagebox.showwarning("Weak Password", "Password should be at least 6 characters long.")
            return

        # Display confirmation message
        message = f"Sign Up Successful \n\nWelcome, {name}!\nYour email: {email}"
        messagebox.showinfo("Success", message)

        # Reset form fields
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = SignUpWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
