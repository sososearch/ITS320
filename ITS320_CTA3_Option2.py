#------------------------------------------------------------------------
# Program Name: Calculate Tax Withholding
# Author: Musung Kim
# Date: 1/3/2021
#------------------------------------------------------------------------
# Pseudocode: This program will request a user to input their income then it looks up the tax rate from the dictionary and prints the income, tax rate, and tax.
#------------------------------------------------------------------------
# Program Inputs: Dollar amount greater than $0
# Program Outputs: Dollar amount for average tax withholding for a customer
#------------------------------------------------------------------------
#Create a program that will calculate the weekly average tax withholding for a customer, given the following weekly income guidelines:
#Income less than $500: tax rate 10%
#Incomes greater than/equal to $500 and less than $1500: tax rate 15%
#Incomes greater than/equal to $1500 and less than $2500: tax rate 20%
#Incomes greater than/equal to $2500: tax rate 30%
#Store the income brackets and rates in a dictionary.
#Write a statement that prompts the user for an income and then looks up the tax rate from the dictionary and prints the income, tax rate, and tax.
#Develop Python code that implements the program requirements.

#User Input Weekly Income
income = float(input("Enter User Income: "))

#User Income Bracket
tax_bracket = {"0-499": "10%", "500-1499": "15%", "1500-2499": "20%", "2500": "30%"}

#Income Less Than $500
if(income < 500):
    taxable = income * 0.10
    print("User taxable income is: $%.2f and tax rate is: %s" % (income, tax_bracket["0-499"]))
    print(tax_bracket["0-499"] + " of taxable income is: $%.2f" % taxable)

#Income >=$500 and <$1500
elif(income < 1500):
    taxable = income * 0.15
    print("User taxale income is: $%.2f and tax rate is: %s" % (income, tax_bracket["500-1499"]))
    print(tax_bracket["500-1499"] + " of taxable income is: $%.2f" % taxable)

#Income >=$1500 and <$2500
elif(income < 2500):
    taxable = income * 0.20
    print("User taxable income is: $%.2f and tax rate is: %s" % (income, tax_bracket["1500-2499"]))
    print(tax_bracket["1500-2499"] + " of taxable income is: $%.2f" % taxable)

#Income >=$2500
else:
    taxable = income * 0.30
    print("User taxable income is: $%.2f and tax rate is: %s" % (income, tax_bracket["2500"]))
    print(tax_bracket["2500"] + " of taxable income is: $%.2f" % taxable)
