import json
import os
import random
import requests
import time

from dotenv import load_dotenv, find_dotenv
import pandas as pd
from tqdm import tqdm

load_dotenv(find_dotenv())

# https://developers.google.com/knowledge-graph/
# https://github.com/schemaorg/schemaorg/issues/458
API_KEY = os.environ['KG_API_KEY']

foods = ['alfalfa sprouts', 'apples', 'apricots', 'artichokes', 'arugula',
    'asparagus', 'avocados', 'bananas', 'bean sprouts', 'beets',
    'bell peppers', 'blackberries', 'blueberries', 'bok choy', 'broccoli',
    'brussels sprouts', 'butternut squash', 'cabbage', 'cantaloupe', 'carrots',
    'cauliflower', 'celery', 'cherries', 'chili peppers', 'clementines',
    'coconuts', 'collard greens', 'coriander', 'corn', 'cranberries',
    'cucumbers', 'currants', 'dandelion greens', 'dates', 'dragonfruit',
    'edamame', 'eggplant', 'endive', 'fennel', 'fiddleheads', 'figs', 'garlic',
    'ginger', 'grapefruits', 'grapes', 'green beans', 'green onions', 'guava',
    'honeydew melons', 'hubbard squash', 'iceberg lettuce', 'jicama', 'kale',
    'kiwi', 'kohlrabi', 'leeks', 'lemons', 'limes', 'mangoes', 'mushrooms',
    'nectarines', 'okra', 'oranges', 'papayas', 'parsley', 'parsnips',
    'passionfruit', 'peaches', 'pears', 'peas', 'persimmons', 'pineapples',
    'plantains', 'plums', 'pomegranates', 'potatoes', 'pumpkins', 'radicchio',
    'radishes', 'raspberries', 'red onions', 'rhubarb', 'romaine lettuce',
    'rutabagas', 'shallots', 'snow peas', 'spaghetti squash', 'spinach',
    'starfruit', 'strawberries', 'sugar snap peas', 'sweet potatoes',
    'swiss chard', 'tomatoes', 'turnips', 'watermelons', 'wax beans',
    'yellow onions', 'yellow squash', 'zucchini'
]

def search_knowledge_graph(query):
    base = 'https://kgsearch.googleapis.com/v1/entities:search'
    url = f'{base}?query={query}&key={API_KEY}&types=Thing'
    r = requests.get(url)
    data = r.json()
    return data

def fetch_food(food):
    filename = f'data/{food.replace(" ", "_")}.json'
    try:
        with open(filename) as infile:
            result = json.load(infile)
    except:
        result = search_knowledge_graph(food)
        with open(filename, 'w') as outfile:
            json.dump(result, outfile)
        #time.sleep(1)
    return result

def fetch_all_foods():
    results = []
    for food in tqdm(foods):
        response = fetch_food(food)

        for r in response['itemListElement']:
            dict = {
                'query': food,
                'score': r['resultScore'],
                'name': r['result']['name'],
                'type': ' '.join(r['result']['@type']),
                'id': r['result']['@id']
            }
            try:
                dict['image'] = r['result']['image']['contentUrl']
            except:
                dict['image'] = None
            try:
                dict['description'] = r['result']['description']
            except:
                dict['description'] = None
            try:
                dict['url'] = r['result']['detailedDescription']['url']
            except:
                dict['url'] = None
            try:
                dict['article'] = r['result']['detailedDescription']['articleBody']
            except:
                dict['article'] = None

            results.append(dict)
    return results

if __name__ == '__main__':
    df = pd.DataFrame(fetch_all_foods())
    df.to_csv('data/vegetables.csv', index=False)
