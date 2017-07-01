import webbrowser # imported webbrowser module to access browser

# class Movie() for storing movies data title,storyline,poster_image_url,trailer_youtube_url
class Movie():
    # a constructor to initialize the variableds for an object
    def __init__(self,movie_title,movie_storyline,image_url,youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = image_url
        self.trailer_youtube_url = youtube_url
    # method to open trailer of movie on a web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
