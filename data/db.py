from datetime import datetime
import json
import sqlite3
import uuid

import pandas as pd

class FoodPrefs:
    def __init__(self, ip, prefs):
        self.date = datetime.now(),
        self.ip = ip,
        self.prefs = prefs

    def save(self):
        df = pd.DataFrame.from_dict(self.prefs, orient='index').T
        df['date'] = self.date
        df['ip'] = self.ip
        con = self._create_table()
        df.to_sql('foodprefs', con, if_exists='append')
        con.close()

    def _create_table(self):
        con = sqlite3.connect('data/broccoli.db')
        df = pd.read_csv('data/foods.csv')
        try:
            df.T.to_sql('foodprefs', con)
        except ValueError:
            pass # table already exists
        return con

    def save_json(ip, args):
        with open(f'data/json/{uuid.uuid4().hex}.json', 'w') as outfile:
            data = {
                'date': datetime.now().__str__(),
                'ip': ip,
                'prefs': args
            }
            json.dump(data, outfile)
        return True

###############################################################################
ip = 'ml-test-01'
prefs = {'peas':0, 'corn':1}
fp = FoodPrefs(ip, prefs)
#con = fp._create_table()
fp.save()
    #pandas.read_sql(sql, con, parse_dates=None, columns=None, chunksize=None)[source])

    df.to_sql('foodpfrefs', con, if_exists='append')

con = sqlite3.connect('data/broccoli.db')
df = pd.read_sql('select * from foodprefs', con)
df = df.set_axis(axis=1)
    #select lower(quote(uid)) from foodprefs
    con = sqlite3.connect("data/broccoli.db")
    cur = con.cursor()
    #cur.execute(sql)
    #con.commit()
    con.close()
