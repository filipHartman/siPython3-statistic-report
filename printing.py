from reports import *


def main():

    print("Number of games in file: ", count_games("game_stat.txt"), "\n")

    year = input("What year woluld You like to check: ")
    print(decide("game_stat.txt", year), "\n")

    print("The latest game is: ", get_latest("game_stat.txt"), "\n")

    genre = input("Enter the genre to check how many games of this genre are in file: ")
    print(count_by_genre("game_stat.txt", genre), "\n")

    title = input("Enter the title of the game to check position in the file: ")
    print(get_line_number_by_title("game_stat.txt", title), "\n")

    print(", ".join(sort_abc("game_stat.txt")), "\n")

    print(", ".join(get_genres("game_stat.txt")), "\n")

    print(when_was_top_sold_fps("game_stat.txt"))


main()
