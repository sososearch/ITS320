#------------------------------------------------------------------------
# Program Name: String Validation
# Author: Musung Kim
# Date: 12/20/2020
#------------------------------------------------------------------------
# Pseudocode: This program will request a user to input a word that is
# less than 50 characters long and checks the string against
# alphabetical characters, alphanumeric characters, digits, lowercase
# and uppercase characters.
#------------------------------------------------------------------------
# Program Inputs: Words less than 50 characters long
# Program Outputs: True or false
#------------------------------------------------------------------------
s = input("Please type a word:")
if len(s) < 50:
	print(str.isalnum(s))
	print(str.isalpha(s))
	print(str.isdigit(s))
	print(str.islower(s))
	print(str.isupper(s))
else:
	print("Input has to be less than 50 characters long.")
