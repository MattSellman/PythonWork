import random

freq = [0]*13

str_integers1 = input("Please choose how many times the die should roll")
num = int(str_integers1)

for i in range(num):
    #compute the sum of two random numbers
    Sum = random.randint(1,6) + random.randint(1,6)

    #add on the frequency of a particular sum
    freq[Sum] += 1

for Sum in range(2,13):
    #Print a column of sums and a column of their frequencies
    x = freq[Sum] * str(Sum)
    print(Sum, "-", freq[Sum], " - ", x)