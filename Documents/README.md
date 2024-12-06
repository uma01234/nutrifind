# NutriFind

NutriFind is a web-based application that helps users find recipes tailored to their dietary preferences and restrictions. Users can search for recipes by ingredients, select multiple dietary restrictions, and view detailed results, including nutritional information and links to the full recipe.

## Features
- Search for recipes by entering one or more ingredients.
- Apply dietary restrictions such as Vegan, Vegetarian, Gluten-Free, etc.
- View recipe results with details like meal type, calories, dietary labels, and ingredients.
- Easily navigate back to the search page with a "Search Again" button.

---

## Installation and Setup

### Prerequisites
- Python 3.8+ installed on your system.
- A basic understanding of Python and Flask.
- An API key and application ID for the **Edamam API**.

### Setting Up the Project
1. Clone or download this repository.
2. Navigate to the project folder in your terminal:
   ```bash
   cd NutriFind
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Obtain your **Edamam API Key**:
   - Go to the [Edamam API website](https://developer.edamam.com/) and sign up.
   - Create a new application to get your `APP_ID` and `APP_KEY`.

6. Create a `keys.py` file in the project root to store your API credentials:
   ```python
   # keys.py
   app_id = "your_app_id_here"
   app_key = "your_app_key_here"
   ```

---

## Running the Application
1. Start the Flask server:
   ```bash
   python runapp.py
   ```
2. Open your browser and go to `http://127.0.0.1:5000`.

---

## How to Use NutriFind

### Step 1: Enter Ingredients
- On the homepage, enter one or more ingredients (e.g., "salmon, butter") in the input field.
- You can enter ingredients separated by commas or spaces (e.g., `eggs, butter` or `eggs butter`).

### Step 2: Select Dietary Restrictions
- Use the dropdown to select one or more dietary restrictions (e.g., Vegan, Gluten-Free).
- Hold the `Ctrl` key (or `Cmd` on Mac) to select multiple options.

### Step 3: View Results
- Click "Search" to view the results.
- The results page displays:
  - **Recipe Name**: Title of the recipe.
  - **Meal Type**: e.g., Breakfast, Lunch, Dinner.
  - **Calories**: Rounded to the nearest whole number.
  - **Dietary Labels**: Dietary restrictions that apply to the recipe.
  - **Ingredients**: A detailed list of ingredients.
  - **View Recipe**: A link to the full recipe.

### Step 4: Search Again
- Use the "Search Again" button (available at the top and bottom of the results page) to return to the search page.

---

## Screenshots
### Homepage
![Homepage](docs/homepage.png)

### Results Page
![Results Page](docs/results_page.png)

---

## Troubleshooting

### Common Issues and Fixes
1. **API Key Error**: If you see an error indicating invalid credentials:
   - Double-check your `keys.py` file to ensure the `app_id` and `app_key` values are correct.
   - Ensure your API key has not expired or exceeded its quota.

2. **No Results for Filters**:
   - If you apply dietary restrictions and see recipes that don’t match, ensure the filters align with your expectations.
   - Check the `healthLabels` section in the recipe details for matching criteria.

3. **Ingredient Formatting**:
   - Ensure ingredients are entered correctly. If you enter "salmon butter," it will automatically format to "salmon,butter."

4. **Missing Dependencies**:
   - If you get errors about missing Python packages, ensure you ran:
     ```bash
     pip install -r requirements.txt
     ```

---

## Limitations and Known Issues
- Recipes might still appear if they partially match dietary filters. This is dependent on the Edamam API's filtering.
- The calorie information is rounded but might still vary slightly due to API data precision.
- Multiple filters are applied conjunctively (i.e., all must match).

---

## Future Improvements
- Add pagination for large result sets.
- Display preparation and cooking times (if available from the API).
- Improve ingredient parsing for more natural input (e.g., "3 eggs and butter").

---

Feel free to raise issues or contribute to the project on GitHub! 😊
