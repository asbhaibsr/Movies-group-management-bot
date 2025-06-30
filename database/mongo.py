from pymongo import MongoClient
import os, random
import json

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client.moviebot

def get_random_trivia():
    data = list(db.trivia.find())
    return random.choice(data) if data else json.load(open("static/trivia_data.json"))[0]

def get_group_settings(chat_id):
    doc = db.groups.find_one({"chat_id": chat_id}) or {"chat_id": chat_id, "movie_info": True, "trivia": True}
    db.groups.update_one({"chat_id": chat_id}, {"$set": doc}, upsert=True)
    return doc

def toggle_feature(chat_id, feature):
    current = get_group_settings(chat_id)
    current[feature] = not current[feature]
    db.groups.update_one({"chat_id": chat_id}, {"$set": current})

def broadcast_all(message):
    chats = db.groups.find()
    # Send logic should be async, simplified here
    return len(list(chats))
