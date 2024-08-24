''' THIS IS FROM https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna
problem statement:
You're going to write some code to help you cook a gorgeous lasagna from your favorite cookbook. You have five tasks, all related to cooking your recipe.
'''

#Test_case1: define the 'EXPECTED_BAKE_TIME' constant.

EXPECTED_BAKE_TIME = 40

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time
