class Fooditem(object): 
    def __init__(self, itemName, mealType, dining, flavor1, health, weight, attribute=0):
        self.itemName = itemName
        self.mealType = mealType
        self.dining = dining
        self.flavor1 = flavor1
        self.health = health
        self.weight = weight
        self.attribute = attribute

    def __gt__(self, other):
        return self.attribute < other.attribute

    def getItemName():
        return self.itemName


# Creates an array of Fooditem objects
foodList = []

foodList.append(Fooditem("Fries", "lunch", "dining out", "salty", "casual", "light"))
foodList.append(Fooditem("Fries", "dinner", "dining out", "salty", "casual", "light"))
foodList.append(Fooditem("Baked Salmon", "dinner", "dining out", "salty", "healthy", "light"))
foodList.append(Fooditem("Steak", "dinner", "dining out", "salty", "healthy", "light"))
foodList.append(Fooditem("Ravioli", "dinner", "dining out", "salty", "healthy", "full"))
foodList.append(Fooditem("GrilledChicken", "lunch", "dining out", "Healthy", "salty", "light"))
foodList.append(Fooditem("GrilledSalmon", "lunch", "dining out", "healthy", "salty", "light"))
foodList.append(Fooditem("GrilledSalmon", "dinner", "dining out", "healthy", "salty", "light"))
foodList.append(Fooditem("Ravioli", "dinner", "dining in", "casual", "salty", "full"))
foodList.append(Fooditem("Burrito", "lunch", "dining out", "casual", "salty", "full"))
foodList.append(Fooditem("Spaghetti", "lunch", "dining out", "casual", "salty", "full"))
foodList.append(Fooditem("Spaghetti", "dinner", "dining out", "casual", "salty", "full"))
foodList.append(Fooditem("Omelet", "breakfast", "dining out", "casual", "salty", "full"))
foodList.append(Fooditem("Nachos", "lunch", "dining out", "casual", "salty", "full"))
foodList.append(Fooditem("Hamburger", "lunch", "dining out", "casual", "salty", "full"))
foodList.append(Fooditem("IceCream", "lunch", "dining out", "casual", "sweet", "light"))
foodList.append(Fooditem("IceCream", "dinner", "dining out", "casual", "sweet", "light"))
foodList.append(Fooditem("HotDog","lunch", "dining out", "casual", "salty", "light"))

# foodlist = [
#             Fooditem(Fries), Fooditem(BakedSalmon), Fooditem(SteakIn), Fooditem(SteakOut), Fooditem(GrilledChicken),
#             Fooditem(GrilledSalmon), Fooditem(Ravioli, Fooditem(Burrito), Fooditem(Spaghetti), Fooditem(Omelet),
#             Fooditem(Nachos), Fooditem(Hamburger), Fooditem(IceCream), Fooditem(HotDog)
#             ]
GrilledChicken = {"GrilledChicken", "dining out", "Healthy", "salty", "light"}
GrilledSalmon = {"GrilledSalmon", "dining out", "healthy", "salty", "light"}
Ravioli = {"Ravioli", "dining in", "casual", "salty", "full"}
Burrito = {"Burrito", "dining out", "casual", "salty", "full"}
Spaghetti = {"Spaghetti", "dining out", "casual", "salty",}
Omelet = {"Omelet", "dining out", "casual", "salty", "full"}
Nachos = {"Nachos", "dining out", "casual", "salty", "full"}
Hamburger = {"Hamburger", "dining out", "casual", "salty", "full"}
IceCream = {"IceCream", "dining out", "casual", "sweet", "light"}
HotDog = {"HotDog", "dining out", "casual", "salty", "light"}