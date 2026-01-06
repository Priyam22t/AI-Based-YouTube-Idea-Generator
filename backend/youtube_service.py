import os
import requests
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_youtube(query, max_results=7):
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    videos = []

    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        videos.append({
            "title": title,
            "url": video_url
        })

    return videos
