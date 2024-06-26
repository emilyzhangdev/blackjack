import random
from deck import Deck

#TODO: Need to add money wagers. Splitting, Doubling Down, Surrender

game_deck = Deck(1)

dealers_cards = []
player_cards = []

#the cards are dealt
d1 = game_deck.get_card()
p1 = game_deck.get_card()
d2 = game_deck.get_card()
p2 = game_deck.get_card()

#check for blackjack
if p1.value + p2.value == 21:
    print ("Blackjack")

print (f"Dealer has a {d1}")

print (f"Player has {p1} {p2} ")

decision = "H"
player_total =  p1.value + p2.value
dealer_total =  d1.value + d2.value

#players turn
while decision != "S" and player_total < 21:
    decision = input("What would you like to do: ")
    if decision == "H":
        next_card = game_deck.get_card()
        print (f"Next card is {next_card}")
        player_total += next_card.value
        if player_total > 21:
            print ("You lose")
        elif player_total == 21:
            break
    

#show dealers turn
print (f"Dealer Face Down Card is {d2} ")
while dealer_total < 16:
    next_card = game_deck.get_card()
    print (f"Dealer got a {next_card}")
    dealer_total += next_card.value
    print (f"Dealer total is {dealer_total}")

if dealer_total > 21:
    print ("Dealer Bust. You win!")
elif dealer_total > player_total:
    print ("Dealer wins")
else:
    print ("You win!")