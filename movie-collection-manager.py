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
    pass


def add_movie(movie_list):
    # ask for title, director, and status
    # build the movie string
    # add it to the list
    pass


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
