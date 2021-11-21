# import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast
import pickle
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_pjt.settings")
import django
django.setup()
from movies.models import Movie
import requests
from tmdb import TMDBHelper
from movies.models import Movie, Genre, Director, Actor, Keyword
from django.shortcuts import get_object_or_404

# tmdbhelper = TMDBHelper('fc736c578445be44e87a385015c5331d')

# def RecommendedSystem():
#     movies = Movie.objects.all()
#     col = {'movie_id':[], 'title': [], 'tags':[]}
#     movie_tags = pd.DataFrame(col)
#     for movie in movies:
#         movie_id = movie.movie_id
#         url = tmdbhelper.get_request_url(method=f'/movie/{movie_id}')
#         response = requests.get(url).json()
#         tag = [response['overview']]
#         keywords = movie.keywords.all()
#         for k in keywords:
#             tag.append(k.name)

#         genres = movie.genres.all()
#         for g in genres:
#             tag.append(g.name)

#         actors = movie.actors.all()
#         for a in actors:
#             tag.append(a.name)

#         directors = movie.directors.all()
#         for d in directors:
#             tag.append(d.name)
#         tag = ' '.join(tag)
#         data = {'movie_id': int(movie.id), 'title': movie.title, 'tags': tag}
#         movie_tags = movie_tags.append(data, ignore_index=True)
    
#     movie_tags.to_csv('movie_tags.csv')


def recommend(movie):
    movie_tags = pd.read_csv('movie_tags.csv')
    lv = TfidfVectorizer(max_features=5000, stop_words='english')
    vector = lv.fit_transform(movie_tags['tags']).toarray()
    similarity = cosine_similarity(vector)

    index = movie_tags[movie_tags['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(movie_tags.iloc[i[0]].title)
    
