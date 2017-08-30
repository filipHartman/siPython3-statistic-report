import csv


def count_games(file_name="game_stat.txt"):
    with open(file_name, "r") as game_stat_file:
        counter = 0
        for game in game_stat_file:
            counter += 1
    return counter


def decide(year, file_name="game_stat.txt"):
    with open(file_name, "r") as game_stat_file:
        game_file = csv.reader(game_stat_file, delimiter="\t")
        dates_of_production = []
        date = 2
        for line in game_file:
            dates_of_production.append(line[date])
        for i in range(len(dates_of_production)):
            if year in dates_of_production:
                return True
        return False


def get_latest(file_name="game_stat.txt"):
    with open(file_name, "r") as game_stat_file:
        game_file = csv.reader(game_stat_file, delimiter="\t")

        title_date_list = []
        title = 0
        date = 2
        for line in game_file:
            title_date_list.append((line[title], line[date]))

        latest_date = 0

        date = 1
        position_in_file = 0
        for i in range(len(title_date_list)):
            if int(title_date_list[i][date]) > latest_date:
                latest_date = int(title_date_list[i][date])
                position_in_file = i
        return title_date_list[position_in_file][title]

#
#
# def count_by_genre(file_name="game_stat.txt", genre):
#     pass
#
#
# def get_line_number_by_title(file_name="game_stat.txt", title):
#     pass


def main():
    print(count_games())
    # print(list_of_games())
    year = input("What year woluld You like to check: ")
    print(decide(year))
    print(get_latest())

main()
