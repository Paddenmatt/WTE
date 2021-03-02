


class Fooditem(object):
    def __init__(self, itemName, dining, health, flavor1, weight):
        self.itemName(itemName)
        print("Init called.")
        self.dining = dining
        self.health = health
        self.flavor1 = flavor1
        self.weight = weight
        self.assign()

    def assign(self): #dining, health, flavor1, weight
        return self.dining, self.health, self.flavor1, self.weight

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









