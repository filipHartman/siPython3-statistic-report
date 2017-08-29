import csv


def count_game(file_name="game_stat.txt"):
    with open(file_name, "r") as game_stat_file:
        counter = 0
        for game in game_stat_file:
            counter += 1
    return counter





# def get_latest(file_name="game_stat.txt"):
#     pass
#
#
# def count_by_genre(file_name="game_stat.txt", genre):
#     pass
#
#
# def get_line_number_by_title(file_name="game_stat.txt", title):
#     pass


print(count_game())
print(decide(0))
