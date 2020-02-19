from datetime import datetime
import sqlite3
import uuid

import pandas as pd

def save_userdata(ip, args):
    return save_text(ip, args)

def save_text(ip, args):
    with open(f'data/userdata/{uuid.uuid4().hex}.txt', 'w') as f:
        f.write(f'{datetime.now()}\n')
        f.write(f'{ip}\n')
        f.write(f'{args}\n')
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
