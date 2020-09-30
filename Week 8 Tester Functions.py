"""
Week Tester Functions
"""
import unittest
from Blackjack import *

class testFunctions(unittest.TestCase):

    def test_makeCard(self):
        card = makeCard("Two of Spades" , 2)
        self.assertEqual(card.Name, "Two of Spades")
        self.assertEqual(card.Value, 2)

    def test_select_Sort(self):
        card2 = makeCard("Nine of Diamonds", 9)
        card1 = makeCard("Ten of Diamonds" , 10)
        list1 = [card1,card2]
        sort_list = select_Sort(list1)
        self.assertEqual(sort_list, [card2,card1])

    def test_make_standard_Card_Deck_List(self):
        res = make_standard_Card_Deck_List({"Ace of Hearts" : 11, "Two of Hearts" : 2})
        self.assertEqual(res[0].Name, "Two of Hearts")
        self.assertEqual(res[0].Value, 2)
        self.assertEqual(res[1].Name, "Ace of Hearts")
        self.assertEqual(res[1].Value, 11)
            
            
    def test_drawCard(self):
        card2 = makeCard("Nine of Diamonds", 9)
        card1 = makeCard("Ten of Diamonds" , 10)
        temp = drawCard([card1, card2])
        self.assertEqual(isinstance(temp, Card),True)
        self.assertEqual(temp.Name,"Nine of Diamonds")
        self.assertEqual(temp.Value, 9)

    def test_createStartingHand(self):
        card2 = makeCard("Nine of Diamonds", 9)
        card1 = makeCard("Ten of Diamonds" , 10)
        temp = createStartingHand([card1,card2], 1)
        self.assertEqual(temp[0].Name,"Nine of Diamonds")
        self.assertEqual(temp[0].Value, 9)	

    def test_eval_Hand(self):
        card2 = makeCard("Nine of Diamonds", 9)
        card3 = makeCard("Nine of Diamonds", 9)
        card1 = makeCard("Eight of Hearts" , 8)
        self.assertEqual(eval_Hand([card1,card2]),17)
        card2 = makeCard("Ace of Spades",11)
        self.assertEqual(eval_Hand([card1,card2,card3]),18)
                    
    def test_getH_or_SChoice(self):
        __builtins__.input = lambda _: 'H'
        self.assertEqual(getH_or_SChoice(),'H')
        __builtins__.input = lambda _: 'h  '
        self.assertEqual(getH_or_SChoice(),'H')

    def test_getBetChoice(self):
        __builtins__.input = lambda _: 'R'
        self.assertEqual(getBetChoice(),'R')
        __builtins__.input = lambda _: 's  '
        self.assertEqual(getBetChoice(),'S')

    def test_getBetAmount(self):
        __builtins__.input = lambda _: 20
        self.assertEqual(getBetAmount(30),20)

    def test_computerTurn(self):
        card1 = makeCard("Ace of Hearts" , 11)
        card2 = makeCard("Two of Hearts" , 2)
        card3 = makeCard("Three of Hearts" , 3)
        self.assertEqual(computerTurn([card1,card2], [card3]), True)	

if __name__ == '__main__':
    unittest.main()
