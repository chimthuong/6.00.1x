# -*- coding: utf-8 -*-
"""
Write a program that uses these bounds and bisection search (for more info 
 check out the Wikipedia page on bisection search) to find the smallest monthly
 payment to the cent (no more multiples of $10) such that we can pay off the 
 debt within a year. Try it out with large inputs, and notice how fast it is 
 (try the same large inputs in your solution to Problem 2 to compare!). Produce
 the same return value as you did in Problem 2.

"""

b = balance
ai = annualInterestRate
mi = ai/12

#set initial lower bound, upper bound of checking values and fixed payment
lower = round(b/12,2)
upper = round((b*(1+mi)**12)/12,2)
fp = (lower+upper)/2

#define variables
interest = 0
result = False
unpaid = 0

#run loop until correct fixed payment found
while result!=True:

    #set remaining balance back to initial balance for new check
    rebal = b
    
    #loop to calculate remaining balance for the checking fixed payment
    for i in range(12):      
        unpaid = rebal - fp
        interest = unpaid*mi
        rebal = unpaid + interest
    
    #when remaining balance > 0, ignore the half of smaller values
    if rebal > 0:
        lower = fp
        fp = (lower+upper)/2
        result = False
    
    #when remaining balance < - 1 cent, ignore the half of greater values 
    elif rebal < -0.01:
        upper = fp
        fp = (lower+upper)/2
        result = False
       
    #correct fixed payment found!
    else:
        result = True

#print result
print("Lowest Payment: ", round(fp,2))