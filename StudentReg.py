import tkinter as tk
from tkinter import messagebox

class StudentRegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration Form")
        self.root.geometry("500x550")
        self.root.configure(bg="#f0f4f7")

        # ====== Title ======
        self.title_label = tk.Label(
            root,
            text="📘 Student Registration Portal",
            font=("Arial", 18, "bold"),
            bg="#f0f4f7",
            fg="#2c3e50"
        )
        self.title_label.pack(pady=15)

        # ====== Main Frame ======
        self.frame = tk.Frame(root, bg="white", relief="ridge", bd=2)
        self.frame.pack(padx=25, pady=10, fill="both", expand=True)

        # ====== Student Name ======
        self.label_name = tk.Label(self.frame, text="Full Name:", font=("Arial", 12, "bold"), bg="white", anchor="w")
        self.label_name.pack(pady=(20, 5), padx=25, fill="x")
        self.entry_name = tk.Entry(self.frame, font=("Arial", 12), width=35, bd=2, relief="groove")
        self.entry_name.pack(padx=25, pady=5)

        # ====== Student Email ======
        self.label_email = tk.Label(self.frame, text="Email Address:", font=("Arial", 12, "bold"), bg="white", anchor="w")
        self.label_email.pack(pady=(15, 5), padx=25, fill="x")
        self.entry_email = tk.Entry(self.frame, font=("Arial", 12), width=35, bd=2, relief="groove")
        self.entry_email.pack(padx=25, pady=5)

        # ====== Course Selection ======
        self.label_course = tk.Label(self.frame, text="Select Course:", font=("Arial", 12, "bold"), bg="white", anchor="w")
        self.label_course.pack(pady=(15, 5), padx=25, fill="x")
        self.courses = ["Mathematics", "Science", "English", "History", "Computer Engineering"]
        self.course_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE, height=5, font=("Arial", 11),
                                         bd=2, relief="groove", exportselection=False)
        for course in self.courses:
            self.course_listbox.insert(tk.END, course)
        self.course_listbox.pack(pady=5, padx=25, fill="x")

        # ====== Gender Selection ======
        self.label_gender = tk.Label(self.frame, text="Select Gender:", font=("Arial", 12, "bold"), bg="white", anchor="w")
        self.label_gender.pack(pady=(15, 5), padx=25, fill="x")
        self.gender_var = tk.StringVar(value="None")
        gender_frame = tk.Frame(self.frame, bg="white")
        gender_frame.pack(pady=5)
        tk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male", font=("Arial", 11), bg="white").pack(side="left", padx=10)
        tk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female", font=("Arial", 11), bg="white").pack(side="left", padx=10)
        tk.Radiobutton(gender_frame, text="Other", variable=self.gender_var, value="Other", font=("Arial", 11), bg="white").pack(side="left", padx=10)

        # ====== Submit Button ======
        self.submit_button = tk.Button(
            root,
            text="Submit Registration",
            font=("Arial", 13, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            width=25,
            pady=10,
            command=self.submit_form
        )
        self.submit_button.pack(pady=25)

        # ====== Footer Label ======
        self.footer_label = tk.Label(
            root,
            text="© 2025 University Enrollment Portal | Designed with HCI Principles",
            font=("Arial", 9, "italic"),
            bg="#f0f4f7",
            fg="#555"
        )
        self.footer_label.pack(side="bottom", pady=10)

    def submit_form(self):
        name = self.entry_name.get().strip()
        email = self.entry_email.get().strip()
        selected_course_index = self.course_listbox.curselection()
        gender = self.gender_var.get()

        # ====== Validation ======
        if not name or not email or not selected_course_index or gender == "None":
            messagebox.showerror(" Missing Information", "Please fill in all the required fields.")
            return

        if "@" not in email or "." not in email:
            messagebox.showwarning(" Invalid Email", "Please enter a valid email address.")
            return

        selected_course = self.courses[selected_course_index[0]]

        # ====== Success Message ======
        summary = (
            f"🎓 Registration Successful!\n\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Course: {selected_course}\n"
            f"Gender: {gender}"
        )
        messagebox.showinfo(" Success", summary)

        # Clear fields for next entry
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.course_listbox.selection_clear(0, tk.END)
        self.gender_var.set("None")

def main():
    root = tk.Tk()
    app = StudentRegistrationForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
