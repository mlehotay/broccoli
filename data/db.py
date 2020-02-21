from datetime import datetime
import json
import os
import sqlite3
import uuid

import pandas as pd

class FoodPrefs:
    def __init__(self, ip, prefs):
        self.date = datetime.now().strftime('%c')
        self.ip = ip
        self.prefs = prefs

    def save(self):
        self._save_json()
        df = pd.DataFrame.from_dict(self.prefs, orient='index').T
        df['date'] = self.date
        df['ip'] = self.ip
        con = get_connection()
        df.to_sql('foodprefs', con, if_exists='append')
        con.close()

    def _save_json(self): # redundant backup just in case
        with open(f'data/json/{uuid.uuid4().hex}.json', 'w') as outfile:
            data = {
                'date': self.date,
                'ip': self.ip,
                'prefs': self.prefs
            }
            json.dump(data, outfile)

def get_connection():
    print('start')
    con = sqlite3.connect('data/broccoli.db')
    #to do: check if table exists before loading csv
    df = get_seed_data()
    try:
        df.to_sql('foodprefs', con)
    except ValueError:
        pass # table already exists
    print('returning connection')
    return con

def get_seed_data():
    df = pd.read_csv('data/foods.csv').T
    df.columns = [food.replace(' ', '') for food in df.iloc[0]]
    df = df.drop('Food', axis=0)
    df = df.reset_index()
    df['name'] = df['index']
    df = df.drop('index', axis=1)
    df['date'] = None
    df['ip'] = None
    return df
