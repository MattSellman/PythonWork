__author__ = 'Matthew'


n = input('what number would you like to choose? ')
a = int(str(n))


def prime(a):
    a = abs(int(a))
    if a < 2: #2 is the lowest prime number 
        return False 
    if a == 2: #also the only even one
        return True
    if not a & 1: #this is to say that any odd numbers are prime
        return False
    for x in range(3, int(a**0.5) + 1, 2): #check if num suits criteria for prime
        if a % x == 0: #
            return False
    return True

if prime(a):  #if value is true or false
    print("Your number is a prime!")
else:
    print("Your number is not prime!")
    
    
    
#str_integers = input("Please choose your number")
#n = int(str_integers)    
    
#primes = primesUpTo(n//2)
#factors = []
#for p in primes:
    #if (n%p) == 0:
        #k=1
    #while(n%(p**k))==0:
        #factors.append(p)
        #k+=1
    #if factors == []
    #factors = [n]
#return factors


# your code here
__author__ = 'Matthew'


n = input('what number would you like to choose? ')
a = int(str(n))


def prime(a):
    a = abs(int(a))
    if a < 2: #2 is the lowest prime number
        return False
    if a == 2: #also the only even one
        return True
    if not a & 1: #this is to say that any odd numbers are prime
        return False
    for x in range(3, int(a**0.5) + 1, 2): #check if num suits criteria for prime
        if a % x == 0: #
            return False
    return True

if prime(a):  #if value is true or false
    print("Your number is a prime!")
else:
    print("Your number is not prime!")



#str_integers = input("Please choose your number")
#n = int(str_integers)

#primes = primesUpTo(n//2)
#factors = []
#for p in primes:
    #if (n%p) == 0:
        #k=1
    #while(n%(p**k))==0:
        #factors.append(p)
        #k+=1
    #if factors == []
    #factors = [n]
#return factors