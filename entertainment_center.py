import media  # file media is imported
import fresh_tomatoes  # fresh_tomatoes is imported

# An object is created named toy_story to store the details of movie toy story
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# An object is created named cars to store the details of movie Cars
cars = media.Movie("Cars",
                   "A hybrid between a stock car and a more"
                   "curvaceous Le Mans endurance racer.",
                   "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",  # noqa
                   "https://www.youtube.com/watch?v=WGByijP0Leo")

# An object created named transformer to store the details of movie transformer
transformers = media.Movie("Transformers",
                           "Several thousand years ago,the planet Cybertron"
                           " was consumed by a civil war by the two "
                           "Transformer factions, the Autobots led by "
                           "Optimus Prime and the Decepticons led by Megatron",
                           "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",  # noqa
                           "https://www.youtube.com/watch?v=yCOvcyfRPRk")

# Array movies created
movies = [toy_story, cars, transformers]

# open_movies_page from fresh_tomatoes is called
fresh_tomatoes.open_movies_page(movies)
