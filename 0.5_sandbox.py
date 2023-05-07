# calculating costs + translating from g -> kg and vice versa (RIPPED OUT CODE)
import random


# colour codes (thanks daniel for sending this and ms gottschalk for making it)


class Colour_It():

    def __init__(self, red, green, blue, text):
        self.red = red

        self.green = green

        self.blue = blue

        self.text = text

    def get_color_escape(self, red, green, blue):
        return '\033[{};2;{};{};{}m'.format(38, red, green, blue)

    def print_colour(self):
        all_coloured = self.get_color_escape(self.red, self.green, self.blue) + self.text

        return all_coloured

    def reset_colour():  # Resets the colours

        return "\033[0m"


# ******** Colours ********
# watermelon colour aesthetic
# Turquoise Text


def colour_turquoise(message):
    return Colour_It(61, 209, 182, message).print_colour()


# pink text


def colour_pink(message):
    return Colour_It(235, 75, 122, message).print_colour()


# Functions go here...
from tkinter import Y


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            # response = "yes"
            return "yes"

        elif response == "no" or response == "n":
            # response = "no"
            return "no"

        else:
            print("Please answer yes / no, if you're not sure I recommend you to press no")


def instructions():
    print()
    print(colour_turquoise(
        " ***** ~Welcome to uys0083's Trivia Game of Basic Math Equations!~ ***** {}".format(Colour_It.reset_colour())))
    print()
    print(colour_pink(
        "- In this game, the user will have a choice to answer a math equation of the following:{}".format(
            Colour_It.reset_colour())))
    print()
    print(colour_pink("- Addition, Subtraction, Multiplication and Division!{}".format(Colour_It.reset_colour())))
    print()
    print(colour_pink(
        "- The user will select the amount of rounds they wish to play, or infinite mode if they wish to do so.{}".format(
            Colour_It.reset_colour())))
    print()
    print(colour_pink(
        "- For each question, the user gets to choose which category the user wants to play with.{}".format(
            Colour_It.reset_colour())))
    print()
    print(colour_pink(
        "- After the user chooses the category of their choice, the computer will generate a random question from that category.{}".format(
            Colour_It.reset_colour())))
    print()
    print(colour_pink("- For every question, the user gets 1 attempt on answering the question correctly.{}".format(
        Colour_It.reset_colour())))
    print()
    print(colour_pink(
        "- When all the rounds are finished, or the user chooses to quit{}".format(Colour_It.reset_colour())))
    print(colour_pink("  The game will tally up the results and display the user's game statistics.{}".format(
        Colour_It.reset_colour())))
    print()
    print(colour_pink("- We wish the user to have fun!~{}".format(Colour_It.reset_colour())))
    print()
    return ""


# Main Routine goes here...

# Functions go here


def check_rounds():
    while True:
        response = input(colour_pink("How many rounds would you like to play?: ".format(Colour_It.reset_colour())))

        round_error = "Please type either <enter> or an integer that is more than 0"

        # If infinite mode not chosen, check response is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to start of loop
                if response < 1:
                    print(round_error)
                    continue

            # If response is not an integer, go back to start of loop
            except ValueError:
                print(round_error)
                continue

        # If infinite mode chosen
        elif response != "<enter>":
            print("You have selected infinite mode. Type 'xxx' if at any time you wish to quit.")

        return response


def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter of an item), the full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"

    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # checks input is not too high or too low if both upper and lower bounds are specifies
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

            # checks input is not too low
            elif situation == "low only":
                if response < low:
                    print("Please print a number that is more than (or equal to) {}".format(low))
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print("Please enter an integer")
            continue


# Ask user if they have played before
# If 'no', show instructions
played_before = yes_no(colour_turquoise("Have you played this game before? {}".format(Colour_It.reset_colour())))

if played_before == "no":
    instructions()

game_summary = []

rounds_lost = 0
rounds_won = 0
rounds_played = rounds_won + rounds_lost

# Lists of valid responses
yes_no_list = ["yes", "no"]
equation_list = ["addition", "subtraction", "multiplication", "division", "xxx"]

end_game = "no"

# ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

# Choose your equation category
choose_instruction = "Please choose addition, subtraction, multiplication, division or 'xxx' to exit "
print()
choose_error = ("{} or 'xxx' to end: ".format(choose_instruction))

# Testing to generate the numbers for the equation
while end_game == "no":
    chosen_num = random.randint(1, 100)
    chosen_num2 = random.randint(1, 100)
    table_num = random.randint(1, 12)
    table_num2 = random.randint(1, 12)
    ans = table_num * table_num2

    # ask user for choice and check it's valid
    choose = choice_checker(choose_instruction, equation_list, choose_error)
    if choose == "xxx":
        break

    # If the user chooses addition
    if choose == "addition":
        answer = int_check("Question: {} + {}  = ".format(chosen_num, chosen_num2))
        actual_ans = chosen_num + chosen_num2

    # If the user chooses subtraction
    elif choose == "subtraction":
        answer = int_check("Question: {} - {}  = ".format(chosen_num, chosen_num2))
        actual_ans = chosen_num - chosen_num2

    # If the user chooses multiplication
    elif choose == "multiplication":
        answer = int_check("Question: {} * {}  = ".format(table_num, table_num2))
        actual_ans = table_num * table_num2

    # If the user chooses division
    elif choose == "division":
        answer = int_check("Question: {} / {}  = ".format(ans, table_num2))
        actual_ans = ans / table_num2

    # compare user's input answer to the actual answer
    if answer == actual_ans:
        print("That's the correct answer. Well played.")
        print()
        rounds_won += 1
        rounds_played += 1
    else:
        print("User Response: {}".format(answer))
        print("Correct Answer: {}".format(actual_ans))
        print("No that's wrong!")
        print()
        rounds_lost += 1
        rounds_played += 1

    # End game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# show game statistics
rounds_won = rounds_played - rounds_lost

# ***** Calculate Game Stats *****
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100

print()
print(colour_turquoise("***** Math Quiz History *****{}".format(Colour_It.reset_colour())))
for game in game_summary:
    print(game)

print()

# displays game stats with % values to the nearest whole number
print(colour_turquoise("***** Quiz Statistics ***** {}".format(Colour_It.reset_colour())))
print(colour_pink("Win: {}, ({:.0f}%) \nLoss: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lose,
                                                                    (Colour_It.reset_colour()))))

# End of game statements
print()
print(colour_turquoise("**** End Quiz Summary **** {}".format(Colour_It.reset_colour())))
print(colour_pink("Won: {} \t|\t Lost: {}".format(rounds_won, rounds_lost, (Colour_It.reset_colour()))))
print()
print(colour_pink("Thanks for playing! {}".format(Colour_It.reset_colour())))

