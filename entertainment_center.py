import fresh_tomatoes
import media

#Film database with title, release year, storyline, picture and trailer of each movie.

last_crusade = media.Movie("Indiana Jones 3", "1989", "The intrepid explorer Indiana Jones sets out to rescue his father, a medievalist who has vanished while searching for the Holy Grail. Following clues in the old man's notebook, Indy arrives in Venice, where he enlists the help of a beautiful academic, but they are not the only ones who are on the trail, and some sinister old enemies soon come out of the woodwork.",
	"https://upload.wikimedia.org/wikipedia/en/8/8c/Indiana_Jones_and_the_Last_Crusade.png",
	"https://www.youtube.com/watch?v=a6JB2suJYHM")

terminator_2 = media.Movie("Terminator 2", "1991", "John Connor, the key to civilization's victory over a future robot uprising, is the target of the shape-shifting T-1000, a Terminator sent from the future to kill him. Another Terminator, the revamped T-800, has been sent back to protect the boy. As John and his mother go on the run with the T-800, the boy forms an unexpected bond with the robot.",
	"https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg",
	"https://www.youtube.com/watch?v=-W8CegO_Ixw")

edge_of_tomorrow = media.Movie("Edge of Tomorrow", "2014", "When Earth falls under attack from invincible aliens, no military unit in the world is able to beat them. Maj. William Cage, an officer who has never seen combat, is assigned to a suicide mission. Killed within moments, Cage finds himself thrown into a time loop, in which he relives the same brutal fight -- and his death -- over and over again.", 
	"https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg", 
	"https://www.youtube.com/watch?v=yUmSVcttXnI")

guardians = media.Movie("Guardians of the Galaxy", "2014", "Brash space adventurer Peter Quill finds himself the quarry of relentless bounty hunters after he steals an orb coveted by Ronan, a powerful villain. To evade Ronan, Quill is forced into an uneasy truce with four disparate misfits. But when he discovers the orb's true power and the cosmic threat it poses, Quill must rally his ragtag group to save the universe.", 
	"https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg", 
	"https://www.youtube.com/watch?v=d96cjJhvlMA")

thor_ragnarok = media.Movie("Thor Ragnarok", "2017", "Imprisoned on the other side of the universe, the mighty Thor finds himself in a deadly gladiatorial contest that pits him against the Hulk, his former ally and fellow Avenger. Thor's quest for survival leads him in a race against time to prevent the all-powerful Hela from destroying his home world and the Asgardian civilization.",
	"https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
	"https://www.youtube.com/watch?v=ue80QwXMRHg")

hunt_for_the_wilderpeople = media.Movie("Hunt for the Wilderpeople", "2016",
	"A boy and his foster father become the subjects of a manhunt after they get stranded in the New Zealand wilderness.", 
	"https://upload.wikimedia.org/wikipedia/en/4/44/Hunt_for_the_Wilderpeople.png", 
	"https://www.youtube.com/watch?v=dPaU4Gymt3E")

#Assigns film instances to a movies variable.
movies = [last_crusade, terminator_2, edge_of_tomorrow, guardians, thor_ragnarok, hunt_for_the_wilderpeople]

#Opens website with films from database above included.
fresh_tomatoes.open_movies_page(movies)