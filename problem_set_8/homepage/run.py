"""
    Quick script to get the Red Dwarf episode data from IMDB API
"""

import requests
import json


API_KEY = "NOT TELLING"
BASE_URL = "https://imdb-api.com/en/API/SeasonEpisodes/API_KEY_HERE/tt0094535/{}"


with open("episodes.json", "w", encoding="utf8") as f:

    for season in range(1, 14):
        url = BASE_URL.format(season)
        response = requests.get(url).json()
        episodes = response["episodes"]

        json.dump(episodes, f)
