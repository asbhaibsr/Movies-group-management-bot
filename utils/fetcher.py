import requests
import os

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

def fetch_movie_info(query):
    search_url = f"{TMDB_BASE_URL}/search/movie?query={query}&api_key={TMDB_API_KEY}&language=hi-IN"
    response = requests.get(search_url)
    if response.status_code != 200:
        return "❌ API Error. Try again later."

    results = response.json().get("results")
    if not results:
        return "😢 Koi result nahi mila."

    movie = results[0]
    movie_id = movie.get("id")
    
    # Get full movie info
    detail_url = f"{TMDB_BASE_URL}/movie/{movie_id}?api_key={TMDB_API_KEY}&language=hi-IN"
    detail = requests.get(detail_url).json()

    return (
        f"🎬 *{detail.get('title', 'N/A')}* ({detail.get('release_date', '')[:4]})\n"
        f"⭐ Rating: {detail.get('vote_average', 'N/A')}/10\n"
        f"📅 Release: {detail.get('release_date', 'N/A')}\n"
        f"🎭 Genre: {', '.join([g['name'] for g in detail.get('genres', [])])}\n"
        f"📝 Plot: {detail.get('overview', 'N/A')}\n"
        f"🌐 TMDB Link: https://www.themoviedb.org/movie/{movie_id}"
    )
