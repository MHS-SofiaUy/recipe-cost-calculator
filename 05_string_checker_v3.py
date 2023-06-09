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


def string_checker(question, valid_responses):
    error = "Please choose one of the following options: {}".format(", ".join(valid_responses))

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:len(response)]:
                return item

        print(error)


def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response.strip() == "":
            print(error)
        else:
            return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# import libraries
# CHATGPT

# *** functions go here ***

# list
yes_no_list = ["yes", "no"]
texture_list = ["dry", "wet"]

# dictionaries for units
measurement_list = {
    "grams": "g",
    "kilograms": "kg"
}
measurement_list_wet = {
    "millilitres": "ml",
    "litres": "l"
}

# get ingredient name
ingredient_name = not_blank("Ingredient: ", "The component can't be blank.")
wet_measurement = ""
dry_measurement = ""


def recipe_cost_calculator():
    global wet_measurement, dry_measurement

    ingredient_type = string_checker("Is the ingredient wet or dry? ", texture_list)

    if ingredient_type == "wet":
        wet_measurement = string_checker("Is the measurement in ml or l? ", measurement_list_wet)
        # Rest of the code for wet ingredient calculation
        # ...
    elif ingredient_type == "dry":
        dry_measurement = string_checker("Is the measurement in g or kg? ", measurement_list)
        # Rest of the code for dry ingredient calculation
        # ...
    else:
        print("Invalid input. Please enter 'wet' or 'dry'.")


# Call the function to start the recipe cost calculator
recipe_cost_calculator()

get_int = num_check("How much did you get of this ingredient? ", "Please enter an amount more than 0\n", float)
get_cost = num_check("How much does it cost (for the amount you bought)? $", "Please enter a number more than 0\n",
                     float)
get_amount = num_check("How much are you using in the recipe? ", "Please enter an amount more than 0\n", float)

# to get the price
get_price = get_cost / get_int * get_amount

measurement_unit = ""

if wet_measurement:
    measurement_unit = measurement_list_wet[wet_measurement]
elif dry_measurement:
    measurement_unit = measurement_list[dry_measurement]
else:
    print("Invalid input. Please try again.")

if measurement_unit:
    print("You need: {}{}".format(get_amount, measurement_unit))
else:
    print("Invalid input. Please try again.")

print("It costs: ${:.2f}".format(get_price))
