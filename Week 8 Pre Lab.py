import random
##import math
##
##print(math.pi)
#random.seed(354) # random will always be this

for x in range(10):
    print(random.randrange(0,2), end = " ")
print()
##
##l = [1,2,4,5,66,3,3,524,45,3,2,3]
##random.shuffle(l)
##print(l)
##print()
##
##
new_list = [265,5,5,23,4324,42,525,4329]
shuffle_list = new_list.copy()
random.shuffle(shuffle_list)
print("Original List:", new_list)
print("Shuffled List:", shuffle_list)
print()
##
##
while len(shuffle_list) > 0:
    print("Removing: ", shuffle_list.pop())
##
##print()
##print("After Pop Operations: ")
##print("Original List:", new_list)
##print("Shuffled List:", shuffle_list)
##print()
##
##

official_deck = {
    "Ace of Spades" : 11,
    "Two of Spades" : 2,
    "Three of Spades" : 3,
    "Four of Spades" : 4,
    "Five of Spades" : 5,
    "Six of Spades" : 6,
    "Seven of Spades" : 7,
    "Eight of Spades" : 8,
    "Nine of Spades" : 9,
    "Ten of Spades" : 10,
    "Jack of Spades" : 10,
    "Queen of Spades" : 10,
    "King of Spades" : 10,
    "Ace of Hearts" : 11,
    "Two of Hearts" : 2,
    "Three of Hearts" : 3,
    "Four of Hearts" : 4,
    "Five of Hearts" : 5,
    "Six of Hearts" : 6,
    "Seven of Hearts" : 7,
    "Eight of Hearts" : 8,
    "Nine of Hearts" : 9,
    "Ten of Hearts" : 10,
    "Jack of Hearts" : 10,
    "Queen of Hearts" : 10,
    "King of Hearts" : 10,
    "Ace of Diamonds" : 11,
    "Two of Diamonds" : 2,
    "Three of Diamonds" : 3,
    "Four of Diamonds" : 4,
    "Five of Diamonds" : 5,
    "Six of Diamonds" : 6,
    "Seven of Diamonds" : 7,
    "Eight of Diamonds" : 8,
    "Nine of Diamonds" : 9,
    "Ten of Diamonds" : 10,
    "Jack of Diamonds" : 10,
    "Queen of Diamonds" : 10,
    "King of Diamonds" : 10,
    "Ace of Clubs" : 11,
    "Two of Clubs" : 2,
    "Three of Clubs" : 3,
    "Four of Clubs" : 4,
    "Five of Clubs" : 5,
    "Six of Clubs" : 6,
    "Seven of Clubs" : 7,
    "Eight of Clubs" : 8,
    "Nine of Clubs" : 9,
    "Ten of Clubs" : 10,
    "Jack of Clubs" : 10,
    "Queen of Clubs" : 10,
    "King of Clubs" : 10}

class Card:
    Name   = None
    Value  = None

def makeCard(name, value):
    c = Card()
    c.Name  = name
    c.Value = value
    return c


def select_Sort(Card_Deck):#sorts it by smallest number
    new_sorted_deck = []
    
    while len(Card_Deck) > 0:
        min_card = Card_Deck[0]
        min_index = 0
        for check_index in range(len(Card_Deck)):
            if Card_Deck[check_index].Value < min_card.Value:
                min_card    = Card_Deck[check_index]
                min_index   = check_index
            elif Card_Deck[check_index].Value == min_card.Value:
                if Card_Deck[check_index].Name < min_card.Name:
                    min_card    = Card_Deck[check_index]
                    min_index   = check_index
        new_sorted_deck.append(min_card)
        del Card_Deck[min_index]
    print(new_sorted_deck)
    return new_sorted_deck

def make_Card_Deck_List(my_deck):
    Card_Deck = []
    for key in my_deck:
        Card_Deck.append(makeCard(key, my_deck[key]))
        new_sorted_deck = select_Sort(Card_Deck)
        return new_sorted_deck

def print_Deck(new_sorted_deck):
    for card in new_sorted_deck:
        print(card.Name, ":", card.Value)
        
sorted_unshuffled_deck = make_Card_Deck_List(official_deck)
print_Deck(sorted_unshuffled_deck)




##def getContinue_Or_Quit():
##    choice = input("Would you like to Continue and Play Another Round (C) or Quit(Q)? ").upper().strip()
##    while choice != "C" and choice != "Q":
##        print("Invalid input, please enter C or Q.")
##        choice = input("Would you like to Continue and Play Another Round (C) or Quit(Q)? ").upper().strip()
##    return choice
##
##
##def getString(prompt, options):
##    choice = input(prompt).upper().strip()
##    while not choice in options:
##        print("Invalid input, please enter ", end = "")
##        if len(options) == 2:
##            print(options[0], "or", options[1])
##        else:
##            for option in options:
##                if option != options[-1]:
##                    print(option, end = "," )
##                else:
##                    print( " or" , option)
##        choice = input(prompt).upper().strip()
##    return choice
##
##getContinue_Or_Quit()
##getString("Would you like to Continue and Play Another Round (C) or Quit(Q)? ", ["C", "Q"])
