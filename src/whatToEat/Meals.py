class Fooditem(object):
    def __init__(self, itemName, dining, flavor1, health, weight, attribute=0):
        self.itemName = itemName
        self.dining = dining
        self.flavor1 = flavor1
        self.health = health
        self.weight = weight
        self.attribute = attribute


# Creates an array of Fooditem objects
foodList = []

foodList.append(Fooditem('Fries', 'dining out', 'salty', 'casual', 'light'))
foodList.append(Fooditem('Baked Salmon', 'dining out', 'salty', 'healthy', 'light'))
foodList.append(Fooditem('Steak', 'dining out', 'salty', 'healthy', 'light'))
