# Import the Question class (data model for each quiz question)
from question_model import Question

# Import the question data fetched from the API
from data import question_data

# Import the quiz logic controller class
from quiz_brain import QuizBrain

# Import the GUI interface class
from ui import QuizInterface


# This list will store Question objects
question_bank = []

# Loop through the API question list (each item is a dictionary)
for question in question_data:
    
    # Extract the question text from dictionary
    question_text = question["question"]
    
    # Extract the correct answer
    question_answer = question["correct_answer"]
    
    # Create a Question object using the Question class
    new_question = Question(question_text, question_answer)
    
    # Add the Question object to the list
    question_bank.append(new_question)


# Create the quiz engine object
# This object will manage:
# - score
# - question number
# - checking answers
quiz = QuizBrain(question_bank)


# Create the GUI and pass the quiz object to it
# The UI will now communicate with QuizBrain
quiz_ui = QuizInterface(quiz)
