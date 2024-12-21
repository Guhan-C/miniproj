from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
db = client['NLP']
collection = db['food']

# Define dietary restriction words
dietary_words = {
    "dairy": ["milk", "butter", "cream", "cheese", "yogurt"],
    "meat": ["beef", "pork", "chicken", "wurst", "lamb", "mutton", "bacon"],
    "seafood": ["fish", "shrimp", "crab", "lobster", "oyster"],
    "gluten": ["wheat", "barley", "rye", "bread", "crackers", "pasta"],
    "nuts": ["peanut", "almond", "cashew", "walnut", "pistachio", "hazelnut"],
    "alcohol": ["wine", "beer", "vodka", "rum", "whiskey", "champagne"]
}

# Function to find dietary restrictions for a given NER array
def find_dietary_restrictions(ner_array, dietary_words):
    matched_categories = set()
    for word in ner_array:
        for category, restriction_words in dietary_words.items():
            if any(restrict_word in word.lower() for restrict_word in restriction_words):
                matched_categories.add(category)
    return list(matched_categories)

# Process each document in MongoDB and update it
cursor = collection.find({}, {"NER": 1})  # Fetch only the NER field
i=0
for doc in cursor:
    print(i)
    i+=1
    ner_array = doc.get("NER", [])
    restrictions = find_dietary_restrictions(ner_array, dietary_words)

    # Update MongoDB with new dietary_restrictions field
    collection.update_one(
        {"_id": doc["_id"]},  # Match document by ID
        {"$set": {"dietary_restrictions": restrictions}}  # Add new field
    )

print("Dietary restrictions added successfully to each document!")
