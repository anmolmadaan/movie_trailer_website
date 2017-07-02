# movie_trailer_website
**website to view movie trailer using python**

please visit the link to view project : **http://anmolmadaan.gq/movie_trailer_website**
## media.py
### class Movie()
Having class variables **title**(for storing title of movie) , **storyline**(a short description about movie) , **poster_image_url**(link to the poster image) , **trailer_youtube_url**(link to the youtube trailer)

Having a method **show_trailer()**(to open trailer in browser window)

## entertainment_center.py
Objects for different movies are created and intialized using constructors.

# Steps to execute the project
1. Clone the repository.
2. run **index.html**

# adding more movies to page
1. open **entertainment_center.py**
2. create a new object and intialize it using constructor
   e.g. movie_name = media.Movie(movie_title, movie_storyline, image_url, youtube_url)
3. add the movie_name to movies array
   e.g. movies = [toy_story, cars, transformers, movie_name]
4. run **entertainment_center.py**
5. run **index.html**      
