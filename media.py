import webbrowser


class Movie():

    '''
    Class for Movie catalogation

    Attributes:
        movie_title (str)       - Movie title
        movie_story (str)       - Movie synopsis
        movie_image (str-url)   - Movie image url
        movie_trailer (str-url) - Movie youtube trailer url

    '''
    def __init__(self, movie_title, movie_story, movie_image, movie_trailer):

        self.title = movie_title
        self.storyline = movie_story
        self.image_url = movie_image
        self.trailer_url = movie_trailer

    def show_trailer(self):
        '''show_trailer() method visualize the trailer in a browser window'''
        traileropen = webbrowser.open(self.trailer_url)
