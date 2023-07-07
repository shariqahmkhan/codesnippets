# I will import modules as and when needed to make the program self explanatory
from pymongo import MongoClient

client = MongoClient('<connection string>')
db = client["DB name"]
# you can also list databases => <b>client.list_database_names() </b>and then select

collection_name = db["collection_name"]
# you can also list collections => <b>client.list_collection_names() </b>and then select

# apply find method on collection_name
data = collection_name.find()

# apply for loop to iterate over data
for i in data:
  print(i)

# the output is raw and not look well structued, hence we use pandas
from pandas import DataFrame as df

data_format = df(data) # the output will be in row and colum format

# NOTE it is just format
