import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()

saving_private_ryan = media.Movie("Saving Private Ryan",
                                  "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",
                                  "https://www.youtube.com/watch?v=zwhP5b4tD6g")
#saving_private_ryan.show_trailer()
three_hundred = media.Movie("300",
                            "https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg",
                            "https://www.youtube.com/watch?v=UrIbxk7idYA")
#three_hundred.show_trailer()
furious_seven = media.Movie("furious 7",
                            "https://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg",
                            "https://www.youtube.com/watch?v=Skpu5HaVkOc")
#furious_seven.show_trailer()
interstellar = media.Movie("interstellar",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")
#interstellar.show_trailer()
movies = [toy_story, avatar, saving_private_ryan, three_hundred, furious_seven, interstellar]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
