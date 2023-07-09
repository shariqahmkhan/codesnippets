from pymongo import MongoClient

client = MongoClient('Connection String')

db = client.grid_fs
##########################################
import gridfs
fs = gridfs.GridFS(db)

file = r'literal path to file'
##########################################
# Image encoding
import base64
image = open(file, 'rb')
image_read = image.read()
image_64_encode = base64.b64encode(image_read) # encoded the image in file variable

##########################################
fs.put(base64.b64decode(image_64_encode), filename = 'test')
