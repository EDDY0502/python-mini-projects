import requests # to make API calls
from twilio.rest import Client # to send SMS notifications # Twilio is a cloud communications platform that allows you to send SMS messages, make phone calls, and perform other communication tasks programmatically. The Client class from the twilio.rest module is used to interact with the Twilio API and send SMS notifications.

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query" # API endpoint for Alpha Vantage stock data, Alpha Vantage is a financial data provider that offers a wide range of APIs for accessing stock market data, including stock prices, technical indicators, and more. The STOCK_ENDPOINT is the URL that you will use to make API calls to Alpha Vantage and retrieve stock market data for the specified stock symbol (in this case, TSLA). This endpoint allows you to access various types of stock data, such as daily time series data, intraday data, and more, depending on the parameters you include in your API request.
NEWS_ENDPOINT = "https://newsapi.org/v2/everything" # API endpoint for NewsAPI.org, NewsAPI.org is a news aggregator service that provides access to news articles from various sources through its API. The NEWS_ENDPOINT is the URL that you will use to make API calls to NewsAPI.org and retrieve news articles related to the specified company (in this case, Tesla Inc). This endpoint allows you to access a wide range of news articles from different sources, and you can specify parameters such as the query term (e.g., company name), language, sort order, and more to filter the news articles returned by the API.

STOCK_API_KEY = "AGGQF4IVXZJD4926" # Stock API key for Alpha Vantage , alpha vantage is a financial data provider that offers a wide range of APIs for accessing stock market data, including stock prices, technical indicators, and more. The STOCK_API_KEY is a unique identifier that allows you to authenticate your API requests and access the stock market data provided by Alpha Vantage. It is typically stored as an environment variable for security reasons, so that it is not hardcoded in the code and can be easily changed without modifying the code itself. In this code, it is accessed using os.environ["STOCK_API_KEY"], which retrieves the value of the STOCK_API_KEY environment variable. This key is necessary to make API calls to Alpha Vantage and retrieve stock market data for the specified stock symbol (in this case, TSLA).
NEWS_API_KEY = "227a4e152a934beaa451a209b372aa56" # News API key for NewsAPI.org, NewsAPI.org is a news aggregator service that provides access to news articles from various sources through its API. The NEWS_API_KEY is a unique identifier that allows you to authenticate your API requests and access the news data provided by NewsAPI.org. It is typically stored as an environment variable for security reasons, so that it is not hardcoded in the code and can be easily changed without modifying the code itself. In this code, it is accessed using os.environ["NEWS_API_KEY"], which retrieves the value of the NEWS_API_KEY environment variable. This key is necessary to make API calls to NewsAPI.org and retrieve news articles related to the specified company (in this case, Tesla Inc).

TWILIO_SID  = "ACdae91d08f7d4818fb16004ba39c88f6c5" # account_sid is a unique identifier for your Twilio account. It is used to authenticate API requests and identify your account when interacting with the Twilio API. Like the auth_token, it is typically stored as an environment variable for security reasons, so that it is not hardcoded in the code and can be easily changed without modifying the code itself. In this code, it is accessed using os.environ["TWILIO_ACCOUNT_SID"], which retrieves the value of the TWILIO_ACCOUNT_SID environment variable.
TWILIO_AUTH_TOKEN = "99c1aa07257fd6160c88b56e7e490bb15" # auth_token is a secret key associated with your Twilio account that is used for authentication when making API requests to the Twilio service. It is a string of characters that should be kept secure and not shared publicly, as it grants access to your Twilio account and allows you to perform actions such as sending SMS messages. Like the account_sid, it is typically stored as an environment variable for security reasons, so that it is not hardcoded in the code and can be easily changed without modifying the code itself. In this code, it is accessed using os.environ["TWILIO_AUTH_TOKEN"], which retrieves the value of the TWILIO_AUTH_TOKEN environment variable.0

    ##  Useing https://www.alphavantage.co/documentation/#daily



#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]



