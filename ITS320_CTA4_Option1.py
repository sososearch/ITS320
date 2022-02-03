#------------------------------------------------------------------------
# Program Name: Repetition Control Structure - Five Floating Point Numbers
# Author: Musung Kim
# Date: 1/10/2021
#------------------------------------------------------------------------
# Pseudocode: This program will request a user to input values to print the total, average, maximum, minimum and interest.
#------------------------------------------------------------------------
# Program Inputs: Any real number
# Program Outputs: Total value, average, maximum, minimum and interest
#------------------------------------------------------------------------
# Write a program that utilizes a loop to read a set of five floating-point
# values from user input. Ask the user to enter the values, then print the following data:
# Total
# Average
# Maximum
# Minimum
# Interest at 20% for each original value entered by the user.
# Use the formula: Interest_Value = Original_value + Original_value*0.2

# Empty array
array = []

# 5x loop
for i in range(0, 5):
    x = float(input('Enter a number : '))
    # Add x to array
    array.append(x)

sum = 0

# Find the sum in array
for x in array:
    sum += x

# Calculate avg

avg = sum / len(array)

print('\n%15s %15s\n' % ('Original Value', 'Interest Value'))

for Original_value in array:
    # Calculate interest
    Interest_value = Original_value + Original_value * 0.2
    print('%10f %15f' % (Original_value, Interest_value))

print('\nTotal :', sum)
print('Average :', avg)
print('Maximum :', max(array))
print('Minimum :', min(array))
