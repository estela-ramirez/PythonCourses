'''
ICS 31 Homework 9 Prblem 2
Driver: UCI_ID: 18108714 Name:EStela Ramirez Ramirez
'''
'''
Factorial and Fibonacci:
'''
import math

def factorial(n: int) -> int:
    if n <=1:
        return 1
    else:
        return n* factorial(n-1)


def print_factorial():
    for x in range(1, 21):
        print(x,"!=\t", factorial(x), "\n", sep ="")
       

def fibonacci(n:int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
   
def print_fibonacci():
    for x in range(1, 21):
        print("Fib #", x,"\t=", fibonacci(x), "\n", sep = "")
    
    
def main():
    print("These are the first 20 Factorials:\n")
    print_factorial()
    print("\nThese are the first 20 Fibonacci:\n")
    print_fibonacci()

if __name__ == "__main__":
    main()

