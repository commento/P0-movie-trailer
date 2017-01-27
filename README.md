# P0 Movie Trailer web page

files:

- media.py
- enterteinment_center.py
- fresh_tomatoes.py
- fresh_tomatoes.html

The class Movie is implemented in media.py
The attribute of the class Movie are:
    movie_title (str)       - Movie title
    movie_story (str)       - Movie synopsis
    movie_image (str-url)   - Movie image url
    movie_trailer (str-url) - Movie youtube trailer url
The method of the class Movie is:
    show_trailer() - visualize the trailer opening a new browser window

The main script is in enterteinment_center.py file.
The Movies are instanciated and using the fresh_tomatoes.py external library the html page is generated.
