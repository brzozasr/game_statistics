import os
import sys

import reports as rep


def is_date_correct(str_date):
    try:
        num = int(str_date)
        if num < 1950 or num > 2050:
            return False
    except ValueError:
        return False
    return True


def check_argv():
    if len(sys.argv) == 6:
        path, source_file, target_file, input_year, input_genre, input_title = sys.argv
        is_file_exist, file_path = rep.check_path(source_file)
        file, extension = os.path.splitext(target_file)
        if not is_file_exist:
            return False
        elif extension != ".txt":
            print('\033[31m', "There is something wrong with the target file (\".txt\" extension is required!)",
                  '\033[0m')
            return False
        elif not is_date_correct(input_year):
            print('\033[31m', f"The entered year \"{input_year}\" is incorrect!", '\033[0m')
            return False
        elif len(input_genre) < 1:
            print('\033[31m', f"The entered genre \"{input_genre}\" is incorrect!", '\033[0m')
            return False
        elif len(input_title) < 1:
            print('\033[31m', f"The entered title \"{input_title}\" is incorrect!", '\033[0m')
            return False
        else:
            return True
    else:
        print('\033[31m', "There is missing argument!", '\033[0m')
        return False


def export_to_file():
    if check_argv():
        path, source_file, target_file, input_year, input_genre, input_title = sys.argv
        current_dir = os.path.dirname(os.path.realpath(__file__))
        dir_source = os.path.join(current_dir, source_file)
        dir_target = os.path.join(current_dir, target_file)
        title_no = ""
        try:
            title_no = str(rep.get_line_number_by_title(dir_source, input_title))
            is_written = True
        except ValueError as e:
            is_written = False
            print('\033[31m', e, '\033[0m')
        if is_written:
            list_to_write = [str(rep.decide(dir_source, int(input_year))),
                             str(rep.count_by_genre(dir_source, input_genre)), title_no]
            with open(dir_target, "w") as line:
                for data in list_to_write:
                    line.write(data + "\n")

            print('\033[36m', "Data has been written to the file!", '\033[0m')
        else:
            print('\033[31m', "Data has not been written to the file!", '\033[0m')
    else:
        print('\033[31m', "Data has not been written to the file!", '\033[0m')


export_to_file()
