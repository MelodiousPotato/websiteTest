from pymongo import MongoClient
from PIL import Image
import io

client = MongoClient("mongodb+srv://MelodiousPotato:zDOl7vurqaquebMJ@cluster0.ewhvwvs.mongodb.net/test")
db = client["readables"]
images = db["images"]

im = Image.open("/Users/rebekahmou/Desktop/Readables/A Fool's Play.png")

image_bytes = io.BytesIO()
im.save(image_bytes, format='PNG')

image = {
    'data': image_bytes.getvalue()
}

image_id = images.insert_one(image).inserted_id