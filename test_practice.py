# # task 5
 # """Return all units matching the given type (case/whitespace-insensitive)."""
import json
import sys
try:
        with open('units.json', 'r') as file:
            my_team = json.load(file)
except:
        print("Sorry, but the file must be broken T_T")
        sys.exit()

# skipped_units = 0
# hp_total = 0
# count = 0
# valid_units = []
# for x in my_team:
#     if isinstance(x["hp"], str) or not x["hp"] :
#         skipped_units+=1
#         continue
#     else:
#         hp_total += x["hp"]
#         count+=1
#         valid_units.append(x)

# with open("clean_units.json" , "w") as file:
#     json.dump(valid_units ,file, indent = 3 )
        
# print(count, "units are valid and has HP")
# print(skipped_units , "were skipped")
# print(hp_total , "is the total HP of the valid units")


# task 6 
# # search function
# # part 1
# def search_units(unit_list , search_term):
#     sameUnits = []
#     cleanSearch = search_term.strip()
#     upperCleanSearch = cleanSearch.upper()
#     for x in unit_list:
#            if upperCleanSearch == x["type"].strip().upper():
#                 sameUnits.append(x)
#            else:
#                 continue
#     filterdResault = []
#     for unit in sameUnits:
#           filterdResault.append({'name' :unit['name'] , 'type' :unit['type']})
#     return filterdResault


# promptUsers = input("Enter the type of the Char: ")
# resualt = search_units(my_team , promptUsers)
# print(resualt)



# #part 2
# def search_by_name(unit_list, partial_name):
#       units_names = []
#       clean_Name = partial_name.strip().lower()
#       for x in unit_list:
#             if clean_Name in x["name"].strip().lower():
#                   units_names.append(x)
#       return units_names
                  
# userInput = input("Enter the name of the char: ")
# outputChar = search_by_name(my_team, userInput)
# if not outputChar:
#       print("No units found matching that name")
# else:
#        print(outputChar)

# # part 3
# def build_report(unit_list):
#        units_string = []
#        filterd_units = []
#        sortedUnits = []
#        for x in unit_list:
#             if isinstance(x["hp"], str) or not x["hp"]:
#                  continue
#             else:
#                  filterd_units.append(x)
#        sortedUnits = sorted(filterd_units , key = lambda HP : HP['hp'] , reverse = True)
#        for x in sortedUnits:
#                 unit = f"{x['name']} ({x['type']}, {x['rarity']}) - {x['hp']} HP"
#                 units_string.append(unit)
#        return units_string

# unitSorted = build_report(my_team)
# # part 4
# with open("report.txt" , "w" , encoding="utf-8") as file:
#       file.write("\n".join(unitSorted))

# STAGE 1

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


my_team = Team()
other_team = Team()
my_team.add_unit(goku)
my_team.add_unit(vegeta)
other_team.add_unit(messi)
other_team.add_unit(cristiano)
namesOUT = my_team.print_names() 
## STAGE 2

def find_matches(team):
  unitList = []
  for unit in team.list_of_units:
       if unit.category == "Pure Saiyans" and unit.rarity == "LR" and unit.has_revive == True:
              unitList.append(unit.name)
  return unitList

test1 = find_matches(my_team)
test2 = find_matches(other_team)
test3 = []

# print(test1)
# print(test2)


# STAGE 4 
new_team = Team()

new_team.add_unit(goku)
new_team.add_unit(vegeta)
new_team.add_unit(messi)
new_team.add_unit(mbappe)
new_team.add_unit(halland)
new_team.add_unit(cristiano)
new_team.add_unit(raditz)




