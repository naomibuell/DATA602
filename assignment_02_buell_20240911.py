
# %%
# Q1. What will the following code display?
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])
# Can you debug and fix the output? The code should return the entire list

# A: The code displays an empty list, because the print statement is for the 2nd through the 5th from last item in the list, i.e., the 1st, which yeilds nothing. The following code returns the entire list:
print(numbers)

# %%
# Q2. Design a program that asks the user to enter a store’s sales for each day of the
# week. The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.
sales = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
total = 0.0  # Initialize total

for day in range(len(days)):
    string = f"Enter sales for {days[day]}: "  # Create dynamic input message
    user_input = float(input(string))  # Expecting a numerical input
    sales.append(user_input)
    total += user_input

print("Total weekly sales = $", total)  # Print the total sales

# %%
# Q3. Create a list with at least 5 places you’d like to travel to. Make sure the list isn’t in
# alphabetical order
# ● Print your list in its original order.
# ● Use the sort() function to arrange your list in order and reprint your list.
# ● Use the sort(reverse=True) and reprint your list.
travel_list = ["Mexico city", "Machu picchu", "Seoul", "Amsterdam", "Morrocco"]
print("Here is the list in its original order:", travel_list)
travel_list.sort()
print("Here is the list sorted:", travel_list)
travel_list.sort(reverse=True)
print("Here is the list in reverse alphabetical order:", travel_list)

# %%
# Q4. Write a program that creates a dictionary containing course numbers and the room
# numbers of the rooms where the courses meet. The program should also create a
# dictionary containing course numbers and the names of the instructors that teach each
# course. After that, the program should let the user enter a course number, then it should
# display the course’s room number, instructor, and meeting time.
dict_rooms = {606: 22, 602: 400, 607: 312}
dict_profs = {606: "Bryer", 602: "Schettini", 607: "Kowalchuk"}
dict_times = {606: "8:00PM", 602: "5:00PM", 607: "8:00PM"} # Also creating a dictionary of meeting times to be displayed.

user_input = int(input("Course numbers offered are 606, 602, or 607. Please enter course number you want to look up: "))

if user_input in dict_rooms :
    print("DATA", user_input, "is taught by Professor", dict_profs[user_input], "in room", dict_rooms[user_input], "at", dict_times[user_input])
else:
    print("Course number not found. Course numbers offered are 606, 602, or 607.")

# %%
# Q5. Write a program that keeps names and email addresses in a dictionary as
# key-value pairs. The program should then demonstrate the four options:
# ● look up a person’s email address,
# ● add a new name and email address,
# ● change an existing email address, and
# ● delete an existing name and email address.
address_book = {"Naomi" : "naomi@spsmail.cuny.edu"}
print(address_book)

user_input = int(input("Above is a list of your existing contacts. Please enter 1-4 to select an option: 1 = look up an email address. 2 = add a new name and email address. 3 = change an existing email address. 4 = delete an existing name and email address. "))

# 1. look up a person’s email address,
if user_input == 1:
    input_name = input("Whose email address do you want to look up? Enter name: ")
    if input_name in address_book:
        print(input_name,"'s email is", address_book[input_name])
    else:
        print(input_name,"'s email not found.")
    
# 2. add a new name and email address,
elif user_input  == 2:
    input_name = input("Who do you want to add? Enter name: ")
    if input_name in address_book:
        print(input_name," is already in your contacts.")
    else:
        input_email = input("Enter new email address: ")
        address_book[input_name] = input_email
    
# 3. change an existing email address
elif user_input  == 3:
    input_name = input("Whose email do you want to change? Enter name: ")
    if input_name in address_book:
        input_email = input("Enter new email address: ")
        address_book[input_name] = input_email
    else:
        print(input_name,"is not in your contacts.")

# 4. delete an existing name and email address.
elif user_input  == 4:
    input_name = input("Whose contact do you want to delete? Enter name: ")
    if input_name in address_book:
        del address_book[input_name]
    else:
        print(input_name,"is not one of your contacts.")

# Handle erronous user inputs. 
else:
    print("Please enter a number between 1 through 4 to select an option.")

# End message.
print("Thank you. Here are your finalized contacts: ", address_book)