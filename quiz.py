import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz App")
        self.root.geometry("500x400")
        
        # Sample questions and answers
        self.questions = [
            "What is the output of 3**2?",
            "What does the // operator do in Python?",
            "Which of the following is a mutable data type in Python?",
            "What is the correct file extension for Python files?",
            "What is the output of print(2 == 2.0)?"
        ]
        
        self.options = [
            ["6", "8", "9", "12"],
            ["Floor division", "Modulus", "Exponent", "Bitwise AND"],
            ["Tuple", "String", "List", "Integer"],
            [".py", ".python", ".pyt", ".pt"],
            ["True", "False", "Error", "None"]
        ]
        
        self.answers = [2, 0, 2, 0, 0]  # correct options for each question
        self.current_question = 0
        self.score = 0

        # Setup UI elements
        self.question_label = tk.Label(root, text=self.questions[self.current_question], font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.option_var = tk.IntVar()
        self.option_buttons = []
        
        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.option_var, value=i, font=("Arial", 12))
            btn.pack(anchor="w")
            self.option_buttons.append(btn)
        
        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=20)

        self.display_question()

    def display_question(self):
        self.question_label.config(text=self.questions[self.current_question])
        self.option_var.set(-1)
        
        for i, option in enumerate(self.options[self.current_question]):
            self.option_buttons[i].config(text=option)

    def next_question(self):
        if self.option_var.get() == -1:
            messagebox.showwarning("Warning", "Please select an answer before proceeding.")
            return
        
        if self.option_var.get() == self.answers[self.current_question]:
            self.score += 1
        
        self.current_question += 1
        
        if self.current_question == len(self.questions):
            self.show_score()
        else:
            self.display_question()

    def show_score(self):
        messagebox.showinfo("Quiz Complete", f"Your score is: {self.score}/{len(self.questions)}")
        self.root.destroy()

# Create the Tkinter window
root = tk.Tk()
quiz_app = QuizApp(root)
root.mainloop()
