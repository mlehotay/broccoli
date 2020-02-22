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
    foods = get_recommendations(args, 5)
    if len(foods) == 0:
        s = 'Sorry! There were no recommendations based on your input. ☹️'
    else:
        for food in foods:
            slug = food.replace(' ', '')
            filename = f'static/images/{slug}.jpg'
            s += '<tr><td align="center">'
            s += f'{food}<br>'
            s += f'<img src="{filename}" height="75%" width="75%" alt="picture of {food}">'
            s += '</td></tr>\n'
    return s

def get_recommendations(args, limit):
    df_user = pd.DataFrame.from_dict(args, orient='index').T

    con = get_connection()
    df_all = pd.read_sql('select * from foodprefs', con, index_col='index')
    df_all = df_all.reset_index(drop=True)
    con.close()

    recs = []
    neighbors = find_neighbors(df_user, df_all)
    for neighbor in neighbors:
        df_neighbor = df_all.iloc[neighbor]
        df_neighbor = df_neighbor.drop(['name', 'ip', 'date'])
        likes = [f for f in df_neighbor.index if df_neighbor[f]==1]
        new_recs = [f for f in likes if f not in df_user.columns]
        random.shuffle(new_recs)
        n = min(len(new_recs), limit-len(recs))
        recs += new_recs[0:n]
        if len(recs) == limit:
            break
    return recs

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
