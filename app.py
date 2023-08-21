from flask import Flask, render_template, request
import requests

# place API key from Spoonacular
API_KEY = '7fb1b4b862af49789a3a081ddeed0187'

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])

def rec():
    if request.method == 'POST':
        min_carbs = request.form.get('min_carbs')
        max_carbs = request.form.get('max_carbs')
        min_protein = request.form.get('min_protein')
        # Endpoint URL for the Spoonacular API
        endpoint = 'https://api.spoonacular.com/recipes/findByNutrients'
        # Parameters for the recipe search
        params = {
        'minCarbs': min_carb,
        'maxCarbs': max_carbs,
        'minProtein': min_protein,
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
            recipe_details = []
            for recipe in recipes:
                recipe_info = {
                    'name': recipe['title'],
                    'calories': recipe['calories'],
                    'carbs': recipe['carbs'],
                    'protein': recipe['protein'],
                    'fat': recipe['fat']
                }
                recipe_details.append(recipe_info)

            return render_template('index.html', recipe_details=recipe_details)
        else:
            error_message = f"Failed to fetch recipes. Status code: {response.status_code}\n{response.json()}"
            return render_template('index.html', error_message=error_message)
    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run()