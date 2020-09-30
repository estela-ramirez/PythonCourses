def compute(n:int)->bool:
    for x in range(2, n):
        if n%x == 0:
            return True
        else:
            return False



def main():
    num = int(input("What is the number, which you would like to primality test? "))
    if compute(num):
        print("The number", num, "is prime.")
    else:
        print("The number", num, " is not prime.")

main()
'''


import math

def prime():
    n= int(input("What is the number, which you would like to primality test? "))
    if n > 1:
        for x in range(2, n):
            if n % x == 0:
                print("The number", n, "is not prime")
                break
            else:
                print("The number", n, "is prime")
                break

prime()
        
'''




            
