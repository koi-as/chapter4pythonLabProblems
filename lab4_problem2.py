# Problem 2
# Write a program and create a function called isDivisible that takes two numbers as parameters, determines 
# the first number is divisible by the second number or not. The function should print the results. 
import sys
def isDivisible(x,y):
    if x%y==0:
        print(f'{x} is divisible by {y}')
    elif x%y!=0:
        print(f'{x} is NOT divisible by {y}')
num1=int(sys.argv[1])
num2=int(sys.argv[2])
isDivisible(num1,num2)