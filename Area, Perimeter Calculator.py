# Area, Perimeter Calculator 
# Author: Veronica Choi
# Date 30/10/2024
# version 1 


def intcheck(question, low, high): 
    valid = False 
    while not valid: 
        error = "Sorry! Please enter an intger between {1}" 
        "\ and {100}.format(low, high)" # This is a error checking part, to check if the user have used a number more than zero and below a hundred

keep_going = ""
while keep_going == "": # This code ask the user if they want to loop the program again. 
    How_are_you = input("How are you doing today?\n")

    if How_are_you == "no" or How_are_you == "bad" : 
        print ("Is ok your day will become better")
    elif How_are_you == "good" or How_are_you == "great" : 
        print ("That is fantastic")
    else:
        print("I don't understand")
    keep_going = input("Press <enter> to continue or any key to quit\n")  # Ask the user if they like to do the program again or like to quit.


    width = int(input("Please input a number between 1 and 100\n")) # Ask user for a number for the width of the shape
    Height = int(input("Please enter a number between 1 and 100\n")) # Ask user for a integer for the height of the shape.

    area = width * Height  # Calculates the area using the numbers chosen above
    perimeter = 2 * (width + Height) # This allows the program to calculate the perimeter of the shape

    print()
    print(f"perimeter: {perimeter} units\n")
    print(f"area: {area} square units\n")

    keep_going = input(" Please enter to keep going or any key to quit\n")
    print("Thank you for using this perimeter and area calculator, I hope you have fun")




