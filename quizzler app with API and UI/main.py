# Import the Question class (data model for each quiz question)
from question_model import Question

# Import question data fetched from the API
from data import question_data

# Import quiz logic controller class
from quiz_brain import QuizBrain

# Import GUI interface class
from ui import QuizInterface


# This list will store Question objects
question_bank = []

# Loop through the question data (each item is a dictionary)
for question in question_data:

    # Extract question text from dictionary
    question_text = question["question"]

    # Extract correct answer from dictionary
    question_answer = question["correct_answer"]

    # Create a Question object using the Question class
    new_question = Question(question_text, question_answer)

    # Add the Question object to the question_bank list
    question_bank.append(new_question)


# Create the QuizBrain object
# This object manages quiz logic like:
# - question flow
# - score tracking
# - answer checking
quiz = QuizBrain(question_bank)


# Create the QuizInterface object (GUI)
# Pass the quiz object so UI can interact with quiz logic
quiz_ui = QuizInterface(quiz)




#API data → Question objects → QuizBrain → QuizInterface





# (Controls the whole app)

# main

# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain
# from ui import QuizInterface


# These are imports:

# Question → blueprint for question objects

# question_data → API questions

# QuizBrain → quiz logic controller

# QuizInterface → GUI

# Creating objects from API data
# question_bank = []


# A list to store Question objects.

# for question in question_data:


# Loop through API data.

# question_text = question["question"]
# question_answer = question["correct_answer"]


# Extract values from dictionary.

# Example:

# {
#  "question": "...",
#  "correct_answer": "True"
# }

# new_question = Question(question_text, question_answer)


# This creates an object from the Question class.

# This calls:

# Question.__init__()

# question_bank.append(new_question)


# Adds the object to the list.

# quiz = QuizBrain(question_bank)


# Creates the quiz engine object.

# quiz_ui = QuizInterface(quiz)


# Starts the GUI.

# This is where the app actually runs.