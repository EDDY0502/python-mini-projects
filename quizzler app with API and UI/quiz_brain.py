# html module is used to convert HTML entities into normal text
# Example: &quot; → "
import html


# QuizBrain class controls the quiz logic
# It keeps track of:
# - current question number
# - score
# - question list
# - checking answers
class QuizBrain:

    # Constructor method
    # Runs automatically when QuizBrain object is created
    # q_list = list of Question objects passed from main.py
    def __init__(self, q_list):

        # Tracks which question we are on
        self.question_number = 0

        # Tracks user's score
        self.score = 0

        # Stores all Question objects
        self.question_list = q_list

        # Stores the current question object
        self.current_question = None


    # Checks if there are questions remaining
    def still_has_questions(self):
        # Returns True if questions remain
        return self.question_number < len(self.question_list)


    # Loads and returns the next question
    def next_question(self):

        # Get question object from list using index
        self.current_question = self.question_list[self.question_number]

        # Move to next question index
        self.question_number += 1

        # Convert HTML characters from API
        q_text = html.unescape(self.current_question.text)

        # Return formatted question string
        return f"Q.{self.question_number}: {q_text}"


    # Checks if user's answer is correct
    def check_answer(self, user_answer):

        # Get correct answer from current question
        correct_answer = self.current_question.answer

        # Compare answers (case-insensitive)
        if user_answer.lower() == correct_answer.lower():

            # Increase score if correct
            self.score += 1

            return True
        else:
            return False








# How object state changes during quiz

# Initial state:

# question_number = 0
# score = 0


# After first question:

# question_number = 1
# score = 0 or 1


# After second question:

# question_number = 2
# score = ...