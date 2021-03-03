


class Fooditem(object):
    def __init__(self, itemName, dining, health, flavor1, weight):
        self.itemName = itemName
        print("Init called.")
        self.dining = dining
        self.health = health
        self.flavor1 = flavor1
        self.weight = weight

    def assign(self): #dining, health, flavor1, weight
        print("This is a test to see if responses were recorded: " + self.dining)

    def show(self):
        print(self.dining)
        print(self.health)
        print(self.flavor1)
        print(self.weight)


# class FoodManager:
#   #list of FoodItem objects
#   def __init__(self):
#     self.foodList = []

#   # add item
#    def add(foodItem):
#     foodList.insert(foodItem)
#   # meals = {
#   #
#   # }









