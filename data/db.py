from datetime import datetime
import sqlite3

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

###############################################################################
ip = 'ml-test-01'
prefs = {'peas':0, 'corn':1}
fp = FoodPrefs(ip, prefs)
#con = fp._create_table()
fp.save()


con = sqlite3.connect('data/broccoli.db')
df = pd.read_sql('select * from foodprefs', con)
df = df.set_axis(axis=1)
