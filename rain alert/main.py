import requests # to make API calls
import os # to access environment variables # The os module in Python provides a way to interact with the operating system, allowing you to access environment variables, read and write files, and perform other operating system-related tasks. In this code, it is used to access environment variables that may contain sensitive information such as API keys or account credentials for services like Twilio.
from twilio.rest import Client # to send SMS notifications # Twilio is a cloud communications platform that allows you to send SMS messages, make phone calls, and perform other communication tasks programmatically. The Client class from the twilio.rest module is used to interact with the Twilio API and send SMS notifications.

OWM_Endpoint ="https://api.openweathermap.org/data/2.5/forecast" # API endpoint for weather forecast data
api_key= "ddd4ffb13405f5f63ba20633f8b2eaef5" # API key for OpenWeatherMap (replace with your own API key) 

account_sid = "ACdae91d08f7d4818fb16004ba39c88f6c5" # account_sid is a unique identifier for your Twilio account. It is used to authenticate API requests and identify your account when interacting with the Twilio API. Like the auth_token, it is typically stored as an environment variable for security reasons, so that it is not hardcoded in the code and can be easily changed without modifying the code itself. In this code, it is accessed using os.environ["TWILIO_ACCOUNT_SID"], which retrieves the value of the TWILIO_ACCOUNT_SID environment variable.
auth_token = "99c1aa07257fd6160c88b56e7e490bb15" # auth_token is a secret key associated with your Twilio account that is used for authentication when making API requests to the Twilio service. It is a string of characters that should be kept secure and not shared publicly, as it grants access to your Twilio account and allows you to perform actions such as sending SMS messages. Like the account_sid, it is typically stored as an environment variable for security reasons, so that it is not hardcoded in the code and can be easily changed without modifying the code itself. In this code, it is accessed using os.environ["TWILIO_AUTH_TOKEN"], which retrieves the value of the TWILIO_AUTH_TOKEN environment variable.0

weather_params = { # parameters for the API call
    "lat": 28.643492, # latitude for the location (replace with your desired latitude)
    "lon": 77.320442, # longitude for the location (replace with your desired longitude)
    "appid": api_key, # API key for authentication
    "cnt":4, # number of forecast data points to retrieve (e.g., 4 for the next 4 time intervals)
}

response = requests.get(OWM_Endpoint,weather_params) # make the API call to get weather data
response.raise_for_status() # check for any errors in the API response (raises an exception if there was an error)
print(response.status_code) # print the status code of the response #statis code is object that contains the status code of the response, which indicates whether the API call was successful or if there was an error. A status code of 200 indicates a successful API call, while other codes may indicate various types of errors (e.g., 404 for not found, 500 for server error, etc.).

weather_data = response.json() # store the JSON response from the API #.json() is a method that converts the response from the API into a JSON format, which is a structured format for representing data. This allows you to easily access and manipulate the weather data returned by the API.

print(weather_data["list"][0]["weather"][0]["id"]) #list will give you the list of weather data for the next 4 time intervals,[0] will give you the first time interval,["weather"][0] will give you the weather information for that time interval, and ["id"] will give you the specific weather condition code. This code can be used to determine if it is going to rain or not based on the weather conditions returned by the API.

will_rain = False # initialize a variable to track whether it will rain or not // this variable will be used to keep track of whether rain is expected in the forecast. It is initially set to False, and will be updated to True if any of the weather condition codes indicate rain.

for hour_data in weather_data["list"]: # loop through the list of weather data for each time interval // this will allow you to check the weather conditions for each time interval and determine if it is going to rain or not.
    condition_code= hour_data["weather"][0]["id"] # get the weather condition code for the current time interval // this code can be used to determine if it is going to rain or not based on the weather conditions returned by the API. 

    if int(condition_code) < 700: # check if the condition code indicates rain (codes less than 700 typically indicate rain or precipitation) // this condition checks if the weather condition code is less than 700, which typically indicates that it is going to rain or there is some form of precipitation. If this condition is true, it means that rain is expected in the forecast.
        
        will_rain = True # if it is going to rain, set the will_rain variable to True // this updates the will_rain variable to True, indicating that rain is expected in the forecast.
if will_rain: # if the will_rain variable is True, print a message indicating that rain is expected // this condition checks if the will_rain variable is True, which means that rain is expected in the forecast. If this condition is true, it will print a message to alert the user about the expected rain.
    client = Client(account_sid, auth_token) # create a Twilio client using the account SID and authentication token // this creates an instance of the Twilio Client class, which allows you to interact with the Twilio API and send SMS notifications. The account_sid and auth_token are used to authenticate the client and authorize it to make API calls on behalf of your Twilio account.
    message = client.messages \
        .create( # create a new message using the Twilio client // this creates a new message object using the Twilio client. The parameters for the message include the body of the message, the sender's phone number (from_), and the recipient's phone number (to). The body of the message contains the alert about the expected rain, and the from_ and to parameters specify the sender and recipient of the SMS notification.
        body="Its going to rain today. Remember to take an umbrella ☔", # the content of the message that will be sent to the recipient, which in this case is an alert about the expected rain and a reminder to take an umbrella.
        from_="+16813456896", # the phone number that will be used as the sender of the SMS notification. This should be a valid phone number associated with your Twilio account.
        to="+9196677716335", # the phone number of the recipient who will receive the SMS notification. This should be a valid phone number that you want to send the alert to.
    )
        
    print(message.status) # this will print the status of the message sent through Twilio, which can indicate whether the message was successfully sent or if there were any issues with the delivery.