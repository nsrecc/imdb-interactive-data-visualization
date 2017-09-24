import csv
import numpy as np
import pandas as pd

# import csv
df = pd.read_csv('movie_metadata_orig.csv');

# select records with country = 'USA'
df = df[df.country == 'USA'];

# deseleect records that are TV
df = df[df.content_rating != ('TV-14')];
df = df[df.content_rating != ('TV-G')];
df = df[df.content_rating != ('TV-MA')];
df = df[df.content_rating != ('TV-PG')];
df = df[df.content_rating != ('TV-Y7')];

# deselect null records
df = df[pd.notnull(df['content_rating'])];
df = df[pd.notnull(df['title_year'])];

# create new csv
df.to_csv('movies-usa.csv', index = False);
