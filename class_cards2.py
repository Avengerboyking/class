class Deck:
    def __init__(self, card_color):
        self.color = card_color

    def __str__(self):
        return f"cards color is {self.color}"
        