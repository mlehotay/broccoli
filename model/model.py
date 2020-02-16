import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

foods = ['name', 'potatoes', 'mushrooms', 'lettuce', 'pumpkin', 'zucchini',
    'onions', 'tomatoes', 'carrots', 'bell peppers', 'broccoli']

users = [
    ('michael', 1, 1, 0, 1, 0, 1, 1, 1, 1, 1),
    ('green', 0, 0, 1, 0, 1, 0, 0, 0, 1, 1),
    ('white', 1, 1, 0, 0, 0, 1, 0, 0, 0, 0),
    ('slippery', 0, 1, 0, 0, 0, 1, 0, 0, 0, 0),
    ('crunchy', 0, 0, 1, 0, 0, 0, 0, 1, 1, 1),
    ('letter_o', 1, 1, 0, 0, 0, 1, 1, 1, 0, 1),
]

# setup dataframe
df = pd.DataFrame(users, columns=foods)
df = df.set_index("name")
df

sim = pd.DataFrame(
    np.round(cosine_similarity(df, df), 2),
    columns=df.index,
    index=df.index)

sim.loc['slippery'].sort_values(ascending=False)[1:]
food = list(df.loc['white'][df.loc['white'] == 1].index)
food
tried = list(df.loc['slippery'][df.loc['slippery'] == 1].index)
[f for f in food if f not in tried]
