from datetime import datetime
import json
import sqlite3
import uuid

import pandas as pd

def save_userdata(ip, args):
    return save_json(ip, args)

def save_json(ip, args):
    with open(f'data/userdata/{uuid.uuid4().hex}.json', 'w') as outfile:
        data = {
            'date': datetime.now().__str__(),
            'ip': ip,
            'prefs': args
        }
        json.dump(data, outfile)
    return True

def save_sql(ip, args):
    con = sqlite3.connect("data/broccoli.db")
    df = pd.read_sql('foodprefs')

    #pandas.read_sql(sql, con, parse_dates=None, columns=None, chunksize=None)[source])

    df.to_sql('foodpfrefs', con, if_exists='append')

    #select lower(quote(uid)) from foodprefs
    con = sqlite3.connect("data/broccoli.db")
    cur = con.cursor()
    #cur.execute(sql)
    #con.commit()
    con.close()
