import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = tk.Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.score_label.config(fg="white")

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        self.right_answer_image = tk.PhotoImage(file="images/right.png")
        self.right_answer_button = tk.Button(
            image=self.right_answer_image,
            bg=THEME_COLOR,
            fg=THEME_COLOR,
            highlightthickness=0,
            borderwidth=0,
            command=self.true_statement
        )
        self.right_answer_button.grid(row=2, column=0)

        self.wrong_answer_image = tk.PhotoImage(file="images/wrong.png")
        self.wrong_answer_button = tk.Button(
            image=self.wrong_answer_image,
            bg=THEME_COLOR,
            fg=THEME_COLOR,
            highlightthickness=0,
            borderwidth=0,
            command=self.false_statement
        )
        self.wrong_answer_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_answer_button.config(state="disabled")
            self.wrong_answer_button.config(state="disabled")

    def true_statement(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_statement(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

