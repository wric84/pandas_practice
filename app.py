# print("Hello World")
import pandas as pd
import numpy as np

shows = pd.DataFrame({
    # key : value
    "show_id":[101, 102, 103, 104, 105],
    "title": ["Star Wars", "RuPaul", "Knives Out", "Alien", "Batman"],
    "genre": ["Sci-fi", "Reality","Mystery", "Sci-Fi", "Action"]
})

shows.to_csv("shows.csv", index=False)

users = pd.DataFrame({
    "user_id":[1,2,3,4,5],
    "name": ["Alice", "Bob", "Charlie", "Dana", "Eli"],
    "country":["USA", "USA", "Canada", "UK", "USA"]
})
users.to_csv("users.csv", index=False)

watch = pd.DataFrame({
    "user_id":[1,1,2,3,4,5,2,3],
    "show_id": [101,102,101,104,103,101,104,102],
    "watch_minutes":[50,30,45,60,40,25,35,20],
    "date":["2026-01-01","2026-01-02","2026-01-01","2026-01-03","2026-01-01","2026-01-02","2026-01-03","2026-01-01"]
})

watch.to_csv("watch_history.csv", index=False)

# print(shows)
# print("\n",users)
# print("\n",watch)

shows = pd.read_csv("shows.csv")
users = pd.read_csv("users.csv")
watch = pd.read_csv("watch_history.csv")

print(watch.head())

watch.loc[2, "watch_minutes"] = np.nan

print(watch.loc[2, "watch_minutes"])
print(watch.head())

print(watch.isnull().sum())

watch["watch_minutes"] = watch["watch_minutes"].fillna(0)
print(watch.head())

new_watch = pd.DataFrame({
    "user_id":[1,4],
    "show_id": [103,101],
    "watch_minutes":[50,30],
    "date":["2026-01-05", "2026-01-05"]
})

print(new_watch)
watch = pd.concat([watch, new_watch])
print(watch)

# merge tables together
watch_shows = pd.merge(
    watch,
    shows,
    on="show_id"
)
print(watch_shows)

# SELECT genre, SUM(watch_minutes)
# FROM data
# GROUP BY genre
genre_watch = watch_shows.groupby("genre")["watch_minutes"].sum()

print(genre_watch)

full_data = pd.merge(
    watch_shows,
    users,
    on="user_id"
)

print(full_data)
title_watch = full_data.groupby("title")["watch_minutes"].sum()
print(title_watch)

user_watch = full_data.groupby("name")["watch_minutes"].sum()
print(user_watch)

genre_stats = full_data.groupby("genre").agg({
    "watch_minutes":["sum", "mean", "max"]
})

print(genre_stats)

title_stats = full_data.groupby("title").agg({
    "watch_minutes":["sum", "mean", "max"]
})

print(title_stats)

full_data["title_avg"] = full_data.groupby("title")["watch_minutes"].transform("mean")
print(full_data)

full_data["genre_avg"] = full_data.groupby("genre")["watch_minutes"].transform("mean")
print(full_data)

full_data["genre"] = full_data["genre"].replace({
    "Sci-fi":"Sci-Fi"
})

pivot = pd.pivot_table(
    full_data,
    values="watch_minutes",
    index = "country",
    columns="genre",
    aggfunc="sum"
)

print(pivot)