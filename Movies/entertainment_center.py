import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
	"114 minutes",
	"English",
	"A story of a boy and his toys that come to life",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
	"150 minutes",
	"English",
	"A marine on an alien planet",
	"http:/upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	"http://www.youtube.com/watch?v=d1_JBMrrYw8")


almost_famous = media.Movie("Almost Famous",
	"112 minutes",
	"English",
	"A boy falls in love with music, and a girl",
	"http://upload.wikimedia.org/wikipedia/en/d/dd/Almost_famous_poster1.jpg",
	"https://youtu.be/qk0XnyrENrE")

school_of_rock = media.Movie("School of Rock",
	"95 minutes",
	"English",
	"Badass teacher gets kids excited about learning music",
	"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
	"https://youtu.be/XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
	"98 minutes",
	"English",
	"Rat takes fine dining to a new level",
	"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://youtu.be/c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
	"100 minutes",
	"English",
	"The clock strikes 12, in Paris.",
	"http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
	"https://youtu.be/5nOF93SzX6s")

movies = [toy_story, avatar, almost_famous, school_of_rock, ratatouille, midnight_in_paris]

fresh_tomatoes.open_movies_page(movies)