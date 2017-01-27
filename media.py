import webbrowser

class Movie():

    def __init__(self, movie_title, movie_story, movie_image, movie_trailer):
        self.title = movie_title
        self.storyline = movie_story
        self.image_url = movie_image
        self.trailer_url = movie_trailer

    def show_trailer(self):
        traileropen = webbrowser.open(self.trailer_url)
