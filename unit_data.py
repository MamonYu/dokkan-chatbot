
class Unit:
       def __init__(self , name , type , rarity, category , has_revive):
              self.name = name
              self.type = type
              self.rarity = rarity
              self.category = category
              self.has_revive = has_revive
       
class Team:
       def __init__(self):
              self.list_of_units = []
              
       def add_unit(self, unit):
              self.unit = unit
              self.list_of_units.append(unit)
              # print(len(self.list_of_units))

       def print_names(self):
        filterdResault = []
        for unit in self.list_of_units:
          filterdResault.append({'name' :unit.name , 'type' :unit.type , 'rarity' : unit.rarity , 'category' : unit.category , 'has_revive' : unit.has_revive })
        return filterdResault
              
goku = Unit("Goku", "AGL", "LR", "Pure Saiyans", True)
vegeta = Unit("Vegeta", "AGL", "LR", "Pure Saiyans", False)
messi = Unit("Messi" , "AGL" , "LR" , "Hybird Saiyans" , False)
cristiano = Unit("Cristiano" , "STR" , "LR" , "Pure Saiyans" , True)
mbappe = Unit("Mbappe" , "STR" , "LR" , "Pure Saiyans" , True)
halland = Unit("Halland" , "PHY" , "LR" , "Pure Saiyans" , True)
raditz = Unit("Raditz" , "TEQ" , "LR" , "Pure Saiyans" , False)

all_units = [goku, vegeta, messi, cristiano, mbappe, halland, raditz]