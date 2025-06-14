Python is a dynamic and strongly typed programming language. It employs both duck typing and gradual typing via type hints.

While Python supports many different programming styles, internally everything in Python is an object. This includes numbers, strings, lists, and even functions.

We'll dig more into what all of that means as we continue through the track.

This first exercise introduces 4 major Python language features:

Name Assignment (variables and constants),
Functions (the def keyword and the return keyword),
Comments, and
Docstrings.

"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# define the 'EXPECTED_BAKE_TIME' constant below.
EXPECTED_BAKE_TIME = 40

# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.
PREPARATION_TIME_PER_LAYER = 2


# Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_time


# Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - the number of lasagna layers.
    :return: int - total preparation time (in minutes).

    Function that takes the number of layers in the lasagna as an argument
    and returns how many minutes it takes to prepare the lasagna.
    """
    total_preparation_time = number_of_layers * PREPARATION_TIME_PER_LAYER
    return total_preparation_time


# define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - the amount of time the lasagna has already baked.
    :return: int - total elapsed time (in minutes) up to that point.

    Function that takes two numbers representing the number of layers and the time already
    spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    total_elapsed_time = preparation_time + elapsed_bake_time
    return total_elapsed_time
    


# Remember to go back and add docstrings to all your functions
# (you can copy and then alter the one from bake_time_remaining.)