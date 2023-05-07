# import libraries


# *** functions go here ***

# checks that input is either a float or an
# integer that is more than zero. takes in custom error messages
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks that users enter a valid response (eg. yes/no, cash/credit) based on a list of options
def string_checker(question, num_letters, valid_responses):
    error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# main routine goes here
yes_no_list = ["yes", "no"]
measurement_list = ["grams", "kilograms"]

get_int = num_check("How much are you using in the recipe? ",
                    "Please enter an amount more than 0\n",
                    int)

measurement_type = string_checker("What measurement is your ingredient in? (grams / kilograms)", 2,
                                  measurement_list)

get_cost = num_check("How much does it cost (for the amount you're using)? $",
                     "Please enter a number more than 0\n",
                     float)

print("You need: {} {}".format(get_int, measurement_type))
print("It costs: ${}".format(get_cost))
