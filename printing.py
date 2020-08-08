import reports as rep


def input_file_name():
    file_name = input("Write the name of a data file (or \"exit\" to terminate): ")
    is_file_exist, file_path = rep.check_path(file_name)
    if file_name == "exit":
        return "exit"
    elif is_file_exist:
        return file_path
    else:
        return None


def input_count_games(file_name):
    is_running = True
    while is_running:
        amount_games = input("How many games are in the file? (Show: \"Y\" - Yes/ \"N\" - No): ")
        amount_games = amount_games.upper()
        input_list = ["Y", "N"]
        if amount_games in input_list:
            if amount_games == "Y":
                print('\033[36m', rep.count_games(file_name), '\033[0m')
                is_running = False
            else:
                break
        else:
            print('\033[31m', f"The entered value \"{amount_games}\" is incorrect!", '\033[0m')
            continue


def input_decide(file_name):
    is_running = True
    while is_running:
        year = input("Is there a game from a given year? Write a year: ")
        if year and year.isdigit():
            if 1900 <= int(year) <= 2050:
                print('\033[36m', rep.decide(file_name, year), '\033[0m')
                is_running = False
            else:
                print('\033[31m', f"The entered year \"{year}\" is incorrect!", '\033[0m')
        else:
            print('\033[31m', f"The entered year \"{year}\" is incorrect!", '\033[0m')


def input_get_latest(file_name):
    is_running = True
    while is_running:
        last_game = input("Which is the latest game? (Show: \"Y\" - Yes/ \"N\" - No): ")
        last_game = last_game.upper()
        input_list = ["Y", "N"]
        if last_game in input_list:
            if last_game == "Y":
                print('\033[36m', rep.get_latest(file_name), '\033[0m')
                is_running = False
            else:
                break
        else:
            print('\033[31m', f"The entered value \"{last_game}\" is incorrect!", '\033[0m')
            continue


def input_count_by_genre(file_name):
    is_running = True
    while is_running:
        genre = input("How many games are in the file by genre? Write a genre: ")
        if len(genre) > 1:
            print('\033[36m', rep.count_by_genre(file_name, genre), '\033[0m')
            is_running = False
        else:
            print('\033[31m', f"The entered value \"{genre}\" is incorrect!", '\033[0m')
            continue


def input_get_line_number_by_title(file_name):
    is_running = True
    while is_running:
        title = input("What is the line number of a given title? Write a title: ")
        if len(title) > 1:
            try:
                print('\033[36m', rep.get_line_number_by_title(file_name, title), '\033[0m')
                is_running = False
            except ValueError as e:
                print('\033[31m', e, '\033[0m')
        else:
            print('\033[31m', f"The entered value \"{title}\" is incorrect!", '\033[0m')
            continue


def input_sort_abc(file_name):
    is_running = True
    while is_running:
        list_title = input(
            "Can you give me the alphabetically ordered list of the titles? (Show: \"Y\" - Yes/ \"N\" - No): ")
        list_title = list_title.upper()
        input_list = ["Y", "N"]
        if list_title in input_list:
            if list_title == "Y":
                counter = 1
                for title in rep.sort_abc(file_name):
                    print(f"{counter:>4}. \033[36m{title}\033[0m")
                    counter += 1
                is_running = False
            else:
                break
        else:
            print('\033[31m', f"The entered value \"{list_title}\" is incorrect!", '\033[0m')
            continue


def input_get_genres(file_name):
    is_running = True
    while is_running:
        list_genre = input("Which genres occur in the data file? (Show: \"Y\" - Yes/ \"N\" - No): ")
        list_genre = list_genre.upper()
        input_list = ["Y", "N"]
        if list_genre in input_list:
            if list_genre == "Y":
                counter = 1
                for genre in rep.get_genres(file_name):
                    print(f"{counter:>4}. \033[36m{genre}\033[0m")
                    counter += 1
                is_running = False
            else:
                break
        else:
            print('\033[31m', f"The entered value \"{list_genre}\" is incorrect!", '\033[0m')
            continue


def input_when_was_top_sold_fps(file_name):
    is_running = True
    while is_running:
        year_fps = input(
            "What is the release year of the top sold first-person shooter game? (Show: \"Y\" - Yes/ \"N\" - No): ")
        year_fps = year_fps.upper()
        input_list = ["Y", "N"]
        if year_fps in input_list:
            if year_fps == "Y":
                try:
                    print(f" \033[36m{rep.when_was_top_sold_fps(file_name)}\033[0m")
                    is_running = False
                except ValueError as e:
                    print('\033[31m', e, '\033[0m')
            else:
                break
        else:
            print('\033[31m', f"The entered value \"{year_fps}\" is incorrect!", '\033[0m')
            continue


def goes_through_questions():
    is_asking = True
    while is_asking:
        file_name = input_file_name()
        if file_name == "exit":
            break
        elif file_name is None:
            continue

        input_count_games(file_name)
        input_decide(file_name)
        input_get_latest(file_name)
        input_count_by_genre(file_name)
        input_get_line_number_by_title(file_name)
        input_sort_abc(file_name)
        input_get_genres(file_name)
        input_when_was_top_sold_fps(file_name)

        print("\033[32m", "You have just gone through all questions.", "\033[0m")
        is_asking = False


def main():
    goes_through_questions()


main()
