import random
from random import randint
import unittest
"""
ICS 31 Lab 8 Problem 1
Driver: UCI_ID: 18108714 Name: Estela Ramirez Ramirez
"""
class Card:
    Name   = None 		
    Value  = None    

def makeCard(name:str, value:int)->Card:
    c = Card()
    c.Name = name
    c.Value = value
    return c
    
class Bets:
    player_funds    = 0		
    player_bet      = 0	

def makeBets(funds:int , bet:int)->Bets:
    b = Bets()
    b.player_funds = funds
    b.player_bet = bet
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


def make_standard_Card_Deck_List(my_deck:[{str:int}]) -> [Card]:
    Card_Deck = make_Card_Deck_List(my_deck)
    new_sorted_deck = select_Sort(Card_Deck)
    return new_sorted_deck
    

def print_Deck(card_deck_list:[Card]):
    for card in card_deck_list:
        print(card.Name, ":", card.Value)


def generate_shuffled_deck(full_deck:[Card]) -> [Card]:
    deck = full_deck.copy()
    random.shuffle(deck)
    return deck


def menu(bets:Bets):# might be that I can use the two paramters themselves
    print("\nYour current bet is $", bets.player_bet, "of your ", bets.player_funds, " ", "funds\n")
    print("You can increase your bet by at most $ ", bets.player_funds - bets.player_bet, "\n")


def intro_message():
    print("Hello and Welcome to the Friend Computer's BlackJack Table!")
    print("At the Friend Computer's BlackJack Tables the closest player to 21, with a value less than 21 wins!")
    print("If you exceed 21, you lose. If the computer has card values closer to 21, you lose.")
    print("If you are closer to 21 than the computer, then you win!")
    print("Note: Ace defaults to 11, but will change to 1, should you exceed 21.")
    print("Also Beware the Friend Computer NEVER turns down a bet and is infinitely wealthy.")
    print("Let's get started")
    

def drawCard(available_cards:[Card]) -> Card:
    a = available_cards.pop()
    return a


def createStartingHand(available_cards:[Card], num_to_draw:int) -> [Card]:
    hand = []
    for card in range(num_to_draw):
        a = drawCard(available_cards)
        hand.append(a)
    return hand
        
def print_Hand(card_list:[Card]):
    print("\n")
    for card in card_list:
        print(card.Name, "with a value of", card.Value)


def eval_Hand(card_list:[Card])->int:
    print("\n")
    player_total = 0
    for card in card_list:
        player_total += card.Value
        if card.Value == 11:
            player_total -= 10
        if player_total <= 21:
            break #or pass
    return player_total


def print_player_hand(player_hand:[Card]):
    print("Your hand contains: ")
    print("\n")
    print_Hand(player_hand)
    print("\n")
    print("For a total value of", str(eval_Hand(player_hand)))


def print_computer_hand(computer_hand:[Card]):
    print("\n")
    print_Hand(computer_hand)
    print("\n")
    print("For a total value of", str(eval_Hand(computer_hand)))

def getH_or_SChoice()-> str:
    while True:
        choice = input("Would you like to Hit(H) or Stay(S)? ").upper().strip()
        if choice != "H" and choice != "S":
            print("Invalid input, Enter H or S.")
        else:
            return choice
            break


 
def Bust_message():
    print("Oh No!! Your hand has busted as it has exceeded 21\nYour hand now has a total value of: " + str(player_value))  

  
       
def stayOrHit(player_hand:[Card], available_cards:[Card])-> bool:
    choice = getH_or_SChoice()
    if choice== "S":
        print("You chose to stay/skip your turn")
        return False
    
    if choice== "H":
        draw_card_for_player = drawCard(available_cards)
        player_hand.append(draw_card_for_player)
        player_hand_total = eval_Hand(player_hand)
        print("You drew " + draw_card_for_player.Name + " which has a value of  " + str(draw_card_for_player.Value))
        
        if player_value > 21:
            Bust_message()
            return False
        print("Your hand has a total value of: " + str(player_value))
        return True

    
def getBetChoice() -> str:
    while True:
        choice = input("Would you like to Raise(R) or Stay(S)? ").upper().strip()
        if choice != "R" and choice != "S":
            print("Invalid input, Enter R or S.")
        else:
            return choice
            break
                  

def getBetAmount(available_for_bet:int)-> int:
    while True:
        bet_amount = int(input("How much would you like to raise by? "))
        if bet_amount < 0:
            print("Invalid amount.")
        else:
            return bet_amount
            break

                  


def betting(bets:Bets):
    available_for_bet = str(bets.player_funds - bets.player_bet)                
    menu(bets)
    choice = getBetChoice()
    if choice == "R":
        bet_amount = 0
        bet_amount = getBetAmount(available_for_bet)
        while bet_amount > 0 and bet_amount <= bets.player_funds:
            break
        print("Insufficient funds to make a bet of $", str(bet_amount))
                  
        bets.player_bet += bet_amount
        print("Your bet has been increased to $" + str(bet_amount))
                  
    if choice == "S":
        print("Your bet is unchanged and remains $" + str(bets.player_bet))

