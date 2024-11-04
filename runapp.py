from flask import Flask, render_template, request
import requests
import csv
import os.path
from keys import app_id, app_key

app = Flask(__name__)

def recipe_search(ingredient, health_filter=None):
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'
    if health_filter:
        for health in health_filter:
            url += f'&health={health}'
    result = requests.get(url)
    data = result.json()
    return data['hits']

@app.route('/')
def index():
    return render_template('index.html')
    result = requests.get(url)
    data = result.json()
    return data['hits']

@app.route('/search', methods=['POST'])
def search():
    ingredient = request.form['ingredient']
    diet = request.form.getlist('diet')
    results = recipe_search(ingredient, diet)
    recipes = []
    for result in results[:10]:  # Get the first 10 recipes
        recipe = result['recipe']
        recipes.append({
            'label': recipe['label'],
            'url': recipe['url'],
            'ingredients': recipe['ingredientLines'],
            'calories': recipe['totalNutrients']['ENERC_KCAL']['quantity'],
            'mealType': recipe['mealType']
        })
    return render_template('results.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)
