from pymongo import MongoClient

client = MongoClient("<Connection String>")

# DB and Collection is not created until there is posage
# create a DB
db = client.DBName

# create a collection
collection = db.Collection

# create a sample data
item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}

item_2 = {
  "_id" : "U1IT00002",
  "item_name" : "Egg",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs"
}

collection.insert_many([item_1, item_2])
