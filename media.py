import webbrowser

class Movie():
	"""This class provides a way to store movie related information"""

	def __init__(self, movie_title, movie_year, movie_storyline, poster_image, trailer_youtube):
		'''
		1. Behaviour/functionality: Creates space in the memory for new instances.
		2. Inputs: Instance variables corresponding to the movie's title, storyline, poster and youtube trailer.
		'''
		self.title = movie_title
		self.year = movie_year
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		'''Opens YouTube trailer in web browser.'''
		webbrowser.open(self.trailer_youtube_url)