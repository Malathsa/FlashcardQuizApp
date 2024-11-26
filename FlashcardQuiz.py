import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎉 Flashcard Quiz App 🎉")
        self.flashcards = {}
        self.score = 0
        self.questions_asked = 0
        self.asked_questions = []
        self.current_question = ""
        
        # Set a light pink theme
        self.root.configure(bg="#ffeef2")
        
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="#ffeef2")
        self.frame.pack(pady=20)

        self.question_label = tk.Label(self.frame, text="Welcome to the Flashcard Quiz App!", font=("Arial", 20, "bold"), bg="#ffeef2", fg="#4B0082")  # Dark purple
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.frame, font=("Arial", 14), width=35, bg="#ffffff", bd=2, relief="solid")
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.frame, text="Submit Answer", command=self.check_answer, font=("Arial", 14), bg="#ffffff", fg="#4B0082", activebackground="#ffb3d1")  # Dark purple
        self.submit_button.pack(pady=10)

        self.add_flashcard_button = tk.Button(self.frame, text="Add Flashcard", command=self.add_flashcard, font=("Arial", 14), bg="#ffffff", fg="#4B0082", activebackground="#ffb3d1")  # Dark purple
        self.add_flashcard_button.pack(pady=10)

        self.quiz_button = tk.Button(self.frame, text="Start Quiz", command=self.start_quiz, font=("Arial", 14), bg="#ffffff", fg="#4B0082", activebackground="#ffb3d1")  # Dark purple
        self.quiz_button.pack(pady=10)

        self.score_label = tk.Label(self.frame, text="", font=("Arial", 16), bg="#ffeef2", fg="#4B0082")  # Dark purple
        self.score_label.pack(pady=10)

        self.footer = tk.Label(self.frame, text="Good luck and have fun!", font=("Arial", 12), bg="#ffeef2", fg="#4B0082")  # Dark purple
        self.footer.pack(pady=10)

    def add_flashcard(self):
        question = simpledialog.askstring("Add Flashcard", "Enter the question:")
        answer = simpledialog.askstring("Add Flashcard", "Enter the answer:")
        if question and answer:
            self.flashcards[question] = answer
            messagebox.showinfo("Success", "Flashcard added!")
        else:
            messagebox.showwarning("Input Error", "Please enter both a question and an answer.")

    def start_quiz(self):
        if not self.flashcards:
            messagebox.showwarning("No Flashcards", "Please add some flashcards first.")
            return
        self.score = 0
        self.questions_asked = 0
        self.asked_questions = []
        self.score_label.config(text="")
        self.ask_question()

    def ask_question(self):
        remaining_questions = list(set(self.flashcards.keys()) - set(self.asked_questions))
        
        if remaining_questions:
            self.current_question = random.choice(remaining_questions)
            self.question_label.config(text=self.current_question)
            self.answer_entry.delete(0, tk.END)
        else:
            self.end_quiz()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.flashcards[self.current_question].strip().lower()
        
        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done! 🎉")
        else:
            messagebox.showinfo("Wrong!", f"The correct answer was: '{self.flashcards[self.current_question]}'")
        
        self.asked_questions.append(self.current_question)
        self.questions_asked += 1
        
        self.ask_question()

    def end_quiz(self):
        self.question_label.config(text="Quiz Finished!")
        self.score_label.config(text=f"Your final score: {self.score}/{len(self.flashcards)}")
        self.answer_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
