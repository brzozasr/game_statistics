# Game statistics

## Story

You are a software architect at game developer company named Eastwood Studios.
Judy, a colleague from sales, asks you to help her in a competitor
evaluation project. She has lots of data files with statistical
information about famous games of all time. Judy has some unanswered
questions about the games and expects you to write a program that
can answer these questions.

There is an additional request: Judy likes to explore the data
manually, and for that she needs a simple terminal interface
where she can pick her questions, type the required inputs, and
gets the answer printed on the screen. On the other hand,
there are a large number of files that need to be processed
so you also need a way to answer the questions programmatically
and save them into a target file.

Since you are an architect you cannot help
but use a modular structure where no code is duplicated and
the responsibilities are strictly separated. So you decide
to create three modules: `reports`, `printing`, and `export`
to cover all the requested features.

## What are you going to learn?

You will learn and practice the following topics:

- using modules,
- conforming to test requirements,
- filtering data,
- working with files,
- handling errors,
- following clean code practices.

## Tasks

1. "How many games are in the file?" - asks Judy. Implement `count_games(file_name)` that answers this question. The expected output of the function is a number.
    - The function returns the number of games (as a number) based on the given data file

2. "Is there a game from a given year?" - asks Judy. Implement `decide(file_name, year)` that answers this question. The expected output of the function is a boolean value.
    - The function returns the `True` or `False` that answers the question based on the given data file

3. "Which is the latest game?" - asks Judy. Implement `get_latest(file_name)` that answers this question. The expected output of the function is the title of the latest game. If there is more than one then return the first title from the file.
    - The function returns the title that answers the question based on the given data file

4. "How many games are in the file by genre?" - asks Judy. Implement `count_by_genre(file_name, genre)` that answers this question. The expected output of the function is a number.
    - The function returns the number of games of the given genre (as a number) based on the given data file

5. "What is the line number of a given title?" - asks Judy. Implement `get_line_number_by_title(file_name, title)` that answers this question based on the given data file. The expected output of the function is a number. If the title is not found then it should raise a `ValueError` exception.
    - The function returns the number of games of the given (as a number) based on the given data file
    - The function raises a `ValueError` exception if the title is not found in the given data file

6. "Can you give me the alphabetically ordered list of the titles?" - asks Judy. Implement `sort_abc(file_name)` that answers this question based on the given data file. The expected output of the function is a list of titles. _Do not use the `sort` method or the built-in `sorted`, `min`, and `max` functions, implement an easy sort algorithm on your own!_
    - The function returns the sorted list of the titles based on the given data file
    - The code uses a custom sort algorithm implementation not using the forbidden functions

7. "Which genres occur in the data file?" - asks Judy. Implement `get_genres(file_name)` that answers this question based on the given data file. The expected output of the function is a list of the genres without duplicates, in alphabetical order. _Do not use the `sort` method or the built-in `sorted`, `min`, and `max` functions, implement an easy sort algorithm on your own!_
    - The function returns the sorted list of the unique genres based on the given data file
    - The code uses a custom sort algorithm implementation not using the forbidden functions

8. "What is the release year of the top sold first-person shooter game?" - asks Judy. Implement `when_was_top_sold_fps(file_name)` that answers this question based on the given data file. The expected output of the function is the year of the release (as a number). If there is no first-person shooter game in the data file then it should raise a `ValueError` exception.
    - The function returns the release year of the top sold first-person shooter game based on the given data file
    - The function raises a `ValueError` exception if the FPS genre is not found in the given data file

9. The three modules share the responsibilities as described in the introduction: `reports` contains the functions providing the answers, `printing` asks for user input and prints output to the terminal, `export` gets the required input parameters as command line arguments, then saves the results. The latter two modules call `reports`'s core functions.
    - The `reports` module does not ask for user input and does not print anything.
    - The `printing` module asks for user input, first for the name of a data file, then it goes through all the questions, asks for the extra arguments, and prints the results to the screen.
    - The `printing` module does not exit on `reports`'s exceptions but handles them and communicates them with the user.
    - The `printing` module does not implement the answers themselves but imports `report` (and does not import `export`).
    - The `export` module needs command line arguments in this form `python3 export.py source_file_name target_file_name input_year input_genre input_title` where the last 3 are arguments for questions #2, #4, and #5, respectively. The results are saved into a file `target_file_name`, the individual answers written into new lines.
    - The `export` module does not exit on `reports`'s exceptions but handles them and sends informative text snippets to the output instead.
    - The `export` module does not implement the answers themselves but imports `report` (and does not import `printing`).

## General requirements

- Variable names in the program are meaningful nouns and not abbreviated
- Function names in the program are meaningful verbs and not abbreviated
- There are no unnecessary (dead) code parts or comments in the program
- There are no duplicating code parts or code parts doing the same thing differently in the program
- There are no functions doing more than one thing in the program
- There are no external imports in the program

## Hints

- Check your code by running `test.py` after implementing each function!
- You should keep in mind: [Don't repeat yourself](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)!
  When a piece of code appears on multiple locations, try to extract it
  into a function.
- Also add some _abstraction_ if it helps you to reduce the code
  (like using parameters to unify similar snippets in one function).
- Your functions need to process any input files with the same structure
  as `game_stat.txt`. Every line contains the **title**, the **copies sold**
  (in millions), the **release year**, the **genre**, and the **publisher** of a
  popular computer game. The columns are separated by tab characters like
  `Minecraft⟶23⟶2009⟶Survival game⟶Microsoft↲`.
  Create files with the same structure but
  different data and test your solution on them!
- Avoid magic numbers.
- Command line arguments separated with space by default. If you would like to provide a single command line argument which contains space, you should put into quotation mark, e.g.: "Electronic Arts"

## Starting your project

To start your project click [this link](https://journey.code.cool/v2/project/solo/blueprint/game-statistics/python).

## Background materials

- <i class="far fa-exclamation"></i> [File handling](https://learn.code.cool/full-stack/#/../pages/python/file-handling)
- <i class="far fa-exclamation"></i> [Error handling in Python](https://python-textbok.readthedocs.io/en/stable/Errors_and_Exceptions.html)
  (until the section "Debugging programs")
- <i class="far fa-exclamation"></i> [About Python modules](https://realpython.com/python-modules-packages/)
  (until the section "Python Packages")
- <i class="far fa-exclamation"></i> [Magic numbers](https://learn.code.cool/full-stack/#/../pages/general/magic-numbers)
- <i class="far fa-exclamation"></i> [Clean code](https://learn.code.cool/full-stack/#/../pages/general/clean-code)
- [Command line arguments in Python](https://www.pythonforbeginners.com/system/python-sys-argv)
