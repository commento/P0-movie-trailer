#import media and fresh_tomatoes
import media
import fresh_tomatoes

#instanciate 3 Movies
magnolia = media.Movie("Magnolia",
                       "It's raining frogs",
                       "http://static.rogerebert.com/uploads/movie/movie_poster/magnolia-1999/large_gHGwiXFEJ5222UiHgtm6VGCJoQI.jpg",
                       "https://www.youtube.com/watch?v=KnamcFv_N9Q")

ottoemezzo = media.Movie("8 e 1/2",
                       "A Film about a film director",
                       "http://media.cineblog.it/a/a10/otto-e-mezzo-poster2-586x868.jpg",
                       "https://www.youtube.com/watch?v=PTmiA-uNSD8")

itmwith = media.Movie("Is the Man Who Is Tall Happy?",
                       "An animated conversation about language",
                       "https://image.tmdb.org/t/p/w600/4OEbqYd4kSwAvw2PNZlr0lKlmKy.jpg",
                       "https://www.youtube.com/watch?v=d9c4xJEP6eI")

#add the movies to a list
movies = [magnolia, ottoemezzo, itmwith]

#generate the html using the fresh_tomatoes open_movies_page() method
fresh_tomatoes.open_movies_page(movies)
