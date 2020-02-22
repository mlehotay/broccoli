import random
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from data.db import get_connection

def food_survey():
    s = ''
    df = pd.read_csv('data/foods.csv')
    foods = df['Food'].to_list()
    i=1
    for food in foods:
        slug = food.replace(' ', '')
        filename = f'static/images/{slug}.jpg'
        s += f'<tr><td>{i}</td><td>{food}</td><td><img src="{filename}" alt="picture of {food}"></td>\n'
        s += f'    <td><input type="radio" id="{slug}-like" name="{slug}" value="1"><label for="{slug}-like">like</label><br>\n'
        s += f'    <input type="radio" id="{slug}-neutral" name="{slug}" value="0" checked><label for="{slug}-neutral">neutral</label><br>\n'
        s += f'    <input type="radio" id="{slug}-dislike" name="{slug}" value="-1"><label for="{slug}-dislike">dislike</label></td></tr>\n'
        i += 1
    return s

def food_grid():
    s = '\n'
    df = pd.read_csv('data/foods.csv')
    foods = random.sample(df['Food'].to_list(), k=16)
    i = 0
    for food in foods:
        slug = food.replace(' ', '')
        filename = f'static/images/{slug}.jpg'
        if (i%4) == 0:
            s += '<tr>\n'
        s += '<td align="center">'
        s += f'{food}<br><img src="{filename}" height="50%" width="50%" alt="picture of {food}"><br>\n'
        s += '<small>'
        s += f'<input type="radio" id="{slug}-like" name="{slug}" value="1"><label for="{slug}-like">like</label>\n'
        s += f'<input type="radio" id="{slug}-neutral" name="{slug}" value="0" checked><label for="{slug}-neutral">neutral</label>\n'
        s += f'<input type="radio" id="{slug}-dislike" name="{slug}" value="-1"><label for="{slug}-dislike">dislike</label>\n'
        s += '</small>'
        s += '</td>'
        if (i%4) == 3:
            s += '\n</tr>'
        s += '\n'
        i += 1
    return s

def recommend_foods(args):
    s = '\n'
    foods = get_recommendations(args)
    for food in foods:
        slug = food.replace(' ', '')
        filename = f'static/images/{slug}.jpg'
        s += '<tr><td align="center">'
        s += f'{food}<br>'
        s += f'<img src="{filename}" height="75%" width="75%" alt="picture of {food}">'
        s += '</td></tr>\n'
    return s

def get_recommendations(args):
    df_user = pd.DataFrame.from_dict(args, orient='index').T

    con = get_connection()
    df_all = pd.read_sql('select * from foodprefs', con, index_col='index')
    df_all = df_all.reset_index(drop=True)
    con.close()

    neighbors = find_neighbors(df_user, df_all)
########################################################
    # for now, just return random foods
    # delete this when the code above is working
    df = pd.read_csv('data/foods.csv')
    foods = random.sample(df['Food'].to_list(), k=5)
    return foods
#####################################################

def find_neighbors(df_user, df_all):
    df_cropped = df_all.drop(['name', 'ip', 'date'], axis=1)
    for food in df_cropped.columns:
        if food not in df_user.columns:
            df_cropped = df_cropped.drop(food, axis=1)
    df_cropped = df_cropped.dropna()
    df_cropped = df_cropped.sort_index(axis=1)

    sim = pd.DataFrame(np.round(cosine_similarity(df_user, df_cropped), 2))
    neighbors = np.fliplr(np.argsort(sim))[0]
    k=0
    while(sim[neighbors[k]][0]>0):
        k += 1
    return neighbors[0:k]

###############################################################################
# sandbox
#import json
#f = open('data/foodgrid.json')
#p = json.load(f)
#f.close()
#args = p['prefs']
#df_user = pd.DataFrame.from_dict(args, orient='index').T.sort_index(axis=1)
#con = get_connection()
#df_all = pd.read_sql('select * from foodprefs', con, index_col='index')
#con.close()
#df_all = df_all.reset_index(drop=True)
#neighbors = find_neighbors(df_user, df_all)


## from model.py
#sim.loc['slippery'].sort_values(ascending=False)[1:]
#food = list(df.loc['white'][df.loc['white'] == 1].index)
#food
#tried = list(df.loc['slippery'][df.loc['slippery'] == 1].index)
#[f for f in food if f not in tried]
