import json
import os
import requests

RANDOM_DOG_API_URL = "https://dog.ceo/api/breeds/image/random"

try:
    response = requests.get(RANDOM_DOG_API_URL)
    response.raise_for_status()
    data = response.json()
    dog_image_url = data['message']
    print(f"Random Dog Image URL: {dog_image_url}")
except:
    print("Failed to fetch a random dog image. Please check your internet connection or the API status.")
    