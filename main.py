from flask import Flask, render_template, request
import requests
import csv
import os.path
from keys import app_id, app_key # Import API keys stored securely in keys.py

# Initialize Flask application
app = Flask(__name__)

def recipe_search(ingredient, health_filter=None):
    # Construct the base URL for the Edamam API request
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'
     # Add dietary filters to the URL if provided
    if health_filter:
        for health in health_filter:
            url += f'&health={health}'
      # Send GET request to the API
    result = requests.get(url)
    data = result.json() # Parse the JSON response
    return data['hits']
     # Process and filter the recipes from the response
    for result in data['hits']:
        recipe = result['recipe']
        # Check if all dietary filters match the recipe's health labels
        if health_filters:  # Check if recipe matches the selected filters
            if not all(health in recipe.get('healthLabels', []) for health in health_filters):
                continue  # Skip recipes that do not match all health filters
        filtered_recipes.append({
            'label': recipe['label'],
            'url': recipe['url'],
            'ingredients': recipe['ingredientLines'],
            'calories': round(recipe['totalNutrients']['ENERC_KCAL']['quantity']),  # Round calories
            'mealType': recipe.get('mealType', []),
            'healthLabels': recipe.get('healthLabels', []),  # Include health labels
        })
    return filtered_recipes
@app.route('/')
def index():
    return render_template('index.html')
    result = requests.get(url)
    data = result.json()
    return data['hits']

@app.route('/search', methods=['POST'])
def search():
    # Get the ingredients and format them for the API
    ingredient = request.form['ingredient']
    ingredient = ','.join(ingredient.replace(' ', ',').split(',')) # Handle spaces and commas in input
    diet = request.form.getlist('diet')
    results = recipe_search(ingredient, diet)
    recipes = []
    for result in results[:10]:  # Get the first 10 recipes
        recipe = result['recipe']
        recipes.append({
            'label': recipe['label'],
            'url': recipe['url'],
            'ingredients': recipe['ingredientLines'],
            'calories': round(recipe['totalNutrients']['ENERC_KCAL']['quantity']),
            'mealType': recipe['mealType'],
            'healthLabels': recipe['healthLabels'],
        })
    # Render the results page with the fetched recipes
    return render_template('results.html', recipes=recipes)

if __name__ == '__main__':
     # Run the Flask app in debug mode for development
    app.run(debug=True)
