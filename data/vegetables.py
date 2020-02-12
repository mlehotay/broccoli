import os
import requests

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

API_KEY = os.environ['KG_API_KEY'] # https://developers.google.com/knowledge-graph/

query = 'broccoli'
URL = f'https://kgsearch.googleapis.com/v1/entities:search?query={query}&key={API_KEY}'

r = requests.get(URL)
data = r.json()
data.keys()
data['@context']
data['@type']
data['itemListElement']
