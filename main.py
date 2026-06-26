#imports
import requests
import json
import os
from dotenv import load_dotenv

print('hello ???')
#LOAD ENV FILES
load_dotenv()  # Load environment variables from .env file  

# API key as a constant
YOUR_API_KEY= os.getenv("YOUR_API_KEY")  # Retrieve the API key from environment variables
GET_RANDOM_URL="https://api.thecatapi.com/v1/images/search"
GET_RANDOM_10 = "https://api.thecatapi.com/v1/images/search?limit=10"
GET_RANDOM_BENGAL="https://api.thecatapi.com/v1/images/search?limit=10&breed_ids=beng&api_key=" + YOUR_API_KEY

#GET REQUEST
try: 
    response = requests.get(GET_RANDOM_URL) # sed get request to the API, stores response in a variable
    response.raise_for_status()  # checking the status code 
    data = response.json() # data stores the reponse in json format
    print(json.dumps(data, indent=4))  # Prints the data in a readable format

except:
    print("Error occurred while making the GET request.")
    