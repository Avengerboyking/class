current_year = 2019

class Person:
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born
    def get_age(self):
        return current_year - self.year_born
    def __str__(self):
        return f"{self.name}: {self.year_born}"
alice = Person("Alitereee Smitthhhhhhhhh", 1345)                                                   
noah = Person("Noah Chen", 2924)
print(alice.get_age())
print(str(noah))