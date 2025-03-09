# lab 3.3 week 03 work
# this program reads in a string and strips any leading or trailing spaces
# Fergus McTiernan

user_input = str(input("Please enter a string: "))

stripped_string = user_input.strip()
string_lowered = stripped_string.lower()
string_length_input = len(user_input)
string_length_output = len(string_lowered)

print(f"Your string normalised is: '{string_lowered}'")
print(f"The string length of the inputted string was {string_length_input}.\nThe string length of the outputted string is {string_length_output}.")