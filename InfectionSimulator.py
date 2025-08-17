import random
import math
import time
class Colony:
    def __init__(self):
        self.colony_population = 0
        self._infected_population = 0
        self.morale = 0
        self.hygiene = 0
        self.medical_supplies = 0
        self.specific_items = []
        self.supply = 0
        self.infection_cap = None

    @property
    def infected_population(self):
        return self._infected_population

    @infected_population.setter
    def infected_population(self, value):
        # Ensure infected_population never exceeds colony_population
        self._infected_population = min(value, self.colony_population)
        
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

    def response_quarantine(self):
        structures_available = 0
        supplies_used = 0
        infection_cap = 0
        quarantine_effectiveness = self.colony.morale + structures_available + supplies_used
        disease_evasion = self.evasion*2 + self.stealth + round(self.colony.infected_population/2)
        if quarantine_effectiveness > disease_evasion:
            infection_cap = 0
            return infection_cap
        elif quarantine_effectiveness == disease_evasion:
            infection_cap = 1
            return infection_cap
        else:
            infection_cap = disease_evasion - quarantine_effectiveness
            return infection_cap

    def response_treatment(self):
        used_medical_supplies = 0
        treatment_effectiveness = used_medical_supplies + self.colony.hygiene + self.colony.morale/2
        disease_resistance = self.resistance + 1
        population_cured = math.floor(treatment_effectiveness/disease_resistance)
        if population_cured < 0:
            population_cured = 0
        elif population_cured >= 1:
            self.colony.infected_population = max(self.colony.infected_population - population_cured, 0)
        else: 
            population_cured = 0
        return
            
    def Elimination(self):
        deaths = 0
        if self.colony.infected_population <= 0:
            self.colony.infected_population = 0
            return
        else:
            supplies_used = 0
            supplies_used = math.ceil(supplies_used/self.infected_population)
            phases_sick = 0
            for i in range(self.colony.infected_population):
                Power = self.lethality + random.radnint(1,3) + phases_sick
                Resistance = 3 + self.colony.hygiene + self.colony.morale/2 + supplies_used
                if Power > Resistance:
                    self.colony.infected_population -= 1
                    self.colony.colony_population -= 1
                    deaths += 1

        print(f"{deaths} members have died out of {i} from the infection.")
        print(f"{i-deaths} members are currently infected.")
        time.sleep(2)

    def spread_infection(self):
        if self.colony.infected_population <= 0:
            print("No infected individuals to spread the disease.")
            return
        else:
            used_medical_supplies = 0
            Spread = self.colony.infected_population + self.spread/2
            Counter = self.colony.hygiene + used_medical_supplies
            if Spread > Counter:
                new_infections = Spread - Counter
                if self.colony.infection_cap != None:
                    new_infections = min(self.colony.infection_cap, new_infections)
                self.colony.infection_cap = None
                self.colony.infected_population += new_infections
                if new_infections > 0:
                    print(f"{new_infections} new infections have occurred.")





