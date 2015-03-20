import webbrowser

class Video():
	"""The Video class is used to describe attributes of videos."""

	def __init__(self, video_title, video_duration, video_language):
		self.title = video_title
		self.duration = video_duration
		self.language = video_language

class Movie(Video):
	"""The Movie class is a child of the Video class, referring specifically to movies."""
	
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, video_title, video_duration, video_language, movie_storyline, poster_image, trailer_youtube):
		Video.__init__(self, video_title, video_duration, video_language)
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)