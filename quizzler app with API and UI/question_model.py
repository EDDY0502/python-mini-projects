# This class is a blueprint for creating Question objects
# Each Question object will store:
# - question text
# - correct answer
class Question:

    # __init__ is the constructor method
    # It runs automatically whenever a new Question object is created
    # Example:
    # q1 = Question("2+2=4?", "True")
    def __init__(self, q_text, q_answer):

        # "self" refers to the current object being created
        # It allows us to store data inside that object

        # Store the question text inside the object
        self.text = q_text

        # Store the correct answer inside the object
        self.answer = q_answer





# q1 = Question("Sky is blue?", "True")
# q2 = Question("2+2=5?", "False")



# q1.text   → "Sky is blue?"
# q1.answer → "True"

# q2.text   → "2+2=5?"
# q2.answer → "False"
