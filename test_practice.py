# # # test 1
# # # write a function that takes a list of numbers 

# # def evenNum(userNum):
# #     boxOfEven = []
# #     for x in userNum:
# #         if (x % 2 == 0):
# #             boxOfEven.append(x)
# #         else:
# #             continue

# #     return boxOfEven

# # newX = evenNum([1,2,3,4,5,6])
# # print(newX)


# # # test 2
# # # You have this:
# # unit = {"name": "Goku", "type": "AGL", "rarity": "LR"}
# # # Write code that prints "Goku is an AGL LR unit"
# # # using the dictionary values, not hardcoded text

# # print(f'{unit["name"]} is an {unit["type"]} LR unit ')




# # # task 3
# # # # Create a class called Unit with name, type, and rarity
# # # # Then create two Unit objects and print both of their names

# # class Unit:
# #     def __init__(self, name, type, rarity ):
# #         self.name = name
# #         self.type = type
# #         self.rarity = rarity


# # unit1 = Unit('Goku' , 'AGL' , 'LR')
# # unit2 = Unit('Vegeta' , 'PHY' , 'SSR')

# # print(unit1.name)
# # # print(unit2.name)

# # my_team = [
# #             {"name": "Goku", "type": "AGL", "rarity": "LR"}, 
# #             {"name": "Vegeta", "type": "AGL", "rarity": "LR"},
# #             {"name": "Picolo", "type": "PHY", "rarity": "LR"},
# #             {"name": "Nappa", "type": "TEQ", "rarity": "LR"},
# #             {"name": "Raditz", "type": "STR", "rarity": "LR"}
# #     ]
# # # You have a list of dictionaries (like Test 2's unit, but 5 of them)
# # # Write code that returns only the units where type == "AGL"
# # def sameType(Theteam):

# #     boxOfSameType = []
# #     for x in Theteam:
# #         if x["type"] == "AGL":
# #             boxOfSameType.append(x)

# #     return boxOfSameType

# # newBox = sameType(my_team)
# # print(newBox)
    

# # task 5
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

# part 3
def build_report(unit_list):
       units_string = []
       filterd_units = []
       sortedUnits = []
       for x in unit_list:
            if isinstance(x["hp"], str) or not x["hp"]:
                 continue
            else:
                 filterd_units.append(x)
       sortedUnits = sorted(filterd_units , key = lambda HP : HP['hp'] , reverse = True)
       for x in sortedUnits:
                unit = f"{x['name']} ({x['type']}, {x['rarity']}) - {x['hp']} HP"
                units_string.append(unit)
       return units_string

unitSorted = build_report(my_team)
# part 4
with open("report.txt" , "w" , encoding="utf-8") as file:
      file.write("\n".join(unitSorted))




