import random
from random import randint
import unittest

my_deck = {
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

def makeCard(name:str,value:int)->Card:
    c = Card()
    c.Name = name
    c.Value = value
    return c
    
class Bets:
    player_funds    = 0		
    player_bet      = 0	

def make_bets(player_funds, player_bet)->Bets:
    b = Bets()
    b.player_funds = player_funds
    b.player_bet = player_bet
    return b


def select_Sort(Card_Deck:[Card]) -> [Card]: #sorts it manually
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
    return new_sorted_deck


def make_Card_Deck_List(my_deck:[{str:int}]) -> [Card]: 
    Card_Deck = []
    for key in my_deck:
        Card_Deck.append(makeCard(key, my_deck[key]))
    return Card_Deck


def make_standard_Card_Deck_List(my_deck:[{str:int}]) -> [Card]:#could go back to original
    Card_Deck = make_Card_Deck_List(my_deck)
    new_sorted_deck = select_Sort(Card_Deck)
    return new_sorted_deck
    

def print_Deck(card_deck_list:[Card]):
    for card in card_deck_list:
        print(card.Name, ":", card.Value)


def generate_shuffled_deck(full_deck:[Card]) -> [Card]:
    Card_Deck = make_Card_Deck_List(my_deck)


##def menu():
##
##def intro_message():
##    print("Hello and Welcome to the Friend Computer's BlackJack Table!")
##    print("At the Friend Computer's BlackJack Tables the closest player to 21, with a value less than 21 wins!")
##    print("If you exceed 21, you lose. If the computer has card values closer to 21, you lose.")
##    print("If you are closer to 21 than the computer, then you win!")
##    print("Note: Ace defaults to 11, but will change to 1, should you exceed 21.")
##    print("Also Beware the Friend Computer NEVER turns down a bet and is infinitely wealthy.")
##    print("Let's get started")
##    prrint("Your hand contains:")
##
##def drawCard(available_cards:[Card]) -> Card:
##
##def createStartingHand(available_cards:[Card], num_to_draw:int) -> [Card]:


if __name__ == '__main__':
            
    sorted_unshuffled_deck = make_standard_Card_Deck_List(my_deck)
    print_Deck(sorted_unshuffled_deck)
    
   

##    You must use the random library for shuffling. 
##	
