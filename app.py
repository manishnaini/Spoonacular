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
        'random': False,
        'number': 10,
        'limitLicense': True,
        'offset': 0,
        'apiKey': API_KEY
    }
    # Make the API request
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        recipes = response.json()
        recipe_details = ""
        for recipe in recipes:
            recipe_details += f"Recipe Name: {recipe['title']}\n"
            recipe_details += f"Calories per Serving: {recipe['calories']}\n"
            recipe_details += f"Carbs per Serving: {recipe['carbs']}g\n"
            recipe_details += f"Protein per Serving: {recipe['protein']}g\n"
            recipe_details += f"Fat per Serving: {recipe['fat']}g\n"
            recipe_details += "\n------\n"
        return recipe_details
    else:
        return f"Failed to fetch recipes. Status code: {response.status_code}\n{response.json()}"