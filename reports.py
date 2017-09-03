import csv


def count_games(file_name):
    with open(file_name, "r") as game_stat_file:
        game_counter = 0
        for game in game_stat_file:
            game_counter += 1
    return game_counter


def decide(file_name, year):
    with open(file_name, "r") as game_stat_file:
        game_file = csv.reader(game_stat_file, delimiter="\t")
        dates_of_production = []
        date_column = 2
        for line in game_file:
            dates_of_production.append(int(line[date_column]))

        answer = lambda year: True if int(year) in dates_of_production else False
        return answer(year)


def get_latest(file_name):
    with open(file_name, "r") as game_stat_file:
        game_file = csv.reader(game_stat_file, delimiter="\t")
        title_date_list = []
        title_column = 0
        date_column = 2
        for line in game_file:
            title_date_list.append((line[title_column], line[date_column]))

        latest_date = 0
        date_column = 1
        position_in_file = 0
        for i in range(len(title_date_list)):
            if int(title_date_list[i][date_column]) > latest_date:
                latest_date = int(title_date_list[i][date_column])
                position_in_file = i
        return title_date_list[position_in_file][title_column]


def count_by_genre(file_name, genre):
    with open(file_name, "r") as game_stat_file:
        game_file = csv.reader(game_stat_file, delimiter="\t")
        genre_list = []
        genre_column = 3
        for line in game_file:
            genre_list.append(line[genre_column].upper())

        genre_counter = 0
        for i in genre_list:
            if genre.upper() == i:
                genre_counter += 1
        return genre_counter


def get_line_number_by_title(file_name, title,):
    with open(file_name, "r") as game_stat_file:
        game_file = csv.reader(game_stat_file, delimiter="\t")
        title_dict = {}
        title_column = 0
        title_position = 1
        for line in game_file:
            title_dict[title_position] = line[title_column]
            title_position += 1

        for i in title_dict.keys():
                if title.upper() == title_dict[i]. upper():
                    return i

        if title.upper() == "HALF-LIFE 3":
            raise ValueError("""Congratulations!
                                You postponed production of Half-Life 3 by 100 years!
                                Be proude of yourself!""")

        raise ValueError("This game is not in the file.")


# Bonus functions


def bubble_sort(list_to_sort):
    for i in range(0, len(list_to_sort) - 1):
        for j in range(0, len(list_to_sort) - 1 - i):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    return list_to_sort


def sort_abc(file_name):
    with open(file_name, "r") as game_stat_file:
        game_file = csv.reader(game_stat_file, delimiter="\t")
        title_list = []
        title_column = 0

        for line in game_file:
            title_list.append(line[title_column])
        sorted_title_list = bubble_sort(title_list)
        return sorted_title_list


def get_genres(file_name):
    with open(file_name, "r") as game_stat_file:
        game_file = csv.reader(game_stat_file, delimiter="\t")
        genre_set = set()
        genre_column = 3
        for line in game_file:
            genre_set.add(line[genre_column])
        genre_list = sorted(genre_set, key=lambda x: x.upper())
        return genre_list


def when_was_top_sold_fps(file_name):
    with open(file_name, "r") as game_stat_file:
        game_file = csv.reader(game_stat_file, delimiter="\t")
        fps_list = []
        sold_copies_column = 1
        date_column = 2
        genre_column = 3
        fps = "First-person shooter"
        for line in game_file:
            if line[genre_column] == fps:
                fps_list.append((float(line[sold_copies_column]), line[date_column]))

        if fps_list == []:
            raise ValueError("There is no first-person shooter game in the file.")

        fps_list.sort(reverse=True)
        the_best_year_fps = int(fps_list[0][1])
        return the_best_year_fps


def main():
    pass


main()
