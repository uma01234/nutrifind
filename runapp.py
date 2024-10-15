from flask import Flask, render_template, request
import requests
import csv
import os.path

app = Flask(__name__)

def recipe_search(ingredient, health_filter=None):
    app_id = '5f32bfc8'
    app_key = '7c0257f762ecb139bb7c86d26c8e6ec6'
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={app_id}&app_key={app_key}'
    if health_filter:
        url += f'&health={health_filter}'
    result = requests.get(url)
    data = result.json()
    return data['hits']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    ingredient = request.form['ingredient']
    diet = request.form.get('diet')
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
