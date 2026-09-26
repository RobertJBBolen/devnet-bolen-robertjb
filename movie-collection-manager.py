"""
Midterm Practical Exam — Movie Collection Manager
Student: Bolen, Robert JB B.
"""

movies = []


def display_menu():
    while True:
        # print the menu
        menu = ["1. Add a Movie", "2. View all movies", "3. Count watched vs unwatched", "4. Find a movie", "5. Exit"]

        print("=== Movie Collection Manager ===")
        for choice in menu:
            print(choice)
        # return the user's choice
        user_input = int(input("Choose an Option: "))

        if user_input == 1:
            add_movie(movies)
        elif user_input == 5:
            break   
        


def add_movie(movie_list):
    # ask for title, director, and status
    movie_title = input("Enter movie title: ")
    movie_director = input("Enter director: ")
    movie_status = input("Enter status (Watched/Unwatched): ")

    # build the movie string
    movie_info = movie_title + " - " + movie_director + " - " + movie_status
    print(f"{movie_info} movie added successfully.")

    # add it to the list
    movie_list = movie_info
    return movie_list 



def view_movies(movie_list):
    # loop through and print every movie
    # handle empty list
    pass


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():
    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


display_menu()
