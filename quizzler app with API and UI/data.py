import requests
# requests library is used to make HTTP/API calls in Python

# These are query parameters sent to the API
parameters = {
    "amount": 10,      # number of questions to fetch
    "type": "boolean", # True/False type questions
}

# Send a GET request to the Open Trivia Database API
# The params argument automatically converts the dictionary
# into URL query parameters
response = requests.get("https://opentdb.com/api.php", params=parameters)

# If the request fails (like 404, 500, etc.), this line
# will stop the program and raise an error
response.raise_for_status()

# Convert JSON response into a Python dictionary
data = response.json()

# Extract the list of questions from the API response
# The API returns:
# {
#   "response_code": 0,
#   "results": [ ...questions... ]
# }
question_data = data["results"]



# Flow
# requests.get()
#       ↓
# response.json()
#       ↓
# data["results"]
#       ↓
# question_data
