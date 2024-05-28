#!/usr/bin/env python3

def happy_new_year():
   number = 11
   while number>0 :
       number=number-1
       print(number)
   print("Happy New Year!")

def square_integers(int_list):
    simon =[i*i for i in int_list]
    return simon
def fizzbuzz():
   for i in range(1,101):
       if i%3==0 and i%5==0:
           print("FizzBuzz")
       elif i%3==0:
           print("Fizz")
       elif i%5==0:
           print("Buzz")
       else:
           print(i)
