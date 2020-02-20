from datetime import datetime
import json
import os
import sqlite3
import uuid

import pandas as pd

class FoodPrefs:
    def __init__(self, ip, prefs):
        self.date = datetime.now(),
        self.ip = ip,
        self.prefs = prefs

    def save(self):
        s = self._save_json()
        #df = pd.DataFrame.from_dict(self.prefs, orient='index').T
        #df['date'] = self.date
        #df['ip'] = self.ip
        #con = self._get_connection()
        #df.to_sql('foodprefs', con, if_exists='append')
        #con.close()
        return s

    def _get_connection(self):
        con = sqlite3.connect('data/broccoli.db')
        #to do: check if table exists before loading csv
        df = pd.read_csv('data/foods.csv')
        try:
            df.T.to_sql('foodprefs', con)
        except ValueError:
            pass # table already exists
        return con

    def _save_json(self): # redundant backup just in case
        status = None
        with open(f'data/json/{uuid.uuid4().hex}.json', 'w') as outfile:
            status = os.path.dirname(os.path.realpath(__file__))
            data = {
                'date': self.date.__str__(),
                'ip': self.ip,
                'prefs': self.prefs
            }
            json.dump(data, outfile)
        return status
