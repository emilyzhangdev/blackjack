class Card:
    def __init__(self, suit, symbol):
        self.suit = suit
        self.symbol = symbol
        if symbol in ["J","Q","K"]:
            self.value = 10
        elif symbol == "A":
            self.value = 11
        else:
            self.value = int(self.symbol)

    def __repr__(self) -> str:
        return f"{self.suit}{self.symbol}"
    
