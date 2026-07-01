# # test 1
# # write a function that takes a list of numbers 

# def evenNum(userNum):
#     boxOfEven = []
#     for x in userNum:
#         if (x % 2 == 0):
#             boxOfEven.append(x)
#         else:
#             continue

#     return boxOfEven

# newX = evenNum([1,2,3,4,5,6])
# print(newX)


# # test 2
# # You have this:
# unit = {"name": "Goku", "type": "AGL", "rarity": "LR"}
# # Write code that prints "Goku is an AGL LR unit"
# # using the dictionary values, not hardcoded text

# print(f'{unit["name"]} is an {unit["type"]} LR unit ')




# # task 3
# # # Create a class called Unit with name, type, and rarity
# # # Then create two Unit objects and print both of their names

# class Unit:
#     def __init__(self, name, type, rarity ):
#         self.name = name
#         self.type = type
#         self.rarity = rarity


# unit1 = Unit('Goku' , 'AGL' , 'LR')
# unit2 = Unit('Vegeta' , 'PHY' , 'SSR')

# print(unit1.name)
# print(unit2.name)

my_team = [
            {"name": "Goku", "type": "AGL", "rarity": "LR"}, 
            {"name": "Vegeta", "type": "AGL", "rarity": "LR"},
            {"name": "Picolo", "type": "PHY", "rarity": "LR"},
            {"name": "Nappa", "type": "TEQ", "rarity": "LR"},
            {"name": "Raditz", "type": "STR", "rarity": "LR"}
    ]
# You have a list of dictionaries (like Test 2's unit, but 5 of them)
# Write code that returns only the units where type == "AGL"
def sameType(Theteam):

    boxOfSameType = []
    for x in Theteam:
        if x["type"] == "AGL":
            boxOfSameType.append(x)

    return boxOfSameType

newBox = sameType(my_team)
print(newBox)
    

