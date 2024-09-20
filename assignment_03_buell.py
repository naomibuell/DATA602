# %% [markdown]
# *Assignment 3*  
# 
# **Q1**: Write a program that prompts the user for a meal: breakfast, lunch, or dinner. Then using if statements and else statements print the user a message recommending a meal. For example, if the meal was breakfast, you could say something like, “How about some bacon and eggs?”  
# The user may enter something else in, but you only have to respond to breakfast, lunch, or dinner.

# %%
# Ask for user input.
user_input = input("Please enter a meal: breakfast, lunch, or dinner. ").lower()

# Return response recommending a meal.
if user_input == "breakfast":
    print("How about some eggs and toast?")
elif user_input  == "lunch":
    print("How about some rice and beans?")
elif user_input  == "dinner":
    print("How about some spaghetti for the table?")
else:
    print("Please enter either breakfast, lunch, or dinner.")

# %% [markdown]
# **Q2**: The mailroom has asked you to design a simple payroll program that calculates a student employee’s gross pay, including any overtime wages. If any employee works over 20 hours in a week, the mailroom pays them 1.5 times their regular hourly pay rate for all hours over 20\.   
# You should take in the user’s input for the number of hours worked, and their rate of pay.

# %%
# Ask for user input
input_hrs = float(input("Please enter the number of hours worked: "))
input_rate = float(input("Please enter your hourly pay rate: "))

# Calculate pay
if input_hrs > 20:
    overtime_hrs = input_hrs - 20
    gross_pay = overtime_hrs * input_rate * 1.5 + 20 * input_rate
    print("Your gross pay, including overtime, is $", round(gross_pay, 2))
else:
    gross_pay = input_hrs * input_rate
    print("Your gross pay is $", round(gross_pay, 2))


# %% [markdown]
# **Q3**: Write a function named times\_ten. The function should accept an argument and display the product of its argument multiplied times 10\.

# %%
# Defining function 'times_ten'
def times_ten(x):
    return x * 10

# Testing function
print(times_ten(2))
print(times_ten("shirt "))

# %% [markdown]
# **SQ4**: Find the errors, debug the program, and then execute to show the output.
# 
# def main()  
#       Calories1 \= input( "How many calories are in the first food?")  
#       Calories2 \= input( "How many calories are in the first food?")  
#       showCalories(calories1, calories2)
# 
# def showCalories()     
#    print(“The total calories you ate today”, format(calories1 \+ calories2,.2f))

# %%
# Revising code from above
def main(): # ERROR: Added missing colon when initializing function definition  
      calories1 = float(input("How many calories are in the first food?")) # ERROR: revised variable names to lower case to match references later on. Also converted inputs to be numeric.
      calories2 = float(input("How many calories are in the second food?")) # ERROR: input text to refer to second food instead of first.
      showCalories(calories1, calories2)

def showCalories(calories1, calories2): # ERROR: Added missing colon when initializing function definition. Also added input parameters.
   print("The total calories you ate today", format((calories1 + calories2),".2f")) # ERROR: corrected type of double quotation marks used, and revised parentheses. Also put ".2f" in quotes.
   
# Executing to show output
main()

# %% [markdown]
# **Q5**: Write a program that uses any loop (*while* or *for*) that calculates the total of the following series of numbers:  
#          1/30 \+ 2/29 \+ 3/28 ............. \+ 30/1

# %%
total = 0
for i in range(30):
    num = i + 1
    denom = 30 - i
    total += num/denom

print("The total of the series of numbers is", total)

# %% [markdown]
# **Q6**: Write a function that computes the area of a triangle given its base and height.  
# The formula for an area of a triangle is:  
# AREA \= 1/2 \* BASE \* HEIGHT
# 
# For example, if the base was 5 and the height was 4, the area would be 10\.  
# triangle\_area(5, 4\)   \# should print 10  

# %%
# Define triangle function
def triangle_area(base, height):
    return 1/2 * base * height

# Test function
print(triangle_area(5,4))


