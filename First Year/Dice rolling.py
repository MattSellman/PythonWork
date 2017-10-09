__author__ = 'Matthew'

import random

freq= [0]*13

str_integers1 = input("Please choose how many times the die should roll")
num = int(str_integers1)

for i in range(num):
    Sum = random.randint(1,6) + random.randint(1,6) #computing the sum of two random numbers

    freq[Sum] += 1 #add on the frequency of a particular sum

for Sum in range(2,13):
    #Print a column of sums and a column of their frequencies
    print(Sum, freq[Sum])

    #with help from a tutorial from stackoverflow
    #http://stackoverflow.com/questions/20994940/python-random-number-and-its-frequency


import random

freq= [0]*13

str_integers1 = input("Please choose how many times the die should roll")
num = int(str_integers1)

for i in range(num):
    Sum = random.randint(1,6) + random.randint(1,6) #computing the sum of two random numbers

    freq[Sum] += 1 #add on the frequency of a particular sum

for Sum in range(2,13):
    #Print a column of sums and a column of their frequencies
    print(Sum, freq[Sum])

    #with help from a tutorial from stackoverflow
    #http://stackoverflow.com/questions/20994940/python-random-number-and-its-frequency