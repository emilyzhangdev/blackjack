import card
import random

class Deck:
    def __init__(self, num) -> None:
        suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
        values = "2,3,4,5,6,7,8,9,10,J,Q,K,A".split(',')
        self.cards = [card.Card(i, l) for i in suits for l in values]

    def get_card(self):
        return self.cards.pop(random.randint(0,len(self.cards)-1))
    

        