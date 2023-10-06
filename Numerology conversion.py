# Welcome to the number input, single converter. Numerology

# Welcome to the numerology breakdown, you can enter any number and it will breakdown to the single digit.

# The code is related to numerolgy
# In numerology, various calculations are performed based on a person's birth date and name 
# to derive a "life path number," "destiny number," "expression number," and other numerological attributes.

# I need to include the meaning of each number and then a pattern animation.

def add_digits(num): # This is a function called add_digits, it will calculate the final result and keeps track of the steps taken, wooh!
    zsteps = [] # Leave null 
    while num >= 10: # As long as the result is equal to or greater than 10, it will separate and add the numbers. Another way of saying anything that is double digit.
        digits = list(map(int, str(num)))
        zstep_result = sum(digits)
        zsteps.append(f"{'+'.join(map(str, digits))} = {zstep_result}")
        num = zstep_result
    return num, zsteps

while True:
    user_input = input("Enter a number or 'quit' to exit: ") # Input the sequence of numbers, single, dates, etc Also allowing the user to quit. 
    
    if user_input.lower() == 'quit': # At the moment, it doesnt go anywhere.
        break

    if not user_input.isdigit(): # Request user input
        print("Please enter a sequence of numbers.")
        continue

    input_number = int(user_input) # Single, no decimal at the moment
    result, zsteps = add_digits(input_number)
    print(f"Your number sequence final result is: {result}")

    ask_question = input("Would you like to see the breakdown of how it was solved? (yes/no): ") # For those who are intersted in knowing how it works.
    if ask_question.lower() == "yes":
        for step in zsteps:
            print(step)

