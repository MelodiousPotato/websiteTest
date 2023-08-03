from pymongo import MongoClient
from PIL import Image
import io

client = MongoClient("urmom")
db = client["readables"]
images = db["images"]

im = Image.open("Readables/A Fool's Play.png")

image_bytes = io.BytesIO()
im.save(image_bytes, format='PNG')

image = {
    'name': "A Fool's Play",
    'data': image_bytes.getvalue()
}

image_id = images.insert_one(image).inserted_id
