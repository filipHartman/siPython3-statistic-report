import csv


def count_game(file_name="game_stat.txt"):
    with open(file_name, "r") as game_stat_file:
        counter = 0
        for game in game_stat_file:
            counter += 1
    return counter


# def list_of_games(file_name="game_stat.txt", games_number=count_game()):
#     with open(file_name, "r") as game_stat_file:
#         game_list = []
#         games_file = csv.reader(game_stat_file, delimiter="\t")
#         for line in games_file:
#             game_list.append(line)
#     return game_list


def decide(year, file_name="game_stat.txt"):
    with open(file_name, "r") as game_stat_file:
        game_file = csv.reader(game_stat_file, delimiter="\t")
        years_of_production = []
        for line in game_file:
            years_of_production.append(line[2])
        for i in range(count_game()):
            if year in years_of_production:
                return True
        return False


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


def main():
    print(count_game())
    # print(list_of_games())
    year = input("What year woluld You like to check: ")
    print(decide(year))


main()
