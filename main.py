import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Replace with your USDA API key
API_KEY = 'your_usda_api_key_here'
BASE_URL = 'https://api.nal.usda.gov/fdc/v1/foods/search'

# Function to search food using USDA API
def search_food(query):
    params = {
        'api_key': API_KEY,
        'query': query,
        'pageSize': 10  # Limit to 10 results for simplicity
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json().get('foods', [])
    else:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query', '')
    if query:
        food_data = search_food(query)
        return jsonify(food_data)
    else:
        return jsonify([]), 400

if __name__ == '__main__':
    app.run(debug=True)