stock_params = {  # this is a dictionary that contains the parameters for the API call to the Alpha Vantage API. It specifies the function to be called (TIME_SERIES_DAILY), the stock symbol (STOCK_NAME), and the API key (STOCK_API_KEY) required for authentication. This dictionary will be passed as query parameters in the API request to retrieve the daily stock market data for the specified stock symbol (in this case, TSLA).
    "function":"TIME_SERIES_DAILY", # This parameter specifies the type of data you want to retrieve from the Alpha Vantage API. In this case, "TIME_SERIES_DAILY" indicates that you want to retrieve daily time series data for the specified stock symbol (STOCK_NAME). This will return historical stock price data for each day, including the opening price, closing price, high price, low price, and volume for each trading day.
    "symbol": STOCK_NAME, # This parameter specifies the stock symbol for which you want to retrieve data from the Alpha Vantage API. In this case, STOCK_NAME is a variable that holds the value "TSLA", which represents the stock symbol for Tesla Inc. By including this parameter in the API request, you are telling the Alpha Vantage API to return data specifically for the TSLA stock.
    "apikey": STOCK_API_KEY # This parameter is used to authenticate your API request to the Alpha Vantage API. It is a unique key that you receive when you sign up for an account with Alpha Vantage. By including this parameter in your API request, you are providing the necessary credentials to access the stock market data provided by Alpha Vantage. It is important to keep this key secure and not share it publicly, as it grants access to your account and allows you to retrieve data from the API.
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)  # This line of code makes a GET request to the Alpha Vantage API using the requests library. It sends the API request to the specified STOCK_ENDPOINT URL, along with the parameters defined in the stock_params dictionary. The response from the API is stored in the variable response. The params argument is used to pass the query parameters for the API request, which include the function, symbol, and API key required for authentication. After this line of code is executed, you can access the data returned by the API through the response variable, which contains information about the stock market data for the specified stock symbol (TSLA).
data = response.json()["Time Series (Daily)"] # This line of code extracts the JSON data from the API response and accesses the "Time Series (Daily)" key to retrieve the daily stock market data. The response.json() method converts the API response into a Python dictionary, and then the ["Time Series (Daily)"] key is used to access the specific data related to daily stock prices. The resulting data variable will contain a dictionary where each key represents a date and the corresponding value contains information about the stock price for that date, such as opening price, closing price, high price, low price, and volume.
data_list = [value for (key, value) in data.items()] # This line of code uses a list comprehension to create a list called data_list that contains the values from the data dictionary. The data dictionary is structured with dates as keys and stock price information as values. By iterating through the items of the data dictionary using data.items(), we can access both the key (date) and value (stock price information) for each entry. The list comprehension extracts only the values (stock price information) and creates a new list called data_list that contains all the stock price information for each date. This allows us to easily access and manipulate the stock price data without needing to reference the specific dates.#.items() is a method that returns a view object containing the key-value pairs of the dictionary, which allows us to iterate through both the keys and values in a single loop.
yesterday_data = data_list[0] # This line of code assigns the first element of the data_list to the variable yesterday_data. Since data_list is a list that contains the stock price information for each date, the first element (index 0) corresponds to the most recent date, which is typically considered as "yesterday" in the context of stock market data. By assigning this value to yesterday_data, we can easily access and work with the stock price information for that specific date.
yesterday_closing_price = yesterday_data["4. close"] # This line of code extracts the closing price from the yesterday_data dictionary. The yesterday_data variable contains the stock price information for a specific date, and the key "4. close" is used to access the closing price for that date. By assigning this value to yesterday_closing_price, we can easily access and work with the closing price for that specific date, which is often used in stock market analysis to track the performance of a stock over time. The closing price represents the final price at which the stock was traded on that day, and it is commonly used as a reference point for evaluating the stock's performance and making investment decisions.

#Get the day before yesterday's closing price



day_before_yesterday_data = data_list[1] # This line of code assigns the second element of the data_list to the variable day_before_yesterday_data. Since data_list is a list that contains the stock price information for each date, the second element (index 1) corresponds to the date before yesterday. By assigning this value to day_before_yesterday_data, we can easily access and work with the stock price information for that specific date, which is often used in stock market analysis to compare the performance of a stock over multiple days.
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"] # This line of code extracts the closing price from the day_before_yesterday_data dictionary. The day_before_yesterday_data variable contains the stock price information for a specific date, and the key "4. close" is used to access the closing price for that date. By assigning this value to day_before_yesterday_closing_price, we can easily access and work with the closing price for that specific date, which is often used in stock market analysis to track the performance of a stock over time. The closing price represents the final price at which the stock was traded on that day, and it is commonly used as a reference point for evaluating the stock's performance and making investment decisions. By comparing the closing prices of yesterday and the day before yesterday, we can analyze the stock's price movement and determine if there has been a significant change in the stock's value.




#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.




difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)) # This line of code calculates the positive difference between yesterday's closing price and the day before yesterday's closing price. The abs() function is used to ensure that the result is always a positive value, regardless of whether yesterday's closing price is higher or lower than the day before yesterday's closing price. By converting the closing prices to floats, we can perform mathematical operations on them to calculate the difference. The resulting difference variable will contain the absolute value of the difference between the two closing prices, which can be used for further analysis or comparisons in stock market analysis. #abs is a built-in Python function that returns the absolute value of a number, which is the non-negative value of the number without regard to its sign. In this case, it ensures that the difference between the two closing prices is always positive, regardless of whether yesterday's closing price is higher or lower than the day before yesterday's closing price. This allows us to focus on the magnitude of the change in stock price rather than the direction of the change. 

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price) # This line of code calculates the difference between yesterday's closing price and the day before yesterday's closing price. By converting the closing prices to floats, we can perform mathematical operations on them to calculate the difference. The resulting difference variable will contain the value of the change in stock price between the two days, which can be used for further analysis or comparisons in stock market analysis. By analyzing the difference, investors can assess whether there has been an increase or decrease in the stock price, which may influence their investment strategies or decisions.
up_down = None # This line of code initializes a variable called up_down to None. This variable will be used to indicate whether the stock price has gone up or down based on the calculated difference between yesterday's closing price and the day before yesterday's closing price. By setting it to None initially, we can later update it to either "🔺" (indicating an increase) or "🔻" (indicating a decrease) based on the value of the difference variable. This allows us to visually represent the direction of the stock price change in our output or analysis.
if difference > 0:
    up_down = "🔺" # This line of code sets the up_down variable to "🔺" if the calculated difference between yesterday's closing price and the day before yesterday's closing price is greater than 0. This indicates that the stock price has gone up, and the "🔺" symbol is used to visually represent this increase in stock price. By setting up_down to "🔺", we can later use this variable in our output or analysis to indicate that the stock price has experienced an upward movement.
else:
    up_down = "🔻" # This line of code sets the up_down variable to "🔻" if the calculated difference between yesterday's closing price and the day before yesterday's closing price is not greater than 0 (i.e., it is less than or equal to 0). This indicates that the stock price has either gone down or remained the same, and the "🔻" symbol is used to visually represent this decrease or lack of change in stock price. By setting up_down to "🔻", we can later use this variable in our output or analysis to indicate that the stock price has experienced a downward movement or has not changed.




#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.



diff_percentage = round(difference / float(yesterday_closing_price)) * 100 # This line of code calculates the percentage difference in price between yesterday's closing price and the day before yesterday's closing price. It divides the absolute difference (calculated in the previous step) by yesterday's closing price and multiplies the result by 100 to convert it to a percentage. The resulting diff_percentage variable will contain the percentage change in stock price between the two days, which can be used to evaluate the magnitude of the change in stock value and make informed decisions based on that information. By analyzing the percentage difference, investors can assess whether there has been a significant increase or decrease in the stock price, which may influence their investment strategies or decisions.





#If TODO4 percentage is greater than 5 then print("Get News").
#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.



if abs(diff_percentage) > 1:
    newa_params = {
        "apiKey": NEWS_API_KEY, # This parameter is used to authenticate your API request to the NewsAPI.org service. It is a unique key that you receive when you sign up for an account with NewsAPI.org. By including this parameter in your API request, you are providing the necessary credentials to access the news data provided by NewsAPI.org. It is important to keep this key secure and not share it publicly, as it grants access to your account and allows you to retrieve news articles from the API.
        "qInTitle": COMPANY_NAME, # This parameter is used to specify the query term for searching news articles in the NewsAPI.org service. By setting "qInTitle" to COMPANY_NAME, you are instructing the API to return news articles that have the company name (in this case, Tesla Inc) in the title of the article. This allows you to filter the news articles to only those that are relevant to the specified company, which can be useful for tracking news and updates related to that company.
    }
    new_response = requests.get(NEWS_ENDPOINT, params=newa_params) # This line of code makes a GET request to the NewsAPI.org API using the requests library. It sends the API request to the specified NEWS_ENDPOINT URL, along with the parameters defined in the newa_params dictionary. The response from the API is stored in the variable new_response. The params argument is used to pass the query parameters for the API request, which include the API key for authentication and the query term for searching news articles. After this line of code is executed, you can access the data returned by the API through the new_response variable, which contains information about the news articles related to the specified company (Tesla Inc) that match the query criteria.
    articles = new_response.json()["articles"] # This line of code extracts the JSON data from the API response and accesses the "articles" key to retrieve the list of news articles. The new_response.json() method converts the API response into a Python dictionary, and then the ["articles"] key is used to access the specific data related to the news articles. The resulting articles variable will contain a list of dictionaries, where each dictionary represents an individual news article with its associated information such as title, description, source, etc. This allows you to easily access and manipulate the news article data returned by the NewsAPI.org API for further analysis or processing.


 


 
#Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation




three_articles = new_response.json()["articles"][:3] # This line of code uses the Python slice operator to create a list called three_articles that contains the first 3 articles from the news data returned by the NewsAPI.org API. The new_response.json() method converts the API response into a Python dictionary, and then the ["articles"] key is used to access the list of articles in the response. By using the slice operator [:3], we can extract only the first 3 articles from the list, which allows us to focus on a smaller subset of news articles for further analysis or processing. The resulting three_articles variable will contain a list of dictionaries, where each dictionary represents an individual news article with its associated information such as title, description, source, etc.
print(three_articles) # This line of code prints the list of the first 3 articles that were extracted from the news data returned by the NewsAPI.org API. By printing this list, you can review the details of each article, such as the title, description, source, and other relevant information. This allows you to analyze the news articles and extract insights or make informed decisions based on the content of the articles related to the specified company (Tesla Inc) and its stock performance.







#Create a new list of the first 3 article's headline and description using list comprehension.



formated_articles=[f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles] # This line of code uses a list comprehension to create a new list called formated_articles that contains formatted strings for each of the first 3 articles. The list comprehension iterates through each article in the three_articles list and constructs a formatted string for each article using an f-string. The formatted string includes the stock symbol (STOCK_NAME), the up/down symbol (up_down), the percentage difference (diff_percentage), the headline of the article (article['title']), and a brief description of the article (article['description']). By creating this new list of formatted articles, you can easily access and display the relevant information about each article in a concise and organized format, which can be useful for analyzing the news content related to the specified company (Tesla Inc) and its stock performance.

print(formated_articles) # This line of code prints the list of formatted articles that were created using the list comprehension in the previous line. By printing this list, you can review the formatted strings that contain the headline and description of each article in a concise format. This allows you to easily read and analyze the relevant information from the news articles related to the specified company (Tesla Inc) and its stock performance, which can be useful for making informed decisions or gaining insights based on the news content.


 





#Send each article as a separate message via Twilio. 



client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN) # This line of code creates an instance of the Client class from the Twilio library, using the TWILIO_SID and TWILIO_AUTH_TOKEN as parameters for authentication. The Client class is used to interact with the Twilio API and perform various actions, such as sending SMS messages. By creating an instance of the Client class, you can use it to send messages through the Twilio service by calling the appropriate methods and providing the necessary parameters, such as the recipient's phone number and the message content.

message = client.messages.create( # This line of code uses the create() method of the messages attribute of the Client instance to send an SMS message through the Twilio API. The create() method takes several parameters, including the body of the message, the sender's phone number (from_), and the recipient's phone number (to). By calling this method with the appropriate parameters, you can send an SMS message containing the formatted article information to a specified phone number using the Twilio service.
    body=articles, # This parameter specifies the content of the SMS message that you want to send through the Twilio API. In this case, the body parameter is set to article, which represents the formatted string containing the headline and description of a news article. By setting the body parameter to article, you are instructing the Twilio API to include the formatted article information in the SMS message that will be sent to the recipient's phone number. This allows you to share the relevant news article information with others via SMS, which can be useful for keeping them informed about the stock performance and news related to the specified company (Tesla Inc).
    from_="+16813456896", # This parameter specifies the sender's phone number that will be used to send the SMS message through the Twilio API. The from_ parameter is set to a specific phone number (in this case, "+15017122661"), which represents the phone number associated with your Twilio account that will be used as the sender of the SMS message. By providing this parameter, you are instructing the Twilio API to use the specified phone number as the sender when sending the SMS message to the recipient's phone number. It is important to ensure that the phone number provided in the from_ parameter is a valid and active phone number associated with your Twilio account, as it will be used to send the SMS message and may incur costs based on your Twilio account plan and usage.
    to="+919667771633" # This parameter specifies the recipient's phone number that will receive the SMS message sent through the Twilio API. The to parameter is set to a specific phone number (in this case, "+15558675310"), which represents the phone number of the intended recipient of the SMS message. By providing this parameter, you are instructing the Twilio API to send the SMS message to the specified recipient's phone number. It is important to ensure that the phone number provided in the to parameter is a valid and active phone number that can receive SMS messages, as it will be the destination for the SMS message containing the formatted article information. Additionally, it is important to consider any applicable regulations or restrictions regarding sending SMS messages to certain phone numbers or regions, and to ensure that you have the necessary permissions to send messages to the specified recipient's phone number.
)