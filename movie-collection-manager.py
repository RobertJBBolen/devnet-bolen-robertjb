"""
Midterm Practical Exam — Movie Collection Manager
Student: Bolen, Robert JB B.
"""

movies = []


def display_menu():
        # print the menu
        menu = ["1. Add a Movie", "2. View all movies", "3. Count watched vs unwatched", "4. Find a movie", "5. Exit"]

        print("=== Movie Collection Manager ===")
        for choice in menu:
            print(choice)
        # return the user's choice
        user_input = int(input("Choose an Option: "))
        return user_input
        

def add_movie(movie_list):
    # ask for title, director, and status
    movie_title = input("Enter movie title: ")
    movie_director = input("Enter director: ")
    movie_status = input("Enter status (Watched/Unwatched): ")

    # build the movie string
    movie_info = movie_title + " - " + movie_director + " - " + movie_status
    print(f"{movie_info} movie added successfully.")

    # add it to the list
    movie_list.append(movie_info)
    return movie_list 

def view_movies(movie_list):
    # loop through and print every movie
    movies_count = len(movie_list)
    if movies_count >= 1:
        print("=== All Movies ===")
        for movie in [movie_list]:
            print("\n".join(movie))
    # handle empty list
    elif movies_count == 0:
        print("No movies in the collection")
         


def count_watched_unwatched(movie_list):
    # loop through the list
    Watched = 0
    Unwatched = 0
    for movie in [movie_list]:
        movies = "".join(movie)
        split = movies.split(" - ")
        print(movies)
    # count Watched vs Unwatched
        if "watched" in split:
            Watched =+ 1
        elif "unwatched" in split:
            Unwatched =+ 1

    # return both counts
    count = f"Watched: {Watched}\nUnwatched: {Unwatched}"
    return count


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main(movies):
    # create the main menu loop
    while True:
        user_input = display_menu()
        if user_input == 1:
            movies = add_movie(movies)
        elif user_input == 2:
            movies = view_movies(movies)
        elif user_input == 3:
            count = count_watched_unwatched(movies)
            print(count)
        elif user_input == 5:
            break  
        else:
            print("Invalid Choice!")
    # call the appropriate function based on the user's choice

main(movies)

