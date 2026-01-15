import os
from fileinput import filename
from re import search

import requests
BASE_URL = "https://images-api.nasa.gov"
#1 search image Curiosity
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}
search_response = requests.get(search_url, params=search_params)
search_response.raise_for_status()
search_data = search_response.json()

#get nasa_id
items = search_data ['collection']['items']
nasa_ids = [item["data"][0]["nasa_id"] for item in items[:2]]

#for each nasa_id get jpg and downloads
for index, nasa_id in enumerate(nasa_ids, start=1):
    asset_url = f"{BASE_URL}/nasa/{nasa_id}"
    asset_response = requests.get(asset_url)
    asset_response.raise_for_status()
    asset_data = asset_response.json()

#search jpg

    jpg_url = None
    for item in asset_data['collection']['items']:
        if item["href"].lower().endswith("jpg"):
            jpg_url = item["href"]
            break
    if not jpg_url:
        print(f"Could not find JPG for {nasa_id}")
        continue

#downloads file
image_response = requests.get(jpg_url)
image_response.raise_for_status()
filename = f"mars_photo{index}.png"
with open(filename, "wb") as f:
    f.write(image_response.content)
