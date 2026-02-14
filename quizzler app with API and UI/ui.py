# Import Tkinter GUI library
from tkinter import *

# Import quiz controller (logic layer)
from quiz_brain import QuizBrain

# Application theme color
THEME_COLOR = "#375362"


# GUI class responsible for rendering the quiz interface
class QuizInterface:

    # Constructor runs when QuizInterface object is created
    # Receives QuizBrain object to interact with quiz logic
    def __init__(self, quiz_brain: QuizBrain):

        # Store reference to quiz logic controller
        self.quiz = quiz_brain

        # Create main application window
        self.window = Tk()
        self.window.title("Quizzler")

        # Configure window layout and styling
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score label displayed at the top
        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR
        )
        self.score_label.grid(row=0, column=1)

        # Canvas widget used to display questions
        self.canvas = Canvas(width=300, height=250, bg="white")

        # Text element inside canvas (returns an ID)
        # This ID is later used to update question text dynamically
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        # Position canvas using grid layout
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Load button images
        # NOTE: In production, store these as self.true_image/self.false_image
        # to prevent garbage collection in Tkinter
        # Load image for the "True" button from the images folder
        # PhotoImage is the Tkinter class used to display images in widgets
        true_image = PhotoImage(file="images/true.png")

        # Create the True button
        # image → sets the button icon
        # highlightthickness=0 → removes default button border
        # command → function that runs when button is clicked
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            command=self.true_pressed
        )

        # Position the button using grid layout
        # row=2 places it below the canvas
        self.true_button.grid(row=2, column=0)

        # Load image for the "False" button
        false_image = PhotoImage(file="images/false.png")

        # Create the False button
        # When clicked, it calls false_pressed()
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            command=self.false_pressed
        )

        # Place False button next to True button
        self.false_button.grid(row=2, column=1)

        # Load the first question when the UI starts
        # This fetches the question from QuizBrain and displays it on the canvas
        self.get_next_question()

        # Start Tkinter's event loop
        # This keeps the window open and listens for user actions
        # Without mainloop(), the window would open and close immediately
        self.window.mainloop()
