#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)
digit = abs(number) % 10
signed_digit = -digit if number < 0 else digit

if signed_digit > 5:
   print (f"Last digit of {number} is {signed_digit} and is grater than 5")
elif signed_digit == 0:
   print (f"Last digit of {number} is {signed_digit} and is zero")
else:
   print (f"Last digit of {number} is {signed_digit} and is less than 6 and not 0")
