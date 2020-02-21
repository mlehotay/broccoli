import random
import pandas as pd

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
