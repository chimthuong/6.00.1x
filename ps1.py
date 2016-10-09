# -*- coding: utf-8 -*-
"""
Problems set 1 :
Problem 1
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 

"""

vowels = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowels += 1
print("Number of vowels: ", vowels)

"""
Problem 2
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
"""
times = 0
for c in range(len(s)-2):
    if s[c] == 'b' and s[c+1] == 'o' and s[c+2] == 'b':
        times += 1
print("Number of times bob occurs is: ", times)

"""
Problem 3
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order.
"""

test = s[0]
best = ''
for i in range(1,len(s)):
    if s[i] >= s[i-1]:
        test += s[i]
    if len(test) > len(best):
        best = test
    if s[i] < s[i-1]:
        test = s[i]
print("Longest substring in alphabetical order is: ", best)

