import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_pjt.settings")
import django
django.setup()
import requests
from tmdb import TMDBHelper
from movies.models import Movie, Genre, Directors, Actors
from django.shortcuts import get_object_or_404


tmdbhelper = TMDBHelper('fc736c578445be44e87a385015c5331d')

# 영화 리스트
movie_list = []
for list_id in range(1, 10):
    url = tmdbhelper.get_request_url(method=f'/list/{list_id}', language='ko', region='KR')
    response = requests.get(url).json()

    if 'items' in response.keys():
        movie_list += response['items']
    
# 중복제거
movie_list = list({movie['id']: movie for movie in movie_list}.values())


# 장르 리스트
url = tmdbhelper.get_request_url(method='/genre/movie/list', language='ko', region='KR')
response = requests.get(url).json()

for res in response['genres']:
    Genre.objects.create(id = int(res['id']), name = res['name'])

for movie in movie_list:
    movie_obj = Movie.objects.create(
        title = movie['title'],
        overview = movie['overview'],
        release_date = movie['release_date'],
        poster_path = movie['poster_path'],
    )

    for genre_pk in movie['genre_ids']:
        genre = get_object_or_404(Genre, pk=genre_pk)
        movie_obj.genres.add(genre)

    movie_id = movie['id']
    url = tmdbhelper.get_request_url(method=f'/movie/{movie_id}/credits', language='ko', region='KR')
    response = requests.get(url).json()

    for cast in response['cast'] :
        if cast['cast_id'] < 10 :
            actor = Actors.objects.get_or_create(id = int(cast['id']), name = cast['name'])[0]
            movie_obj.actors.add(actor)

    for crew in response['crew'] :
        if crew['department'] == 'Directing' :
            director = Directors.objects.get_or_create(id = int(crew['id']), name = crew['name'])[0]
            movie_obj.directors.add(director)

