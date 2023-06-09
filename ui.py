THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
from tkinter import *

class QuizInterface:
    
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300,height=250,highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width= 280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",20,"italic")
        )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.score_label = Label(text = "Score: 0", fg="White",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.get_next_question()

        
        
        #Buttons
        true_img = PhotoImage(file="images/true.png")
        correct_btn = Button(image=true_img, highlightthickness=0,command=self.true_pressed)
        correct_btn.grid(row=2,column=0)
        
        false_img = PhotoImage(file="images/false.png")
        false_btn = Button(image=false_img, highlightthickness=0,command=self.false_pressed)
        false_btn.grid(row=2,column=1)
        
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
            #self.quiz.check_answer(self, answer)
        else:
            self.canvas.itemconfig(self.question_text,text = f"You've reached the end of the quiz. Your score was {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.config(bg="white")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}", fg="White", bg=THEME_COLOR)
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)

