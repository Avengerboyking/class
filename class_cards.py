class Card:
    def __init__(self, rank, suit):
        self.rank  = rank
        self.suit = suit
    def __str__(self):
        return f"This card's rank is {self.rank}, its suit is {self.suit}."

card1 = Card("Ace", "Spade")
card2 = Card(5, "Heart")
card3 = Card(3, "Club")
card4 = Card(9, "Diamond")

print(card1, card2, card3, card4)