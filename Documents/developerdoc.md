### Developer's Guide for NutriFind

---

# NutriFind Developer's Guide

## **Overview**
NutriFind is a Python-based web application that leverages Flask and the Edamam API to fetch and display recipes based on user input. Users can search for recipes by providing one or more ingredients and applying dietary restrictions (e.g., Vegan, Gluten-Free). The application dynamically renders search results in a user-friendly interface.

This guide provides detailed information for developers who want to maintain, extend, or understand the application's internals.

---

## **Planning Specifications**

### Final Implemented Features
1. **Ingredient-Based Recipe Search**:
   - Users input one or more ingredients, separated by commas or spaces.
   - The application formats the input for compatibility with the Edamam API.

2. **Dietary Filters**:
   - Users can select multiple dietary restrictions from a dropdown menu.
   - Filters such as Vegan, Vegetarian, and Gluten-Free are applied to the API query.

3. **Recipe Details**:
   - Displays recipe name, calories (rounded), meal type, ingredients, and dietary labels.

4. **Navigation**:
   - A "Search Again" button is available at the top and bottom of the results page.

---

## **Installation, Deployment, and Administration**

### Prerequisites
- Python 3.8 or higher.
- A virtual environment for dependencies.
- Edamam API credentials (APP_ID and APP_KEY).

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd NutriFind
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up API credentials in `keys.py`:
   ```python
   # keys.py
   app_id = "your_app_id_here"
   app_key = "your_app_key_here"
   ```

5. Run the application:
   ```bash
   python main.py
   ```

6. Access the app in a browser at `http://127.0.0.1:5000`.

---

## **User Interaction and Code Walkthrough**

### User Interaction Flow
1. **Search Page**:
   - Users input ingredients and select dietary restrictions.
   - On submission, data is sent to the `/search` route via POST.

2. **Results Page**:
   - Recipes matching the input and filters are displayed in a card layout.
   - Details include calories, meal type, ingredients, and dietary labels.

3. **Navigation**:
   - "Search Again" buttons at the top and bottom allow easy navigation back to the search page.

### Code Walkthrough
#### Key Modules and Functions
| **Name**            | **Location**      | **Description**                                                                 |
|---------------------|-------------------|---------------------------------------------------------------------------------|
| `main.py`           | `app/`            | Core logic, including Flask app initialization and route definitions.           |
| `keys.py`           | `app/`            | Stores API credentials for Edamam.                                              |
| `index.html`        | `app/templates/`  | Renders the search form.                                                        |
| `results.html`      | `app/templates/`  | Dynamically displays the recipe results.                                        |
| `recipe_search`     | `main.py`         | Fetches recipes from the Edamam API based on user input and dietary filters.    |

---

### Code Flow
1. **Initialization**:
   - Flask is initialized in `main.py`.
   - Routes (`/` and `/search`) handle navigation.

2. **Search Processing**:
   - `recipe_search` formats user input, constructs the API query, and filters results.

3. **Rendering**:
   - Jinja2 templates (`index.html`, `results.html`) dynamically render pages.

---

## **Known Issues**

### Minor Issues
1. **Dietary Filter Mismatches**:
   - Some recipes may include irrelevant results due to API limitations.
   - Workaround: Verify recipes using the displayed dietary labels.

2. **UI Design**:
   - The interface is functional but could benefit from a CSS framework like Bootstrap for better aesthetics.

### Major Issues
- **API Dependency**:
  - The app relies entirely on the Edamam API. If the API is unavailable, the app cannot function.
  - Suggested Fix: Implement caching for frequent queries.

---

## **Future Work**

### Enhancements
1. **Pagination**:
   - Display search results across multiple pages for improved usability.

2. **User Profiles**:
   - Allow users to save favorite recipes and search history.

3. **Expanded Filters**:
   - Add cuisine type filters (e.g., Italian, Mexican) for more granular searches.

### Performance Improvements
1. **Caching**:
   - Cache API responses using a service like Redis to reduce latency and API dependency.

2. **Database Integration**:
   - Store recipes locally for offline access or batch processing.

---

## **Graphics and Tables**

### Flow Diagram
```
User Input --> /search Route --> API Query --> Filter Recipes --> Render Results
```

---

## **Ongoing Development**

### Testing
1. **Testing Framework**:
   - Use `pytest` to write and execute test cases.

2. **Example Test**:
   ```python
   def test_recipe_search():
       mock_ingredient = "salmon,butter"
       mock_filters = ["vegan"]
       results = recipe_search(mock_ingredient, mock_filters)
       assert all("Vegan" in recipe['healthLabels'] for recipe in results)
   ```
