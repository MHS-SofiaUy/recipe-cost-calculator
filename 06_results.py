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
    all_amount = []
    all_price = []
    all_cost = []
    all_unit = []

    # Dictionary used to create data frame ie: column_name:list
    recipe_cost_dict = {
        "ingredients": all_ingredients,
        "amount": all_amount,
        "price": all_price,
        "cost": all_cost,
        "unit": all_unit
    }

    # Call the function to start the recipe cost calculator
    unit = recipe_cost_calculator()

    if wet_measurement:
        measurement_unit = measurement_list_wet[wet_measurement]
    elif dry_measurement:
        measurement_unit = measurement_list[dry_measurement]
    else:
        print("Invalid input. Please try again.")

    amount = num_check("How much did you get of this ingredient? ", "Please enter an amount more than 0\n", float)
    cost = num_check("How much does it cost (for the amount you bought)? $", "Please enter a number more than 0\n",
                        float)
    price = num_check("How much are you using in the recipe? ", "Please enter an amount more than 0\n", float)

    # collecting ingredient name
    ingredients = (ingredient_name)

    # add to list in order to print out
    all_ingredients.append(ingredients)
    all_amount.append(amount)
    all_price.append(price)
    all_cost.append(cost)
    all_unit.append(unit)

# main routine goes here

# to get the price
get_serving = num_check("How many servings are you making? ", "Please enter an amount more than 0\n", float)

# calculating the price
totalprice = price / get_serving


total_costs = ("It costs: ${:.2f}".format(totalprice))

# create panda data frame from dictionary to organise information
recipe_cost_frame = pandas.DataFrame(recipe_cost_dict)
print(recipe_cost_frame)

# list all the ingredients
recipe_cost_frame['Recipe Ingredients'] = recipe_cost_frame['ingredients'] + recipe_cost_frame['price']

# calculate the prices per serving
recipe_cost_frame['Price per Cost'] = recipe_cost_frame['price'] + recipe_cost_frame[totalprice]

# calculate
recipeingredients = recipe_cost_frame['Recipe Ingredients']
pricepercost = recipe_cost_frame['Price per Cost']

# set index before printing
recipe_cost_calculator = recipe_cost_calculator.set_index('Name')

# print out ingredients
recipe = ("----- {} -----".format(recipe_name))





