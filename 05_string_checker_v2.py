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

measurement_type = string_checker("What measurement is your ingredient in? (grams / kilograms)", 2,
                                  measurement_list)

get_int = num_check("How much did you get of this ingredient? ",
                    "Please enter an amount more than 0\n",
                    float)

get_cost = num_check("How much does it cost (for the amount you bought)? $",
                     "Please enter a number more than 0\n",
                     float)

get_amount = num_check("How much are you using in the recipe? ",
                       "Please enter an amount more than 0\n",
                       float)
# to get the price
get_price = get_cost / get_int * get_amount

print("You need: {} {}".format(get_amount, measurement_type))
print("It costs: ${:.2f}".format(get_price))
