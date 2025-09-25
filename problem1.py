# Problem 1
# Write a program that computes your gross pay. Your code should get two numbers: hours and rate per hour. 
# You should give the employee 1.75 times the hourly rate for hours worked above 40 hours. Use function called 
# computepay, Use try and except so that your program handles non-numeric inputs gracefully by printing a 
# message and exiting the program. 
import sys
try:
    hours=int(sys.argv[1])
    rate=int(sys.argv[2])
except:
    print('Error, please enter valid numeric info')
else:
    def computePay(h,r):
        if h>40:
            normalPay=40*r
            overtimePay=(((h-40)*r)*1.75)
            grossPay=normalPay+overtimePay
            return grossPay
        elif h<=40:
            grossPay=40*r
            return grossPay
    print(f'You earned ${computePay(hours,rate)}')
