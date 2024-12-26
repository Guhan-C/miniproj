from flask import Flask, request, jsonify, render_template
import pymongo

app = Flask(__name__)

# MongoDB connection setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["recipe_database"]
recipes_collection = db["recipes"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get data from the form
    ingredients = request.form.get('ingredients')
    diet = request.form.get('diet')

    # Convert inputs to lists for comparison
    ingredient_list = [i.strip().lower() for i in ingredients.split(',')] if ingredients else []
    dietary_restriction = diet.lower() if diet else None

    # Query MongoDB for recipes
    query = {"ingredients": {"$all": ingredient_list}}
    if dietary_restriction:
        query["dietary_restrictions"] = dietary_restriction

    # Retrieve matching recipes
    matching_recipes = list(recipes_collection.find(query, {"_id": 0}))

    if matching_recipes:
        return jsonify({"status": "success", "recipes": matching_recipes})
    else:
        return jsonify({"status": "error", "message": "No recipes found matching your criteria."})

if __name__ == '__main__':
    app.run(debug=True)
