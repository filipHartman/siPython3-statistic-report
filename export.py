from reports import *
import csv


def export_report(export_file="report_game_stat.txt"):
    with open(export_file, "w") as report_game_file:
        export_list = []
        bonus_export_list = []
        number_of_line = 1
        report = """
 _______     ________  _______     ___   _______   _________
|_   __ \   |_   __  ||_   __ \  .'   `.|_   __ \ |  _   _  |
  | |__) |    | |_ \_|  | |__) |/  .-.  \ | |__) ||_/ | | \_|
  |  __ /     |  _| _   |  ___/ | |   | | |  __ /     | |
 _| |  \ \_  _| |__/ | _| |_    \  `-'  /_| |  \ \_  _| |_
|____| |___||________||_____|    `.___.'|____| |___||_____|

"""
        export_list.append(count_games("game_stat.txt"))
        export_list.append(decide("game_stat.txt", 2004))
        export_list.append(get_latest("game_stat.txt"))
        export_list.append(count_by_genre("game_stat.txt", "RPG"))
        export_list.append(get_line_number_by_title("game_stat.txt", "Minecraft"))

        report_game_file.write(report)
        for answer in export_list:
            report_game_file.write(str(number_of_line) + ". ")
            report_game_file.write(str(answer))
            report_game_file.write("\n")
            number_of_line += 1
# Bonus fuctions
        report_game_file.write("\n---BONUS FUNCTIONS---\n")
        bonus_export_list.append(sort_abc("game_stat.txt"))
        bonus_export_list.append(get_genres("game_stat.txt"))

        for answer in bonus_export_list:
            report_game_file.write(str(number_of_line) + ".\n")
            report_game_file.write("\n".join(answer))
            report_game_file.write("\n\n\n")
            number_of_line += 1
        report_game_file.write(str(number_of_line) + ". " + str(when_was_top_sold_fps("game_stat.txt")))


def main():
    export_report()


main()
