# Conditional statements and while loops
# Author : Veronica choi
# Date: 2024-09-27
# Version 1 
# TODO: Create a program that ask a user a question and returns a response based on the answer of the user. 


# Main loop. Keeps running until a condition is met
keep_going = ""
while keep_going == "" : 
    # Asking the user for an input to a question 
    like_coffee = input("Do you like coffee").lower()
    # .lower()converts the input to lower case

    if like_coffee == "Yes" or like_coffee == "y": 
        print("I like coffee too!")
    elif like_coffee == "No" or like_coffee == "no":
        print("You are missing out!")

    like_tea = input ("would you like tea instead?").upper()
     #upper()converts to upper case.
    if like_tea == "YES" or like_tea == "Y":
     print("Good For you . Give coffee another try!")
     print("sorry, that is all I have")
        

     
    else:
        print("I don't understand.")
    keep_going = input( "press <enter> to continue or any key to quit")
    

