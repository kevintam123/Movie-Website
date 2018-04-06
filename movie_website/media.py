import webbrowser

class Video():
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

class Movie(Video):

    """This class provides a way to store movie related information"""
    #class (global) variable
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, poster_image, trailer_youtube)
        #self.title = movie_title
        #self.storyline = movie_storyline
        #self.poster_image_url = poster_image
        #self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TV_Show(Video):
    def __init__(self, movie_title, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, poster_image, trailer_youtube)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
