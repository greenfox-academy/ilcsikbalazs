import random
class Pirate:
    def __init__(self, toxic_lvl=0, dies=False, passes_out=False):
        self.toxic_lvl = toxic_lvl
        self.dies = dies
        self.passes_out = passes_out

    def drink_some_rum(self):
        if (self.passes_out == True) or (self.dies == True):
            return
        self.toxic_lvl += 1
        if self.toxic_lvl > 4:
            self.passed_out()

    def hows_it_going_mate(self):
        if (self.passes_out == True) or (self.dies == True):
            return
        if self.toxic_lvl > 4:
            self.passed_out()
        elif self.toxic_lvl <=4:
            print("another")

    def brawl(self,other_pirate):
        if (self.passes_out == True) or (self.dies == True):
            return
        chance = random.randint(1,3)
        if chance == 1:
            print("You")
            self.died()
        elif chance == 2:
            print("Enemy")
            other_pirate.died()
        elif chance == 3:
            self.passed_out()
            other_pirate.passed_out()

    def passed_out(self,other_pirate=None):
        self.passes_out = True
        print("Passed out")

    def died(self, other_pirate=None):
        self.dies = True
        print("Died")

class Ship:
    def __init__(self,crew=0,captain=0):
        self.crew = crew
        self.captain = captain

    def fill_ship(self):
        pirates = random.randint(20,100)
        self.crew = pirates
        self.captain = 1

    def get_crew_number(self):
        print(self.crew)

crew = Ship()
captain = Pirate()
crew.fill_ship()
crew.get_crew_number()
