import pandas as pd
import numpy as np
import sqlite3

from django.conf import settings
from sqlalchemy import create_engine
from pandas.io import sql

movies = pd.read_csv("ptt.csv").dropna(how='all')
movies["title"] = movies["title"].astype("category")
# df = pd.DataFrame.from_records(movies)
# print(df)

titles = pd.read_csv("yahoo.csv")
key_word = titles.iloc[:, 7]
# print(key_word)


# for key in key_word:
#     mask = df["title"].str.contains(key, na=False)
#     for maches in mask:
#         df["key_word"] = key
#     print(df)

# df['Match'] = df['title'].apply(matcher)

# data = []

newDF = pd.DataFrame()

for key in key_word:
    mask = movies["title"].str.contains(key)  # string compare
    movies["key_word"] = key  # Add new column
    # for x in mask:
    #     movies["key_word"] = key
    # # data.append(movies[mask])
    newDF = newDF.append(movies[mask], ignore_index=True)

# df = pd.DataFrame(data, columns=[
#     'title', 'author', 'date', 'contenttext', 'key_word'])
# print(df)
conn = sqlite3.connect('../movie_ptt/db.sqlite3')
query = '''insert or replace into moviecomm_movie(title,critics_consensus,date,duration,genre,rating,images,amount_reviews,approval_percentage) values (?,?,?,?,?,?,?,?,?)'''
conn.executemany(query, titles.to_records(index=False))
conn.commit()
# titles.to_sql('moviecomm_movie', conn, if_exists='replace', index=True)
# newDF.to_sql('moviecomm_pttmovie', conn,
#              if_exists='replace', index=False)

# user = settings.DATABASES['default']['USER']
# password = settings.DATABASES['default']['PASSWORD']
# database_name = settings.DATABASES['default']['NAME']

# database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
#     user="thomas",
#     password="5566",
#     database_name="db.sqlite3",
# )
# engine = create_engine(database_url, echo=False)

# titles.to_sql('moviecomm_movie', conn, if_exists='replace', index=True)


# newDF.to_csv('newdata.csv', index=False)
# print(newDF)


# movies[mask].to_csv('output.csv', index=False)
# print(movies[mask])


# print(mask)
# print(movies.tail(10))
