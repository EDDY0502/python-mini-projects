from tkinter import *          # For GUI
import pandas                  # For loading CSV file
import random                  # For random word selection

# Background color
BACKGROUND_COLOR = "#B1DDC6"

# Initial score and current card
score = 0
current_card = {}

# Load French words data
data = pandas.read_csv("data/french_words.csv")          # Load CSV file
to_learn = data.to_dict(orient="records")                # Convert to list of dictionaries

# Function to update the score label
def update_score():
    score_label.config(text=f"Score: {score}")           # Update score display

# Function to flip card and show English
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")              # Change title
    canvas.itemconfig(card_word, text=current_card["English"], fill="white") # Show English word
    canvas.itemconfig(card_background, image=card_back_img)                  # Show back image

# Function to show next French word
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)                                          # Cancel previous timer
    current_card = random.choice(to_learn)                                   # Choose random word
    canvas.itemconfig(card_title, text="French", fill="black")              # Set title
    canvas.itemconfig(card_word, text=current_card["French"], fill="black") # Show French word
    canvas.itemconfig(card_background, image=card_front_img)                # Show front image
    flip_timer = window.after(3000, flip_card)                               # Auto flip after 3 sec

# Function for correct answer
def is_known():
    global score
    to_learn.remove(current_card)                                            # Remove word from list
    score += 1                                                               # Add 1 point
    update_score()                                                           # Update score
    next_card()                                                              # Show next word

# Function for wrong answer
def is_unknown():
    global score
    score -= 1                                                               # Subtract 1 point
    update_score()                                                           # Update score
    next_card()                                                              # Show next word

# -------------------- UI SETUP -------------------- #
window = Tk()                                                                # Create window
window.title("Flashy")                                                       # Window title
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)                         # Padding & bg color

flip_timer = window.after(3000, flip_card)                                   # Start flip timer

canvas = Canvas(width=800, height=526)                                       # Create canvas
card_front_img = PhotoImage(file="images/card_front.png")                    # Load front image
card_back_img = PhotoImage(file="images/card_back.png")                      # Load back image
card_background = canvas.create_image(400, 263, image=card_front_img)        # Set image on canvas
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))  # Title
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))    # Word
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)                     # No border
canvas.grid(row=0, column=0, columnspan=2)                                   # Position canvas

# Score label
score_label = Label(text=f"Score: {score}", bg=BACKGROUND_COLOR, font=("Ariel", 14, "bold")) # Score display
score_label.grid(row=1, column=0, columnspan=2)                              # Position score

# Wrong button
wrong_img = PhotoImage(file="images/wrong.png")                              # Load wrong image
wrong_button = Button(image=wrong_img, command=is_unknown, highlightthickness=0)  # Wrong answer button
wrong_button.grid(row=2, column=0)                                           # Position button

# Right button
right_img = PhotoImage(file="images/right.png")                              # Load right image
right_button = Button(image=right_img, command=is_known, highlightthickness=0)   # Correct answer button
right_button.grid(row=2, column=1)                                           # Position button

# Show the first card
next_card()

# Start the app
window.mainloop()
