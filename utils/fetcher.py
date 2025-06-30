import requests
import os

API_KEY = os.getenv("OMDB_API_KEY")

def fetch_movie_info(title):
    r = requests.get(f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}")
    if r.status_code != 200: return None
    data = r.json()
    if data.get("Response") == "False": return None
    return (
        f"🎬 *{data['Title']}* ({data['Year']})\n"
        f"⭐ Rating: {data.get('imdbRating')}/10\n"
        f"📅 Release: {data.get('Released')}\n"
        f"🎭 Genre: {data.get('Genre')}\n"
        f"🎙️ Plot: {data.get('Plot')}\n"
    )
