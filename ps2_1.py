# -*- coding: utf-8 -*-
"""
Write a program to calculate the credit card balance after one year if a person
 only pays the minimum monthly payment required by the credit card company 
 each month.
The following variables contain values as described below:

1.balance - the outstanding balance on the credit card
2.annualInterestRate - annual interest rate as a decimal
3.monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining 
balance. At the end of 12 months, print out the remaining balance. Be sure to 
print out no more than two decimal digits of accuracy 

"""
b = balance
ai = annualInterestRate
mp = monthlyPaymentRate
interest = 0
rebal = b + interest

#loop to calculate remaining balance after 12 months
for i in range(12):
    minpay = rebal*mp
    unpaid = rebal - minpay
    interest = unpaid*ai/12
    rebal = round(unpaid + interest, 2)

#print result
print("Remaining balance: ", rebal) 

