class Student():
    def __init__(self, name, years=1):
        self.name = name
        self.years_UM = years
        self.knowledge = 0
        
    def study(self):
        self.knowledge += 1
        return None
        
    def getKnowledge(self):
        return self.knowledge
        
    def year_at_umich(self):
        return self.years_UM
        
noah = Student("Noah")
eric = Student("Eric", 3)

assert noah.name == "Noah"
assert noah.years_UM == 1
assert noah.knowledge == 0

assert eric.name == "Eric"
assert eric.years_UM == 3
assert eric.knowledge == 0

assert noah.study() == None
assert noah.knowledge == 1
assert noah.getKnowledge() == noah.knowledge

assert eric.study() == None
assert eric.knowledge == 1
assert eric.getKnowledge() == noah.knowledge

assert noah.year_at_umich() == noah.years_UM
assert eric.year_at_umich() == eric.years_UM