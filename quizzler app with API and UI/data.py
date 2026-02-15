# Import requests library to make API calls
import requests

# Parameters to send with the API request
# "amount" → number of questions to fetch
# "type" → boolean questions (True/False)
parameters = {
    "amount": 10,
    "type": "boolean",
}

# Send GET request to the Open Trivia Database API
# params automatically attaches the dictionary as URL query parameters
response = requests.get("https://opentdb.com/api.php", params=parameters)

# Raise an error if the request fails (status code not 200)
response.raise_for_status()

# Convert API JSON response into a Python dictionary
data = response.json()

# Extract the list of questions from the response
# The API response contains a "results" key with question data
question_data = data["results"]





# 3. data.py — API data

# data

# response = requests.get("https://opentdb.com/api.php", params=parameters)


# Sends HTTP request.

# response.raise_for_status()


# Stops program if API fails.

# data = response.json()


# Converts JSON → Python dictionary.

# question_data = data["results"]


# Stores list of questions.