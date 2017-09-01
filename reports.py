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
        answer = False
        for line in game_file:
            dates_of_production.append(int(line[date_column]))

        if int(year) in dates_of_production:
            answer = True
        return answer


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
        try:
            raise ValueError
        except ValueError:
            return "ValueError: This game is not in the file."
def main():
    pass


main()
