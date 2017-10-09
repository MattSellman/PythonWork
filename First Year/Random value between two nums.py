__author__ = 'Matthew'
import random

str_integers1 = input("Please choose your first number")
first_num = int(str_integers1)

str_integers2 = input("Please choose your second number")
second_num = int(str_integers2)

number = random.randrange(first_num, second_num)
print(number)