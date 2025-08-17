import random
class Colony:
    def __init__(self):
        self.colony_population = 0
        self.infected_population = 0
        self.morale = 0
        self.hygiene = 0
        self.medical_supplies = 0
        self.specific_items = []
        self.supply = 0
class Disease:
    def __init__(self):
        self.stealth = 0
        self.lethality = 0
        self.spread = 0
        self.evasion = 0
        self.dormancy = 0
        self.resistance = 0
        self.adaptation = 0

    def infect_individual(self):
        colony = Colony()
        spread_strength = self.spread + self.stealth + self.adaptation + random.randint(1,3)
        lost_hp = 0
        resistance = 5 - lost_hp/2 + self.colony.supply + self.colony.hygiene
        if spread_strength >= resistance:
            self.colony.infected_population += 1

    def infect_group(self):
        spread_strength = self.spread + self.stealth + self.colony.infected_population
        spread_resistance = 5 + self.colony.hygiene + self.colony.supply
        if spread_strength >= spread_resistance:
            new_infections = spread_strength - spread_resistance
            if new_infections == 0:
                new_infections = 1
            self.colony.infected_population += new_infections





