'''
ICS 31 Week 2 Homework 1
Author: UCI_ID: 18108714  Name: EStela Ramirez Ramirez
'''


lis= [] # global area to keep track of prime numbers
max_tested_prime = max(lis) #largest variable checked for primality 
n = int(input("Enter a positive even integer: "))

def Update_Prime_List(n:int): 
    if n > 1:
        for x in range(2, n):
            if n%x == 0:
                var.append(int(input(local)))
                return Update_Prime_list

def find_smaller_primes(n:int):
    global max_tested_prime #calls global variable
    if n > max_tested_prime:
        for x in range(max_tested_prime, n):
            Update_Prime_List(n)#calls first function
            max_tested_prime = x
            return find_smaller_primes

def Goldenbach(n:int):
    find_smaller_primes(n)#calls second function
    a = n-max_tested_prime
    if a > 1:
        for x in range(2, n):
            if a%x == 0:
                print(" The two Goldbach numbers are", a, "and", max_tested_prime)

print(Update_Prime_List()) 
print(find_smaller_primes())
print(Goldenbach())         
    
    
    
