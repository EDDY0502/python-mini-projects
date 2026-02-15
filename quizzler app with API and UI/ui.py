# Import everything from the Tkinter library
# Tkinter is Python’s built-in GUI toolkit used to create desktop applications
from tkinter import *

# Import QuizBrain class (handles quiz logic like questions, score, etc.)
from quiz_brain import QuizBrain

# Constant used to maintain consistent UI theme color
THEME_COLOR = "#375362"


# QuizInterface class is responsible for the graphical user interface (GUI)
# It displays questions, buttons, score, and feedback
class QuizInterface:

    # Constructor method
    # Runs automatically when a QuizInterface object is created
    # quiz_brain is the QuizBrain object passed from main.py
    def __init__(self, quiz_brain: QuizBrain):

        # Store the QuizBrain object inside this UI object
        # This allows UI methods to call quiz logic methods
        self.quiz = quiz_brain

        # Create the main application window
        # Tk() initializes the GUI application
        self.window = Tk()

        # Set window title
        self.window.title("Quizzler")

        # Configure window padding and background color
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Create label widget to display score
        self.score_label = Label(
            text="Score: 0",      # Initial text
            fg="white",           # Text color
            bg=THEME_COLOR        # Background color
        )

        # Place score label in grid layout
        self.score_label.grid(row=0, column=1)

        # Create canvas widget for displaying question text
        self.canvas = Canvas(width=300, height=250, bg="white")

        # Create text element inside canvas
        # create_text returns an object ID used to update text later
        self.question_text = self.canvas.create_text(
            150,        # x-coordinate (center horizontally)
            125,        # y-coordinate (center vertically)
            width=280,  # text wrapping width
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        # Place canvas in window using grid layout
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Load image for True button
        # PhotoImage is required to display images in Tkinter
        true_image = PhotoImage(file="quizzler app with API and UI/images/true.png")

        # Create True button widget
        # command defines which function runs when button is clicked
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            command=self.true_pressed
        )

        # Place True button in grid
        self.true_button.grid(row=2, column=0)

        # Load image for False button
        false_image = PhotoImage(file="quizzler app with API and UI/images/false.png")

        # Create False button widget
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            command=self.false_pressed
        )

        # Place False button in grid
        self.false_button.grid(row=2, column=1)

        # Load the first question when UI starts
        self.get_next_question()

        # Start Tkinter event loop
        # Keeps the application running and listening for events
        self.window.mainloop()


    # Method to load and display the next question
    def get_next_question(self):

        # Reset canvas background color after feedback
        self.canvas.config(bg="white")

        # Check if quiz still has questions
        if self.quiz.still_has_questions():

            # Update score label text
            self.score_label.config(text=f"Score: {self.quiz.score}")

            # Get next question text from QuizBrain
            q_text = self.quiz.next_question()

            # Update canvas text using itemconfig
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            # If quiz is finished, display completion message
            self.canvas.itemconfig(
                self.question_text,
                text=f"Quiz Complete!\nYour Score: {self.quiz.score}"
            )

            # Disable buttons to prevent further clicks
            self.true_button.config(state="Disabled")
            self.false_button.config(state="Disabled")


    # Function called when True button is clicked
    def true_pressed(self):

        # Check answer using QuizBrain and show feedback
        self.give_feedback(self.quiz.check_answer("True"))


    # Function called when False button is clicked
    def false_pressed(self):

        # Store result of answer check
        is_right = self.quiz.check_answer("False")

        # Show feedback color
        self.give_feedback(is_right)


    # Shows feedback color and schedules next question
    def give_feedback(self, is_right):

        # If answer is correct → green background
        if is_right:
            self.canvas.config(bg="green")

        # If answer is wrong → red background
        else:
            self.canvas.config(bg="red")

        # Wait 1000 milliseconds (1 second) before next question
        self.window.after(1000, self.get_next_question)



















# Method explanations
# get_next_question()
# def get_next_question(self):


# Loads the next question from QuizBrain.

# self.canvas.config(bg="white")


# Reset background after feedback.

# if self.quiz.still_has_questions():


# Ask QuizBrain if quiz continues.

# self.score_label.config(text=f"Score: {self.quiz.score}")


# Update score display.

# q_text = self.quiz.next_question()


# Get next question string.

# self.canvas.itemconfig(self.question_text, text=q_text)


# Update canvas text.

# End of quiz
# else:


# No questions remaining.

# self.true_button.config(state="disabled")
# self.false_button.config(state="disabled")


# Disable buttons.

# Button handlers

# These functions run when buttons are clicked.

# def true_pressed(self):


# Triggered by True button.

# self.quiz.check_answer("True")


# Calls QuizBrain.

# give_feedback()

# This shows green/red feedback.

# def give_feedback(self, is_right):

# self.canvas.config(bg="green")


# Correct answer.

# self.canvas.config(bg="red")


# Wrong answer.

# self.window.after(1000, self.get_next_question)


# Wait 1 second, then load next question.

# This is event scheduling in Tkinter.

# How OOP works’ here

# Your UI object communicates with QuizBrain object.

# Relationship:

# QuizInterface → QuizBrain → Question


# UI never handles quiz logic directly.

# That’s separation of concerns, which is very important in software design.

# One important improvement

# To avoid images disappearing:

# self.true_image = PhotoImage(file="images/true.png")
# self.false_image = PhotoImage(file="images/false.png")


# Tkinter requires persistent references.