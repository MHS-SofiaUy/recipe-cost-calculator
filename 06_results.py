# import libraries
import pandas


# functions go here

# instructions go here
def show_instructions():
    print('''\n
***** Instructions *****

This program will ask you for ...
- The name of the recipe you are using
- The names of the ingredients you are using
- How much of it you plan on using
- The costs for the amount of servings you plan to make
- How much it will cost per serving

It will then output an itemised list of the costs 
with subtotals for the variable and fixed costs.
Finally it will tell you how much you should use of 
each item for you to reach your serving goal.

The data will also be written to a text file which
has the same name as your recipe.

**** Program Launched! ****''')


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

# *** functions go here ***

# list
yes_no_list = ["yes", "no"]
texture_list = ["dry", "wet"]

# ask user if they want to see the instructions
want_instructions = string_checker("do you want to read the instructions (y/n)?: ", yes_no_list)

if want_instructions == "yes":
    print(show_instructions())

# get recipe name
recipe_name = not_blank("Recipe name: ", "The recipe name can't be blank.")

# loop to get component, quantity and price
ingredient_name = ""
get_ingredientprice = 0
while ingredient_name.lower() != "xxx":
    # get ingredient name
    ingredient_name = not_blank("\nIngredient: ", "The component can't be blank.")

    # if
    if ingredient_name.lower() == "xxx":
        break

    # dictionaries for units
    measurement_list = {
        "grams": "g",
        "kilograms": "kg"
    }
    measurement_list_wet = {
        "millilitres": "ml",
        "litres": "l"
    }

    # get
    measurement_unit = ""
    wet_measurement = ""
    dry_measurement = ""

    # lists to hold ingredient details
    all_ingredients = []
    all_ingredient_name = []
    all_price = []

    # Dictionary used to create data frame ie: column_name:list
    recipe_cost_dict = {
        "ingredients": all_ingredients,
        "ingredient name": all_ingredient_name,
        "price": all_price
    }

    # Call the function to start the recipe cost calculator
    recipe_cost_calculator()

    if wet_measurement:
        measurement_unit = measurement_list_wet[wet_measurement]
    elif dry_measurement:
        measurement_unit = measurement_list[dry_measurement]
    else:
        print("Invalid input. Please try again.")

    get_int = num_check("How much did you get of this ingredient? ", "Please enter an amount more than 0\n", float)
    get_cost = num_check("How much does it cost (for the amount you bought)? $", "Please enter a number more than 0\n",
                        float)
    price = num_check("How much are you using in the recipe? ", "Please enter an amount more than 0\n", float)

    # Create strings for printing...
    ingredients = ("{} - ${}".format(ingredient_name, all_price))

    # add ingredients to lists
    all_ingredients.append(ingredients)
    all_ingredient_name.append(ingredient_name)
    all_price.append(price)

# create data frame from dictionary to organise information
recipe_cost_frame = pandas.DataFrame(recipe_cost_dict)
  


# to get the price
get_serving = num_check("How many servings are you making? ", "Please enter an amount more than 0\n", float)

# calculating the price
get_totalprice = price / get_serving


# main routine goes here
total_cost = ("It costs: ${:.2f}".format(get_totalprice))


recipe = ("----- {} -----".format(recipe_name))

# list holding content to print / write to file
to_write = [recipe, all_ingredients, total_cost]

# print output
for item in to_write:
    print(item)

text_file = open("RCC_ingredients.txt", "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()





