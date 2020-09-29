import pandas as pd
import numpy as np

movies = pd.read_csv("text.csv").dropna(how='all')
movies["title"] = movies["title"].astype("category")
# df = pd.DataFrame.from_records(movies)
# print(df)

titles = pd.read_csv("text2.csv")
key_word = titles.iloc[:, 7]
# print(key_word)


# for key in key_word:
#     mask = df["title"].str.contains(key, na=False)
#     for maches in mask:
#         df["key_word"] = key
#     print(df)

# df['Match'] = df['title'].apply(matcher)

data = []
newDF = pd.DataFrame()

for key in key_word:
    mask = movies["title"].str.contains(key)
    for x in mask:
        movies["key_word"] = key
    # data.append(movies[mask])
    newDF = newDF.append(movies[mask], ignore_index=True)

# df = pd.DataFrame(data, columns=[
#     'title', 'author', 'date', 'contenttext', 'key_word'])
# print(df)
newDF.to_csv('newdata.csv', index=False)
# print(newDF)

# movies[mask].to_csv('output.csv', index=False)
# print(movies[mask])


# print(mask)
# print(movies.tail(10))
