# loops and indents
# Author: Veronica Choi
# Date: 20 September 2024
# Version: 1 
# TODO: 
    # Get user input (ask the user for their name)
    # Ask the user for two numbers
    # add the numbers together

# Ask the user for their name
name = input("what is your name?")
print(f"Kia ora {name}") # f stands for format. we are formating the print statement 

# Ask the user for two numbers 
num_1 = int(input("What is your favourite number"))
num_2 = int(input("What is your favourite number"))

# Add numbers together
sum = num_1 + num_2 
print(f"The numbers added together equal to {sum}")


# For loops. Repeat for a set number of times. 
# For start the loop
#next is the name of the loop
# in range tells the loop how many times to run
# the number in the () is how many times it repeats. 
for name_of_loop in range (5):
    print("ha ")

# while loop. Runs until condition is met or no longer is met.
keep_going = "" # empty variable 
while keep_going == "":
    print("Looping")
    print("still looping") 

    keep_going = input("Again? or press any other key to quit")
    