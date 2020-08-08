import os
from enum import Enum


game_title = 0
game_top_sold = 1
game_release = 2
game_genre = 3
game_maker = 4


def check_path(file_name):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    dir_file = os.path.join(current_dir, file_name)
    if os.path.exists(dir_file):
        return True, dir_file
    else:
        if file_name != "exit":
            print('\033[31m', f"The file \"{dir_file}\" doesn't exist!", '\033[0m')
        return False, None


class Genre(Enum):
    SURVIVAL = "Survival game"
    RPG = "RPG"
    ACTION = "Action-adventure"
    SHOOTER = "First-person shooter"
    SIMULATE = "Simulation"
    STRATEGY = "Real-time strategy"
    SANDBOX = "Sandbox"


def count_games(file_name):
    with open(file_name, "r") as line:
        i = 0
        for _ in line:
            i += 1
    return i


def decide(file_name, year):
    with open(file_name, "r") as line:
        for data in line:
            data = data.strip(os.linesep)
            list_game = data.split("\t")
            release_date = list_game[game_release]
            if int(release_date) == int(year):
                return True
        return False


def get_latest(file_name):
    with open(file_name, "r") as line:
        latest_date = 0
        title = ""
        for data in line:
            data = data.strip(os.linesep)
            game = data.split("\t")
            date = int(game[game_release])
            if latest_date < date:
                latest_date = date
                title = game[game_title]
        return title


def count_by_genre(file_name, genre):
    with open(file_name, "r") as line:
        counter = 0
        for data in line:
            data = data.strip(os.linesep)
            game = data.split("\t")
            genre_game = game[game_genre].lower()
            if genre_game == genre.lower():
                counter += 1
        return counter


def get_line_number_by_title(file_name, title):
    with open(file_name, "r") as line:
        counter = 0
        for data in line:
            counter += 1
            data = data.strip(os.linesep)
            game = data.split("\t")
            title_game = game[game_title].lower()
            if title_game == title.lower():
                return counter
        else:
            raise ValueError("There is no such title in the library!")


def sort_abc(file_name):
    with open(file_name, "r") as line:
        title_list = []
        for data in line:
            data = data.strip(os.linesep)
            game = data.split("\t")
            title_game = game[game_title]
            title_list.append(title_game)

        sorted_list = []
        while title_list:
            min_title = title_list[0]
            for title in title_list:
                if title < min_title:
                    min_title = title
            sorted_list.append(min_title)
            title_list.remove(min_title)

        return sorted_list


def get_genres(file_name):
    with open(file_name, "r") as line:
        genres_set = set()
        for data in line:
            data = data.strip(os.linesep)
            game = data.split("\t")
            genre = game[game_genre]
            genres_set.add(genre)
        genres_list = list(genres_set)
        sorted_list = []
        while genres_list:
            min_genre = genres_list[0]
            for title in genres_list:
                if title < min_genre:
                    min_genre = title
            sorted_list.append(min_genre)
            genres_list.remove(min_genre)

        return sorted_list


def when_was_top_sold_fps(file_name):
    with open(file_name, "r") as line:
        release_date = 0
        top_sold_tmp = 0.0
        is_fps = False
        for data in line:
            data = data.strip(os.linesep)
            game = data.split("\t")
            genre_game = game[game_genre]
            release_game = game[game_release]
            top_sold = game[game_top_sold]
            fps_game = Genre.SHOOTER.value
            if genre_game == fps_game:
                is_fps = True
                if top_sold_tmp < float(top_sold):
                    top_sold_tmp = float(top_sold)
                    release_date = int(release_game)
        else:
            if is_fps:
                return release_date
            else:
                raise ValueError("There is no such a genre in the library!")


if __name__ == '__main__':
    file_game = "game_stat.txt"
    print("=" * 10, "count_games", "=" * 10)
    print(count_games(file_game))
    print("=" * 10, "decide", "=" * 10)
    print(decide(file_game, 2009))
    print("=" * 10, "get_latest", "=" * 10)
    print(get_latest(file_game))
    print("=" * 10, "count_by_genre", "=" * 10)
    print(count_by_genre(file_game, Genre.SHOOTER.value))
    print("=" * 10, "get_line_number_by_title", "=" * 10)
    print(get_line_number_by_title(file_game, "World of Warcraft"))
    print("=" * 10, "sort_abc", "=" * 10)
    print(sort_abc(file_game))
    print("=" * 10, "get_genres", "=" * 10)
    print(get_genres(file_game))
    print("=" * 10, "when_was_top_sold_fps", "=" * 10)
    print(when_was_top_sold_fps(file_game))


