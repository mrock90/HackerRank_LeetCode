Python represents true and false values with the bool type, which is a subtype of int. There are only two values in this type: True and False. These values can be bound to a variable:

>>> true_variable = True
>>> false_variable = False
We can evaluate Boolean expressions using the and, or, and not operators:

>>> true_variable = True and True
>>> false_variable = True and False

>>> true_variable = False or True
>>> false_variable = False or False

>>> true_variable = not False
>>> false_variable = not True
Instructions
In this exercise, you need to implement some rules from Pac-Man, the classic 1980s-era arcade-game.

You have four rules to implement, all related to the game states.

Do not worry about how the arguments are derived, just focus on combining the arguments to return the intended result.

1. Define if Pac-Man eats a ghost
Define the eat_ghost() function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man is able to eat a ghost. The function should return True only if Pac-Man has a power pellet active and is touching a ghost.

>>> eat_ghost(False, True)
...
False
2. Define if Pac-Man scores
Define the score() function that takes two parameters (if Pac-Man is touching a power pellet and if Pac-Man is touching a dot) and returns a Boolean value if Pac-Man scored. The function should return True if Pac-Man is touching a power pellet or a dot.

>>> score(True, True)
...
True
3. Define if Pac-Man loses
Define the lose() function that takes two parameters (if Pac-Man has a power pellet active and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man loses. The function should return True if Pac-Man is touching a ghost and does not have a power pellet active.

>>> lose(False, True)
...
True
4. Define if Pac-Man wins
Define the win() function that takes three parameters (if Pac-Man has eaten all of the dots, if Pac-Man has a power pellet active, and if Pac-Man is touching a ghost) and returns a Boolean value if Pac-Man wins. The function should return True if Pac-Man has eaten all of the dots and has not lost based on the parameters defined in part 3.

>>> win(False, True, False)
...
False

"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """
    # Pac-Man can eat a ghost if AND only if he has an active power pellet
    # AND he is currently touching a ghost.
    # Both conditions must be True for this action to be possible.
    return power_pellet_active and touching_ghost
    


def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    # Pac-Man scores if he is touching a power pellet OR he is touching a regular dot
    # If either those conditions (or both) are True; he has scored
    return touching_power_pellet or touching_dot
    


def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    # Pac-Man loses if he is touching a ghost and he does NOT have an active power pellet
    # The 'not' operator inverts the boolean value of power_pellet_active
    return touching_ghost and not power_pellet_active
    


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    # Pac-Man wins if all the dots have been eaten
    # However, he cannot win if he has simultaneously met the conditions to lose
    # We first determine if the losing condition is met
    player_has_lost = touching_ghost and not power_pellet_active

    # The player wins if ALL dots have been eaten AND the player has NOT lost
    return has_eaten_all_dots and not player_has_lost