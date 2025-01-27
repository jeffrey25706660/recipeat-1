# RecipEat
**By: Corina Geier, Jeffery Lai, Edward Lou, Sai Muktevi, Andrew Zhou**

## Background
Figuring out what to eat based on the food you have in your fridge can be a difficult task for many. This task is made even harder when someone is trying to eat healthy. RecipEat aims to solve this problem by providing healthy recipes that can be made with the food someone has on hand. RecipEat works with a user’s dietary constraints and nutritional goals to provide recipe recommendations that are the most relevant to the user. RecipEat also allows for a visual comparison of recipes so that users can quickly decide which recipe they would rather make. 

## Modules
### recipe_recommender.py
A class that has methods to search for recipes with given inputs:
* Desired ingredients (i.e. chicken, potatoes, etc)
* Nutritional Requirements (i.e. calories, carbohydrates, proteins, and fats)
* Intolerances (i.e. dairy, egg, etc)
* Diet (i.e. Gluten Free, Ketogenic, etc)

### comparator.py
A class that has methods to visually compare nutrients and ingredients for selected recipes.
* the nutrient comparator shows a bargraph of different nutrional information amounts per each recipe
* the ingredient comparator shows pictures of the ingredients in a selected recipe


## Project Data (or API?)
### Spoonacular: 
Spoonacular is a Recipe-Food-Nutrition API providing access to over 365,000 recipes through ingredient- and nutrient-based queries. The user can also include keywords or phrases, such as ‘lactose intolerance’, to search for recipes that accommodate any special dietary restrictions or preferences. Additionally, the user can analyze nutritional information for each recipe by utilizing the visualization widgets.

## Testing

## Documentation

## Directory Structure
```bash
.
|-- Procfile
|-- README.md
|-- __pycache__
|   |-- config.cpython-38.pyc
|   `-- recipeat.cpython-38.pyc
|-- app
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-38.pyc
|   |   `-- routes.cpython-38.pyc
|   |-- forms
|   |   |-- __pycache__
|   |   |   |-- ingredients_form.cpython-38.pyc
|   |   |   `-- register_form.cpython-38.pyc
|   |   |-- ingredients_form.py
|   |   |-- login_form.py
|   |   |-- recipe_form.py
|   |   `-- register_form.py
|   |-- routes.py
|   |-- static
|   |   `-- styles
|   |       `-- base.css
|   `-- templates
|       |-- base.html
|       |-- index.html
|       |-- ingredients.html
|       |-- login.html
|       |-- recipe.html
|       |-- register.html
|       `-- visual_comparator.html
|-- commands
|   |-- command.py
|   `-- create_table.py
|-- config.py
|-- github_commands.md
|-- modules
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-38.pyc
|   |   |-- bag_of_ingredients.cpython-38.pyc
|   |   |-- constants.cpython-38.pyc
|   |   |-- database.cpython-38.pyc
|   |   `-- user.cpython-38.pyc
|   |-- bag_of_ingredients.py
|   |-- constants.py
|   |-- database.py
|   |-- jsonConverter.py
|   |-- readme.txt
|   |-- recipe_recommender.py
|   `-- user.py
|-- notebooks
|   `-- spoonapi.ipynb
|-- recipeat.py
|-- requirements.txt
|-- tests
|   |-- __init__.py
|   |-- test_jsonConverter.py
|   `-- test_recipe_recommender.py
`-- wsgi.py
```


## Future Work

[More information about the project propsal here.](https://docs.google.com/document/d/1VCmc425JY53zHsUiasGh4CeFm5eu0YMbTKfwk1pRHZA/edit#heading=h.5x0d5h95i329) 

>Run the following code to install all the requuired packages/dependecies to run this application locally.

```
while read requirement; do pip install $requirement; done < requirements.txt
```

> Run the application using the following command line while in app.py directory.

```
flask run
```


