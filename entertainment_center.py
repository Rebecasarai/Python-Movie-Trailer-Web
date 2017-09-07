import media
import fresh_tomatoes

joy = media.Movie("Joy", "JOY is the wild story of a family across four generations centered on the girl who becomes the woman who founds a business dynasty and becomes a matriarch in her own right. Betrayal, treachery, the loss of innocence and the scars of love, pave the road in this intense emotional and human comedy about becoming a true boss of family and enterprise facing a world of unforgiving commerce.", "https://pics.filmaffinity.com/joy-380748983-large.jpg","https://www.youtube.com/watch?v=8bnBUNzz8AgI")

robinsons = media.Movie("Meet the Robinsons", "Lewis is a brilliant inventor who meets mysterious stranger named Wilbur Robinson, whisking Lewis away in a time machine and together they team up to track down Bowler Hat Guy in a showdown that ends with an unexpected twist of fate.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg0NTU4MDY5OV5BMl5BanBnXkFtZTcwMzY0MjM0MQ@@._V1_.jpg",
                        "https://www.youtube.com/watch?v=S396-fnLldk")

jobs = media.Movie("Jobs", "It only takes one person to start a revolution. The extraordinary story of Steve Jobs, the original innovator and ground-breaking entrepreneur who let nothing stand in the way of greatness. The film tells the epic and turbulent story of Jobs as he blazed a trail that changed technology",
                   "https://resizing.flixster.com/h7g_NuM11gk2PlOH7Pl8a_F6_7A=/206x305/v1.bTsxMTE3MjIxMTtqOzE3NDk5OzEyMDA7MjAyNTszMDAw", "https://www.youtube.com/watch?v=FrvkCS0ZGPU")

movies = [joy, robinsons, jobs]
fresh_tomatoes.open_movies_page(movies)
