#AVAILABLE API KEYS
apikey1 = 'apiKey=4078ba908cf14212b9c3754a84a262f5'
apikey2 = 'apiKey=d18b19ea103f46929e677ecacef2c15c'
apikey3 = 'apiKei=000c6ad96dd4406084b8c5492a302592'

# Config firebase
config = {
    "apiKey": "AIzaSyALmQ-MUJqlIWPmZZK8P73JTxgiWFzcTwY",
    "authDomain": "recipeat-e5c29.firebaseapp.com",
    "databaseURL": "https://recipeat-e5c29-default-rtdb.firebaseio.com",
    "projectId": "recipeat-e5c29",
    "storageBucket": "recipeat-e5c29.appspot.com",
    "messagingSenderId": "141820818637",
    "appId": "1:141820818637:web:303e5636dc57aabbd9e584",
    "measurementId": "G-SHGP23CXCE"
}

#sample user details
username = "recipeat@gmail.com"
password = "qwerty01"
usn = "johndoe1"

#sample user json data
sample_user = {
  "email": "recipeat@gmail.com",
  "username": "johndoe1",
  "details": {
    "height": "999",
    "weight": "999",
    "age": "999",
    "gender": "male"
  },
  "boi": [
    {
      "ingredientFull": "1 cup green tea",
      "ingredient": "green tea",
      "amount": 1,
      "unit": "cup"
    },
    {
      "ingredientFull": "2 oz mushrooms",
      "ingredient": "mushrooms",
      "amount": 2,
      "unit": "oz"
    },
    {
      "ingredientFull": "150 g egg whites",
      "ingredient": "egg whites",
      "amount": 150,
      "unit": "g"
    }
  ],
  "cuisine": [
    "italian"
  ],
  "tolerances": [
    "gluten"
  ],
  "diet": "vegetarian"
}

#GET URL
# api_home = "https://api.spoonacular.com/recipes"

search_recipes = "https://api.spoonacular.com/recipes/complexSearch"
search_recipes_nutrients = " https://api.spoonacular.com/recipes/findByNutrients"
search_recipes_ingredients = "https://api.spoonacular.com/recipes/findByIngredients"

get_recipe_info = "https://api.spoonacular.com/recipes/{id}/information"
get_recipe_info_bulk = "https://api.spoonacular.com/recipes/informationBulk"
