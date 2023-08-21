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
        max_protein = request.form.get('max_protein')
        min_calories = request.form.get('min_calories')
        max_calories = request.form.get('max_calories')
        min_fat = request.form.get('min_fat')
        max_fat = request.form.get('max_fat')
        # Endpoint URL for the Spoonacular API
        endpoint = 'https://api.spoonacular.com/recipes/findByNutrients'
            # Parameters for the recipe search
        params = {
            'minCarbs': min_carbs,
            'maxCarbs': max_carbs,
            'minProtein': min_protein,
            'maxProtein':  max_protein,
            'minCalories': min_calories,
            'maxCalories': max_calories,
            'minFat': min_fat,
            'maxFat': max_fat,
            'offset': 0,
            'number': 10,
            'random': False,
            'limitLicense': True,
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