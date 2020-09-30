'''
ICS 31 Homework 3 Problem 1
Author: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
'''
def main():
    hint_list = ["I am round.", "I can be seen during the day.",
                  "I am very hot.", "I am brihgt.", "I am in the sky."]
    introduction()
    is_Guess_correct("answer") 
    ask_question(hint_list, "answer" )
    
def is_Guess_correct(answer:str)->str: # asks the question # does not give hints, but if the guess is right/wrong it works
    hint_number = 5
    for hints in range(hint_number):
        user_answer = input("Now make a guess: ")
        if user_answer== "sun":
            print("Good job you guessed correctly!")
            break
        elif user_answer == "the sun":
            print("Good job you guessed correctly!")
            break
        else:
            print("Nope, Guess again! ")
           
def introduction():
    print("Let's play a guessing game! ")
    print("I've picked something, and I will give you five hints. ")
    print("You get to make a guess after each hint. ")
    print("If you get it right, I will let you know otherwise ")
    print("You will keep guessing until I run out of hints. ")
    print("Let's get started ")      

def ask_question(hint_list:list, answer:str): # gives hints, asks for guess
    hint_number = 5
    for x in hint_list:
        print()
        print("Here is your hint: ","\n", x)
        user_answer = input("Now make a guess: ")
        user_answer = user_answer.lower()
        hint_number -=1
        

        if hint_number < 1: 
            print("\n","Ohh, I must not have given good hints. I was the sun. ")

main()





