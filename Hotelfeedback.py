import tkinter as tk
from tkinter import messagebox

class CustomerFeedbackForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Feedback Form")
        self.root.geometry("500x700")
        self.root.configure(bg="#f0f4f7")

        # Title Label
        title_label = tk.Label(
            root,
            text="Customer Feedback Form",
            font=("Arial", 18, "bold"),
            bg="#f0f4f7",
            fg="#333"
        )
        title_label.pack(pady=20)

        # --- Name Section ---
        frame_name = tk.Frame(root, bg="#f0f4f7")
        frame_name.pack(pady=10)
        tk.Label(frame_name, text="Full Name:", font=("Arial", 12), bg="#f0f4f7").pack()
        self.entry_name = tk.Entry(frame_name, width=40, font=("Arial", 11))
        self.entry_name.pack(pady=5, ipady=3)

        # --- Feedback Section ---
        frame_feedback = tk.Frame(root, bg="#f0f4f7")
        frame_feedback.pack(pady=10)
        tk.Label(frame_feedback, text="Your Feedback:", font=("Arial", 12), bg="#f0f4f7").pack()
        self.text_feedback = tk.Text(frame_feedback, height=5, width=50, font=("Arial", 10))
        self.text_feedback.pack(pady=5)

        # --- Ratings Section ---
        frame_ratings = tk.Frame(root, bg="#f0f4f7")
        frame_ratings.pack(pady=10)
        tk.Label(frame_ratings, text="Rate the following (1–5):", font=("Arial", 13, "bold"), bg="#f0f4f7").pack(pady=5)

        self.rating_fields = {
            "Food Quality": tk.IntVar(),
            "Service": tk.IntVar(),
            "Cleanliness": tk.IntVar(),
            "Ambience": tk.IntVar(),
            "Value for Money": tk.IntVar()
        }

        # Rating Options
        options = [("Excellent", 5), ("Good", 4), ("Satisfactory", 3), ("Needs Improvement", 2), ("Poor", 1)]

        for category, var in self.rating_fields.items():
            cat_frame = tk.Frame(frame_ratings, bg="#e9eef2", relief="groove", bd=1)
            cat_frame.pack(pady=5, fill="x", padx=20)

            tk.Label(cat_frame, text=category + ":", font=("Arial", 11, "bold"), bg="#e9eef2").pack(anchor="w", padx=10, pady=2)

            radio_frame = tk.Frame(cat_frame, bg="#e9eef2")
            radio_frame.pack(anchor="w", padx=15)

            for text, value in options:
                tk.Radiobutton(
                    radio_frame,
                    text=text,
                    variable=var,
                    value=value,
                    bg="#e9eef2",
                    font=("Arial", 10)
                ).pack(side="left", padx=5)

        # --- Submit Button ---
        self.submit_button = tk.Button(
            root,
            text="Submit Feedback",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            width=20,
            pady=6,
            command=self.submit_feedback
        )
        self.submit_button.pack(pady=30)

        # --- Footer ---
        footer = tk.Label(root, text="Thank you for sharing your experience!", font=("Arial", 10, "italic"), bg="#f0f4f7", fg="#555")
        footer.pack(pady=5)

    def submit_feedback(self):
        name = self.entry_name.get().strip()
        feedback = self.text_feedback.get("1.0", tk.END).strip()
        ratings = {k: v.get() for k, v in self.rating_fields.items()}

        if not name or not feedback or any(v == 0 for v in ratings.values()):
            messagebox.showerror("Error", "Please fill in your name, feedback, and select ratings for all categories.")
            return

        # Save feedback to file
        with open("feedback_records.txt", "a") as f:
            f.write(f"Name: {name}\n")
            f.write(f"Feedback: {feedback}\n")
            for category, rating in ratings.items():
                f.write(f"{category}: {rating}\n")
            f.write("-" * 40 + "\n")

        # Confirmation Message
        msg = f"Thank you, {name}!\n\nYour feedback has been recorded successfully."
        messagebox.showinfo("Feedback Submitted", msg)

        # Clear form
        self.entry_name.delete(0, tk.END)
        self.text_feedback.delete("1.0", tk.END)
        for var in self.rating_fields.values():
            var.set(0)

def main():
    root = tk.Tk()
    feedback_form = CustomerFeedbackForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()
