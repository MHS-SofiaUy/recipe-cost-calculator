# import libraries
import os
import pandas
import math


# log 01/05 - recycling code, currently rewriting instructions

# functions go here

# instructions go here
def show_instructions():
    print('''\n
***** Instructions *****

This program will ask you for ...
- The name of the ingredient you are using
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


# yes no list for instructions
yes_no_list = ["yes", "no"]


# checks that users enter a valid response (eg. yes/no, cash/credit) based on a list of options
def string_checker(question, num_letters, valid_responses):
    error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])

    while True:
        response = input(question).lower()

        for items in valid_responses:
            if response == items[:num_letters] or response == items:
                return items

        print(error)


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


# checks that user has entered yes / no to a question
def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


# checks that string response is not blank
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease try again, \n".format(error))
            continue

        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# gets expenses, returns list which has the data frame and sub-total
def get_expenses(var_fixed):
    # set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ",
                              "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity: ",
                                 "The amount must be a whole number more than zero.",
                                 int)
        else:
            quantity = 1

        price = num_check("How much for a single item? $",
                          "The price must be a number <more than zero>",
                          float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # find sub-total
    sub_total = expense_frame['Cost'].sum()

    # currency formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for items in add_dollars:
        expense_frame[items] = expense_frame[items].apply(currency)

    return [expense_frame, sub_total]


# prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""


# work out profit goal and total sales required
def profit_goal(total_costs):
    # initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal...
        response = input("What is your profit goal (eg $500 or 50%) ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}. "
                                 "ie {:.2f} dollars? ,"
                                 "y / n".format(amount, amount))

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}%? , "
                                  "y / n".format(amount))
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# rounding function
def round_up(amount, rounding_to):
    return int(math.ceil(amount / rounding_to)) * rounding_to


# *** main routine goes here ***
# ask user if they want to see the instructions
want_instructions = string_checker("do you want to read the instructions (y/n)?: ", 1, yes_no_list)

if want_instructions == "yes":
    print(show_instructions())

# get product name
product_name = not_blank("Product name: ", "The product name can't be blank.")
how_many = num_check("How many items will you be producing? ",
                     "The number of items must be a whole number more than zero", int)

print()
print("Please enter your variable costs below...")
# get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y/n)? ")

if have_fixed == "yes":
    # get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0
    fixed_frame = ""

# work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# calculates total sales needed to reach goal
sales_needed = all_costs + profit_target

# ask user for rounding
round_to = num_check("Round to nearest...? $",
                     "Can't be 0", int)

# calculate recommended price
selling_price = sales_needed / how_many
recommended_price = round_up(selling_price, round_to)

# strings to be written to file

required_sales = f'\nRequired Sales: ${sales_needed:.2f}'
minimum_price_txt = f'\nMinimum Price: ${selling_price:.2f}'
profit_target_txt = f'\nProfit Target: ${profit_target:.2f}'
recommended_price_txt = f'Recommended Price: ${recommended_price:.2f}'

# write data to file

# change frames to strings
variable_txt = pandas.DataFrame.to_string(variable_frame)

if have_fixed == "yes":
    fixed_txt = pandas.DataFrame.to_string(fixed_frame)
    fixed_heading = "\n*** Fixed Costs ****"
    fixed_sub_text = f"=== Fixed Costs Sub Total: ${fixed_sub:.2f} ===="
else:
    fixed_txt = ""
    fixed_heading = ""
    fixed_sub_text = ""

to_write = [f"==== {product_name} ====",
            "\n*** Variable Costs ****",
            variable_txt,
            f"=== Variable Costs Sub Total: ${variable_sub:.2f} ====",
            fixed_heading,
            fixed_txt,
            fixed_sub_text,

            profit_target_txt,
            required_sales,

            minimum_price_txt,
            recommended_price_txt]

# *** Printing Area ***

# write to file...
# create file to hold data (add .txt extension)
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# heading
for item in to_write:
    print(item)
    text_file.write(item)
    text_file.write("\n\n")

# close file
text_file.close()

print("Saved receipt to {}".format(os.path.realpath(text_file.name)))
