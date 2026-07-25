import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 179
AGE = 22

APP_ID = "app_f0f9dddb397f4f6595207152"
API_KEY = "nix_live_jqWseuVeupBnWqK055dkeOL4RXn34KZW"

exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
# Use the actual Sheety API URL shown in the dashboard, not the dashboard page URL.
sheet_endpoint = "https://api.sheety.co/bcb40a8fd56f96d80be63649d6239d45/nutritionAndExerciseApi/workouts"
exercise_text = input("Tell me which exercises you did:  {e.g. ran 3 miles and swam for 30 minutes} ")

headers = {
    "x-app-id": "app_f0f9dddb397f4f6595207152",
    "x-app-key": "nix_live_jqWseuVeupBnWqK055dkeOL4RXn34KZW",
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)