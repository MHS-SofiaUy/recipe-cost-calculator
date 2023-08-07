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

# main routine goes here

# *** functions go here ***

# list
yes_no_list = ["yes", "no"]
texture_list = ["solid", "liquid"]

# dictionaries for units
measurement_list = {
    "g",
    "kg",
}
measurement_list_wet = {
    "ml",
    "l"
}

# lists to hold ingredient details
all_ingredients = []
all_amount = []
all_price = []
all_cost = []
all_unit = []
all_texture = []
all_needed = []

# Dictionary used to create data frame ie: column_name:list
recipe_cost_dict = {
    "ingredients": all_ingredients,
    "amount": all_amount,
    "price": all_price,
    "cost": all_cost,
    "unit": all_unit,
    "texture": all_texture,
    "needed": all_needed
}

# ask user if they want to see the instructions
want_instructions = string_checker("do you want to read the instructions (y/n)?: ", yes_no_list)

if want_instructions == "yes":
    print(show_instructions())

# set maximum number of ingredients below
MAX_INGREDIENTS = 99
ingredients_listed = 0

# get recipe name
recipe_name = not_blank("Recipe name: ", "The recipe name can't be blank.")

# loop to get component, quantity and price
# ingredient_name = ""
get_ingredientprice = 0
while ingredients_listed < MAX_INGREDIENTS:
    # get ingredient name
    ingredients = not_blank("\nIngredient: ", "The component can't be blank.")

    if ingredients == 'xxx' and len(all_ingredients) > 0:
        break
    elif ingredients == 'xxx':
        print("You must write down at least ONE ingredient before quitting")
        continue

    # if
    #if ingredient_name.lower() == "xxx":
        break

    texture = string_checker("Is the ingredient a liquid or solid? ", texture_list)
    if texture == "liquid":
        unit = string_checker("Is the measurement in ml or l? ", measurement_list_wet)

    elif texture == "solid":
        unit = string_checker("Is the measurement in g or kg? ", measurement_list)

    else:
        print("Invalid input. Please enter 'wet' or 'dry'.")

    amount = num_check("How much did you get of this ingredient ({})? ".format(unit), "Please enter an amount more than 0\n", float)
    cost = num_check("How much does it cost (for the amount you bought)? $", "Please enter a number more than 0\n",float)
    price = num_check("How much are you using in the recipe ({})? ".format(unit), "Please enter an amount more than 0\n", float)

    # cost needed for AMOUNT of ingredients USED in recipe
    needed1 = cost / amount
    needed = needed1 * price

    ingredients_listed += 1

    # add to list in order to print out
    all_ingredients.append(ingredients)
    all_amount.append(amount)
    all_price.append(price)
    all_cost.append(cost)
    all_unit.append(unit)
    all_texture.append(texture)
    all_needed.append(needed)

# create panda data frame from dictionary to organise information
recipe_cost_frame = pandas.DataFrame(recipe_cost_dict)

# print out recipe name
recipe = ("----- {} -----".format(recipe_name))

# to get the price
get_serving = num_check("How many servings are you making? ", "Please enter an amount more than 0\n", float)

# calculating the price
totalprice = ("Total Price: ${:.2f}".format(sum(all_needed)))
# recipe_cost_frame['Total_Price'] = totalprice
# recipe_cost_frame['Price per serve'] = recipe_cost_frame['Total_Price'] / get_serving

per_serve = sum(all_needed) / get_serving
cost_per_serve = ("Costs per serve: ${:.2f}".format(per_serve))

print(recipe)
print(recipe_cost_frame)
print(totalprice)
print(cost_per_serve)

# list all the ingredients
# recipe_cost_frame['Recipe Ingredients'] = recipe_cost_frame['ingredients'] + recipe_cost_frame['price']

# calculate the prices per serving
# recipe_cost_frame['Price per Cost'] = recipe_cost_frame['price'] + recipe_cost_frame[totalprice]

# calculate
# recipeingredients = recipe_cost_frame['Recipe Ingredients']
# pricepercost = recipe_cost_frame['Price per Cost']

# set index before printing
# recipe_cost_calculator = recipe_cost_calculator.set_index('Name')







