import os
import random
import requests

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# https://developers.google.com/knowledge-graph/
API_KEY = os.environ['KG_API_KEY']

foods = ['alfalfa sprouts', 'aloe vera', 'apples', 'apricots', 'artichokes',
    'arugula', 'asparagus', 'avocados', 'bananas', 'bean sprouts', 'beets',
    'bell peppers', 'blackberries', 'blueberries', 'bok choy', 'broccoli',
    'brussels sprouts', 'cabbage', 'cantaloupe', 'carrots', 'cauliflower',
    'celery', 'cherries', 'chili peppers', 'clementines', 'coconuts',
    'collard greens', 'coriander', 'corn', 'cranberries', 'cucumbers',
    'currants', 'dandelion greens', 'dates', 'edamame', 'eggplant', 'endive',
    'fennel', 'fiddlehead ferns', 'figs', 'garlic', 'ginger', 'grapefruits',
    'grapes', 'green beans', 'green onions', 'sweet peas', 'guava',
    'honeydew melons', 'jicama', 'kale', 'kiwi', 'kohlrabi', 'kumquats',
    'leeks', 'lemons', 'lettuce', 'limes', 'lychee', 'mangoes', 'mushrooms',
    'nectarines', 'okra', 'onions', 'oranges', 'papayas', 'parsley',
    'parsnips', 'passionfruit', 'peaches', 'pears', 'persimmons',
    'pineapples', 'plantains', 'plums', 'pomegranates', 'potatoes',
    'pumpkins', 'radicchio', 'radishes', 'raspberries', 'rhubarb',
    'rutabagas', 'shallots', 'snow peas', 'spinach', 'starfruit',
    'strawberries', 'sugar snap peas', 'sweet potatoes', 'swiss chard',
    'tangerines', 'tomatoes', 'turnips', 'watermelons', 'wax beans',
    'winter squash', 'yams', 'yellow squash', 'zucchini'
]

def search_knowledge_graph(query):
    base = 'https://kgsearch.googleapis.com/v1/entities:search'
    url = f'{base}?query={query}&key={API_KEY}'
    r = requests.get(url)
    data = r.json()
    return data

if __name__ == '__main__':
    query = random.choice(foods)
    veg = search_knowledge_graph(query)
    print(f'query: {query}')
    print(f'@context:\n{veg["@context"]}')
    print(f'@type:\n{veg["@type"]}')
    print(f'itemListElement:\n{veg["itemListElement"]}')
