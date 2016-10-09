# -*- coding: utf-8 -*-
"""
Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but instead 
is a constant amount that will be paid each month.
In this problem, we will not be dealing with a minimum monthly payment rate.
The following variables contain values as described below:

1.balance - the outstanding balance on the credit card
2.annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will 
pay off all debt in under 1 year

"""

ai = annualInterestRate

#guess initial possible fixed monthly payment
fp = round(balance/12,-1) - 10

#set initial values for monthly interest amount and remaining balance
interest = 0
rebal = balance

#loop to determine correct fixed monthly payment that satisfies the remaining balance < 0
while rebal > 0:
    
    # set  remaining balance back to initial balance
    rebal = balance
    
    #increment guess
    fp += 10
    
    #calculate remaining balance after 12 months
    for i in range(12):
        unpaid = rebal - fp
        interest = unpaid*ai/12
        rebal = round(unpaid + interest, 2)

#print result
print("Lowest Payment: ", round(fp))    