'''
ICS Homework 2 Problem 2
Author UCI ID: 18108714 Name: Estela Ramirez Ramirez
'''

def get_numbers():
    return int(input("How many numbers do you want to check? "))

def repeat()->list:
    L = []
    num = get_numbers()
    for x in range(num):
        ask = float(input("What is the price of this item: "))
        L.append(ask)

repeat()


def check(n:int, L:list)->list:
    L = []
    for x in L:
        if x% n == 0:
            L.append(x)
            print(L)


def check_more():
    n = int(input("The number, which you want to find multiples of: "))
    if n == 0:
       quit
    else:
        check(n, [])

check_more()


    
            
        
    


