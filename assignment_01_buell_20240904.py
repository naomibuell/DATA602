# Q1 Fix all the syntax and logical errors in the given source code 
# add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

high_score = 95 # Changing to lower case to match reference in if-statement later on.
 
# Get the test scores.
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
test3 = float(input('Enter the score for test 3: ')) # Added user input for test3.

# Calculate the average test score.
average = (test1 + test2 + test3) / 3 # Revised arithmetic, putting the sum of all test scores in the numerator, to generate an average.

# Print the average.
print('The average score is', average)

# If the average is a high score, congratulate the user.
if average >= high_score:
    print('Congratulations! That is a great average!') # Moving the second sentence into the if-statement.

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

# Get length and width of two rectangles.
length1 = float(input('Enter the length for rectangle 1: '))
width1 = float(input('Enter the width for rectangle 1: '))

length2 = float(input('Enter the length for rectangle 2: '))
width2 = float(input('Enter the width for rectangle 1: '))

# Print the area of both rectangles.
area1 = length1*width1
area2 = length2*width2

print('The area of rectangle 1 is', area1,'. The area of rectangle 2 is',area2,'.')

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  
name = str(input('Enter your first name: '))
age = int(input('Enter your age: '))

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"
print('Happy birthday,',name,'! You are',age ,'years old today!')
