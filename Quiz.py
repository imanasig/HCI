import tkinter as tk
from tkinter import messagebox

class OnlineQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz System")
        self.root.geometry("550x400")
        self.root.configure(bg="#f0f4f7")

        # Title Label
        self.title_label = tk.Label(
            root, text="Welcome to the Online Quiz!",
            font=("Arial", 18, "bold"),
            bg="#f0f4f7",
            fg="#333"
        )
        self.title_label.pack(pady=15)

        # Frame for the quiz content
        self.quiz_frame = tk.Frame(root, bg="#ffffff", relief="ridge", bd=2)
        self.quiz_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Question Label
        self.label_question = tk.Label(
            self.quiz_frame,
            text="",
            font=("Arial", 14, "bold"),
            bg="#ffffff",
            wraplength=480,
            justify="left"
        )
        self.label_question.pack(pady=20)

        # Variable for selected option
        self.selected_option = tk.StringVar()

        # Radio Buttons for Options
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.quiz_frame,
                text="",
                variable=self.selected_option,
                value="",
                font=("Arial", 12),
                bg="#ffffff",
                anchor="w",
                padx=15,
                pady=5,
                relief="flat",
                activebackground="#e3f2fd"
            )
            rb.pack(fill="x", padx=30, pady=3)
            self.option_buttons.append(rb)

        # Next Button
        self.next_button = tk.Button(
            root,
            text="Next Question ➜",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            width=18,
            pady=6,
            command=self.next_question
        )
        self.next_button.pack(pady=15)

        # Footer Label
        self.footer_label = tk.Label(
            root,
            text="Answer all questions carefully!",
            font=("Arial", 10, "italic"),
            bg="#f0f4f7",
            fg="#555"
        )
        self.footer_label.pack(pady=5)

        # Quiz Data
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "correct": "Paris"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Saturn"], "correct": "Mars"},
            {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe", "Lion"], "correct": "Blue Whale"},
            {"question": "Who developed the theory of relativity?", "options": ["Newton", "Einstein", "Tesla", "Edison"], "correct": "Einstein"},
            {"question": "Which language is used to create web pages?", "options": ["Python", "C++", "HTML", "Java"], "correct": "HTML"}
        ]

        # Tracking variables
        self.current_question_index = 0
        self.score = 0

        # Display first question
        self.display_question()

    def display_question(self):
        """Displays the current question and options."""
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=f"Q{self.current_question_index + 1}. {question_data['question']}")

            self.selected_option.set(None)
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option, value=option)
        else:
            self.show_results()

    def next_question(self):
        """Handles user input and moves to the next question."""
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an option before continuing.")
            return

        correct_answer = self.questions[self.current_question_index]["correct"]
        if selected == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct ✅", f"Great job! '{selected}' is the right answer.")
        else:
            messagebox.showinfo("Incorrect ❌", f"Oops! The correct answer is '{correct_answer}'.")

        self.current_question_index += 1
        self.display_question()

    def show_results(self):
        """Displays the final score."""
        total = len(self.questions)
        messagebox.showinfo(
            "Quiz Completed 🎉",
            f"You've completed the quiz!\n\nYour Score: {self.score}/{total}\n\nThank you for participating!"
        )
        self.root.destroy()  # Close window after completion

def main():
    root = tk.Tk()
    app = OnlineQuiz(root)
    root.mainloop()

if __name__ == "__main__":
    main()