def getContinue_Or_Quit():
    while True:
        choice = input("Would you like to Continue and Play Another Round (C) or Quit(Q)? ").upper().strip()
        if choice != "C" and choice != "Q":
            print("Invalid input, Enter C or Q.")
        else:
            return choice
            break



def computerTurn(computer_hand:[Card], available_cards:[Card])->bool: #True if C hits and does not bust
    computer_hand_total = eval_Hand(computer_hand)
                  
    if computer_hand_total < 17:
        card_for_computer = drawCard(available_cards)
        computer_hand.append(card_for_computer)
        print("The Friend Computer Hits.")
        return True
    #check if bust
    if computer_hand_total > 21:
        print("The computer has bust. You win this round!!")
        return False
    else:
        print("The Friend Computer Stays.")
        return False


def comp_busts_add_money_message(bets:Bets):
    bets.player_funds += bets.player_bet
    print("Your bet of $", str(bets.player_bet) , "has been added to your funds!!")
    print("You now have", str(bets.player_funds))

                  
def both_stay_reveal_hands_message():
    print("All players have chosen to stay, so we will reveal hands.")

                  
def comp_wins_message(bets:Bets):
    print("The computer has one this round.")
    print("Your bet of", str(bets.player_bet),"has been subtracted from your funds.")
    bets.player_funds -= bets.player_bet
    print("You now have", str(bets.player_funds))
                  
def tie_message(bets:Bets):
    print("What? You have tied the Friend Computer ?!?")
    print("Alright mortal I will grant you the pot,..., this time...")
    print("The Friend Computer has graciously and generously awarded you.")
    print("Your bet has been added to your funds")
    bets.player_funds += bets.player_bet
    print("You now have", str(bets.player_funds))


                  
def player_wins_message(bets:Bets):
    print("Congrats your hand was better than the Friend Computers !")
    print("Your funds have been increased by your bet size.")
    bets.player_funds += bets.player_bet
    print("You now have", str(bets.player_funds))
                 
def player_runs_out_message():
    print("Alas you have run out of money.")
    print("We hope you come back and play again soon!")
    print("The Friend Computer always appreciates financial contributions!")
    quit()


def runRound_for_computer(full_deck:[{str:int}], funds:int, bets:Bets):
    comp_total = eval_Hand(computer_hand)
    if computer_hand > 21:
        comp_busts_add_money_message(bets)
                  
    if comp_total <= 21 and player_total <= 21:
        both_stay_reveal_hands_message()
        print("Your hand had a final value of", str(player_total))
        print("The Friend Computer had a final value of", str(comp_total))
                  
        if comp_total > player_total:
            comp_wins_message(bets)

                  
        elif computer_total == player_total:
            tie_message(bets)

                  
        else:
            player_wins_message(bets)
            

    print("Now that the round has ended, the Friend Computer's hand will be revealed.")
    print("The Friend Computer's hand contains:", comp_total)
    print_Hand(computer_hand)
    if bets.player_funds == 0:
        player_runs_out_message()
        

                  
def runRound(full_deck:[{str:int}], funds:int, bets:Bets):
    cards = make_standard_Card_Deck_List(full_deck)
    shuffled_deck = generate_shuffled_deck(cards)
                  
    player_hand = createStartingHand(shuffled_deck, 2)
    computer_hand = createStartingHand(shuffled_deck, 2)
                  
    print_player_hand(player_hand)
    betting(bets)
                  
    while stayOrHit(player_hand, shuffled_deck) == False:
        break
    
    player_total = eval_Hand(player_hand)
    
    if player_total > 21:
        bets.player_funds =  bets.player_funds- bets.player_bet
        print("Your bet of $", bets.player_bet , "has been subtracted from your funds!!\nYou now have", bets.player_funds)

    while True and player_total <= 21:
        if computerTurn(computer_hand, shuffled_deck) == False:
            break
    runRound_for_computer(full_deck, funds, bets)

                  

def getString(prompt:str, options:[str])-> str: #Klefstad version
    choice = input(prompt).upper().strip()
    while not choice in options:
        print("Invalid input, please enter ", end = "")
        if len(options) == 2:
            print(options[0], "or", options[1])
        else:
            for option in options:
                if option != options[-1]:
                    print(option, end = "," )
                else:
                    print( " or" , option)
        choice = input(prompt).upper().strip()
    return choice

def runGame(full_deck:[{str:int}], Game_Money:int):
    intro_message()
    computer_and_player_bets = makeBets(Game_Money, 0)
    while computer_and_player_bets.player_funds > 0:
        runRound(full_deck, computer_and_player_bets.player_funds, computer_and_player_bets)
        print("\n")
        print("The Friend Computer has challenged you to another round!")
        choice = getString("Would you like to Continue and Play Another Round (C) or Quit(Q)? ", ["C", "Q"])
        if choice == "Q":
            break




def main():

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

    runGame(official_deck, 100)
    
if __name__== "__main__":
    
    main()
    
   
    
    
    



    
 	
