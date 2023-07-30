from flask import Flask
import requests

# place API key from Spoonacular
API_KEY = '7fb1b4b862af49789a3a081ddeed0187'

app = Flask('Flask')

@app.route("/")
def rec():
    # Endpoint URL for the Spoonacular API
    endpoint = 'https://api.spoonacular.com/recipes/findByNutrients'
    # Parameters for the recipe search
    params = {
        'minCarbs': 10,
        'maxCarbs': 100,
        'minProtein': 10,
        'maxProtein': 100,
        'minCalories': 50,
        'maxCalories': 800,
        'minFat': 1,
        'maxFat': 100,
        'number': 10,
        'offset': 0,
        'apiKey': API_KEY
    }
    response = requests.get(endpoint, params=params)
    return response.json()