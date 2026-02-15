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






# What self means (important)

# Think of self as "this object".

# Example:

# q1 = Question("Sky is blue?", "True")
# q2 = Question("2+2=5?", "False")


# Memory looks like this:

# q1.text   → "Sky is blue?"
# q1.answer → "True"

# q2.text   → "2+2=5?"
# q2.answer → "False"


# Each object stores its own data.

# What __init__ does

# __init__ is called automatically when an object is created.

# Example:

# Question("Hello", "True")


# Python internally does:

# create empty object
# call __init__()
# store values using self

# Real-life analogy

# Think of Question like a form template.

# Template:

# Question
# - text
# - answer


# Objects created from template:

# Question 1 → "HTML stands for...?"
# Question 2 → "Python is compiled?"

# Why this class exists

# Without the class, you'd use dictionaries everywhere:

# question["question"]
# question["correct_answer"]


# With OOP:

# question.text
# question.answer


# Cleaner and easier to manage.