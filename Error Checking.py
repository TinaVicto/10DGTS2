# Error checking
# Author Veronica
# Date: 25/10/2024
# Version 1 


# Code that tests that a valid number is entered (v1)
'''done = False # Boolean variable set to False
while not done: # while loop that runs until a valid number is entered. 
    num = int(input("Please enter your value:  "))
    done = True 

print(f"The number you entered is {num}.")'''

# Code that tests that a valid number is entered (v2)
# Create a function to call everytime I ask the user for a number. 
# I can use a function over and over. To use a function, I 'call' it by writing out its name. 
'''def test_in_num(question): 
    done = False 
    while not done: 
        print(question) # The 'question is a place holder
        try: # This tries for a valid input 
            num = int(input(question))
            done = True 

        except ValueError:
            print("That is not a valid number.")  

    return(num)     # Gives back the value of num so that I can use it outside the function.     

# Main routine 
num_1 = test_in_num("Please enter your first number:")
print(f"You entered {num_1}.")
num_2 = test_in_num("Please enter your second number:")
print(f"You entered {num_2}")
num_3 = test_in_num("Please enter your third number")
print(f"You entered {num_3}")

sum = num_1 + num_2 + num_3 
print(f"The total of {num_1}, {num_2} and {num_3} is {sum}")'''


# Version 3. Refining my code. Making it more pythonic.
# Ask the user to pick a number in a range. 
def valid_num(question, low, high):
    error = f"That is not a valid number. Please enter an integer between {low} and {high}"
    while True:
        try:
            response = int(input(question))
            if low < response < high: # If response >= low and response <= high: 
                break 

            else:
                print(error)
                print()
                
        except ValueError:
            print(error)
    return response # make the value stored in the response variable available outside the loop         

# Main routine
num_1 = valid_num("enter a number between 1 and 15", 1,15)    
print(f"You entered {num_1}\n")
num_2 = valid_num ("Now enter a number between 50 and 100", 50,100)
print (f"You entered {num_2}\n")
num_3 = valid_num("Lastly enter a number between 70 and 80" , 70, 80)
print(f"You entered {num_3}\n")

# Multiply the result of num_1, num_2, and num_3
multiply = num_1 * num_2 * num_3 
print(f"Your three numbers multiplied together are equal to {multiply}\n")
sum = num_1 + num_2 + num_3 
print(f" The total of {num_1}, {num_2} and {num_3} is {sum}.\n")



