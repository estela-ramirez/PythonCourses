'''
ICS 31 HW 8 Problem 1
Author: Name: Estela Ramirez Ramirez  UCI_ID:18108714
'''

import random   #Lottery Game Program#
from random import randint

def random_digit()->str:
    for x in range(1):
        prg_num = random.randint(10,99)
    return int(prg_num)


def present_menu():
    print("Are you ready to play the number lotto?")


def get_usr_num():
    while True:
        usr_num = input("What's your guess between 10 and 99? ")
        if usr_num == "":
          print("\nYou did not Guess!")
        elif int(usr_num) > 99 or int(usr_num) < 10:
          print("\nYour guess is not between 10 and 99.\nGuess again!")
        else:
          return int(usr_num)


def getDigits(usr_num:int)->list:
    L = []
    usr_num = get_usr_num()
    for x in str(usr_num):
        L.append(int(x))
    return L


def isMirrorMatch(num_1_digit_1:int,num_1_digit_2:int, num_2_digit_1:int, num_2_digit_2:int)-> bool:
    num_1_digit_1 = int(str(usr_num)[0])
    num_1_digit_2 = int(str(usr_num)[1])
    num_2_digit_1 = int(str(prg_num)[0])
    num_2_digit_2 = int(str(prg_num)[1])
    if (num_1_digit_1) == (num_2_digit_2) and (num_1_digit_2) == (num_2_digit_1):
        return True
    else:
        return False

    
def isDigitMatch(usr_num:int, prg_num:int)-> bool:###
    a = str(usr_num)[0]
    b = str(usr_num)[1]
    if a in str(prg_num):
        return True
    elif b in str(prg_num):
        return True
    else:
        return False


def winnings(usr_num:int, prg_num:int) -> int:
    if (usr_num) == (prg_num):
        return 10000
    elif isMirrorMatch(int(str(usr_num)[0]),int(str(usr_num)[1]), int(str(prg_num)[0]), int(str(prg_num)[1])):
        return 3000
    elif isDigitMatch(usr_num, prg_num):
        return 1000
    elif (usr_num) != (prg_num):
        return None

    
def print_winnings(usr_num:int, prg_num:int):
    cash = winnings(usr_num, prg_num)
    if cash == 10000:
        print("AMAZING! You guessed the EXACT Number! You win $10,000")
    elif cash == 3000:
        print("WOW! You guessed the reverse of the number! You win $3,000")
    elif cash == 1000:
        print("Good Job! You guessed one digit correctly! You win $1,000")
    elif cash == None:
        print("Thanks for trying, I hope you play again.")



if __name__ == "__main__":
    present_menu()
    usr_num = get_usr_num()
    prg_num = random_digit()
    #prg_num = 78
    print("Secret Number: ", prg_num)
    print_winnings(usr_num, prg_num)

    
