# -*- coding: utf-8 -*-
from movie import Movie
import fresh_tomatoes


#I prefer using a dict for the actual data. The storylines are all from IMDB, the trailers from youtube, and the poster images from wikimedia.
movieData = {
    'Amélie': {
        'trailer_url': 'https://www.youtube.com/watch?v=sECzJY07oK4',
        'director': 'Jean-Pierre Jeunet',
        'storyline': 'Amelie is an innocent and naive girl in Paris with her own sense of justice. She decides to help those around her and, along the way, discovers love.',
        'poster_image': 'https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Amelie_poster.jpg/220px-Amelie_poster.jpg'
    },
    'Donnie Darko': {
        'trailer_url': 'https://www.youtube.com/watch?v=ZZyBaFYFySk',
        'director': 'Richard Kelly',
        'storyline': 'A troubled teenager is plagued by visions of a large bunny rabbit that manipulates him to commit a series of crimes, after narrowly escaping a bizarre accident.',
        'poster_image': 'https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Donnie_Darko_poster.jpg/220px-Donnie_Darko_poster.jpg',
    },
    'Departures': {
        'trailer_url': 'https://www.youtube.com/watch?v=6UFlWO5zhO8',
        'director': 'Yōjirō Takita',
        'storyline': 'A newly unemployed cellist takes a job preparing the dead for funerals.',
        'poster_image': 'https://upload.wikimedia.org/wikipedia/en/thumb/e/e1/Okuribito_%282008%29.jpg/225px-Okuribito_%282008%29.jpg',
    }
}

#Loop through our dictionary to create our list of objects

movies = []
for title,attributes in movieData.items():
    movies.append(Movie(title, attributes['storyline'], attributes['poster_image'], attributes['trailer_url'], attributes['director']))

fresh_tomatoes.open_movies_page(movies)