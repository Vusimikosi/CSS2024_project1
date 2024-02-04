#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:27:44 2024

@author: vusani
"""

import pandas as pd
df = pd.read_csv("/Users/vusani/Documents/Project_1/.spyproject/movie_dataset.csv")
print(df)

df.dropna(inplace = True)
df = df.reset_index(drop=True)
print(df)

#highest rated movie
df.columns = df.columns.str.replace(" "," ")
print(df['Rating'].max())

movie_with_rating_9 = df[df['Rating'] == 9]
print(movie_with_rating_9)

#Average revenue of all movies
print(df['Revenue (Millions)'].mean())

#average revenue of movies from 2015 to 2017
Revenue_filtered = df[(df['Year'] >= 2015) & (df['Year'] <=2017)]
average_Revenue_filtered = Revenue_filtered['Revenue (Millions)'].mean()
print(average_Revenue_filtered)

#movies released in 2016
movies_released_in_2016 = df[df['Year'] == 2016]
print(movies_released_in_2016)

#directed by christopher nolan
movies_directed_by_christopher_Nolan = df[df['Director'] == "Christopher Nolan"]
print(movies_directed_by_christopher_Nolan)

#rating of at least 8
print(df[df['Rating'] >= 8])

movies_with_rating_at_least_8 = df[df['Rating'] >= 8]
print(movies_with_rating_at_least_8)

#median
movies_directed_by_christopher_Nolan = df[df['Director'] == "Christopher Nolan"]
median_rating_Christopher_Nolan = movies_directed_by_christopher_Nolan['Rating'].median()
print(median_rating_Christopher_Nolan)

#highest average rating
average_rating_by_year = df.groupby('Year')['Rating'].mean()
highest_average_rating = average_rating_by_year.max()
print(highest_average_rating)

year_with_highest_rating = df[df['Year'] ==7.1439]
print(year_with_highest_rating)

#percentage increase
number_movies_2006 = len(df[df['Year'] == 2006])
number_movies_2016 = len(df[df['Year'] == 2016])
percentage_increase = ((number_movies_2016 - number_movies_2006)/number_movies_2006) * 100
print(percentage_increase)

#all_actors = [actor for sublist in pd['Actors'] for actor in sublist]
#actor_counts = pd.Series(all_actors).value_counts()

#most_common_actor_count = actor_counts.max()
#print("Number of appearances:", most_common_actor_count)


#all_actors = df.Actors
#print(all_actors)
#actor_counts = pd.Series(all_actors).value_counts()
#most_common_actor_count = actor_counts.max()
#print(most_common_actor_count)


#common actor
all_actors = []
for actors_str in df['Actors']:
    actors_list = actors_str.split(',')
    all_actors.extend(actors_list)
    
actor_counts = {}
for actor in all_actors :
    if actor in actor_counts :
        actor_counts[actor] += 1
    else:
        actor_counts[actor] = 1
        

most_common_actor = max(actor_counts,
key=actor_counts.get)
count_of_most_common_actor = actor_counts[most_common_actor]

print(f"The most common actor in all the movies is {most_common_actor}"
      f"with {count_of_most_common_actor} appearances.")

#unique genre
all_genres = []
for genres_str in df['Genre'] :
    genres_list = genres_str.split(', ')
    all_genres.extend(genres_list)

unique_genres = set(all_genres)
num_unique_genres = len(unique_genres)
print(f"There are {num_unique_genres} unique genres in the dataset.")

#value = 'Guardians of the Galaxy'
#float_value = float(value)
#correlation_matrix = df.corr()
#print(f"Cannot convert '{value}' to float")


#correlation of numerical features
movies_numeric = df.drop(['Title', 'Genre', 'Description', 'Director', 'Actors'], axis=1)
correlation_matrix = movies_numeric.corr()
print(correlation_matrix)

#                        Rank      Year  ...  Revenue (Millions)  Metascore
#Rank                1.000000 -0.312809  ...           -0.273170  -0.195909
#Year               -0.312809  1.000000  ...           -0.129198  -0.062303
#Runtime (Minutes)  -0.254783 -0.101933  ...            0.281721   0.221397
#Rating             -0.243125 -0.145703  ...            0.217106   0.672731
#Votes              -0.303284 -0.362445  ...            0.636833   0.332674
#Revenue (Millions) -0.273170 -0.129198  ...            1.000000   0.142397
#Metascore          -0.195909 -0.062303  ...            0.142397   1.000000


















        

    





















