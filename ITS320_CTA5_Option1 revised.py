#------------------------------------------------------------------------
# Program Name: String Values in Reverse Order
# Author: Musung Kim
# Date: 1/17/2021
#------------------------------------------------------------------------
# Pseudocode: This program will request a user to input 3 string values
#------------------------------------------------------------------------
# Program Inputs: Any value
# Program Outputs: Concat of the string values in reverse order
#------------------------------------------------------------------------
# Write a Python function that will accept as input three string values from a user.
# The method will return to the user a concatenation of the string values in reverse order.
# The function is to be called from the main method.
# In the main method, prompt the user for the three strings.

# Main function
def main():
    # User prompt to enter 3 string values
    print("String Values in Reverse Order ")
    st1 = str(input("Enter 1st String: "))
    st2 = str(input("Enter 2nd String: "))
    st3 = str(input("Enter 3rd String: "))

    # Print concat strings
    print("Strings in Reverse Order: ", st3[::-1]+st2[::-1]+st1[::-1])

# Call main function
main()
