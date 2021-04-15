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
foodList.append(Fooditem("GrilledChicken", "lunch", "dining out","salty",  "healthy", "light"))
foodList.append(Fooditem("GrilledSalmon", "lunch", "dining out","salty", "healthy",  "light"))
foodList.append(Fooditem("GrilledSalmon", "dinner", "dining out","salty",  "healthy",  "light"))
foodList.append(Fooditem("Ravioli", "dinner", "dining in","salty", "casual",  "full"))
foodList.append(Fooditem("Burrito", "lunch", "dining out","salty", "casual",  "full"))
foodList.append(Fooditem("Spaghetti", "lunch", "dining out","salty", "casual",  "full"))
foodList.append(Fooditem("Spaghetti", "dinner", "dining out","salty", "casual",  "full"))
foodList.append(Fooditem("Omelette", "breakfast", "dining out","salty", "casual",  "full"))
foodList.append(Fooditem("Nachos", "lunch", "dining out","salty", "casual",  "full"))
foodList.append(Fooditem("Hamburger", "lunch", "dining out","salty", "casual", "full"))
foodList.append(Fooditem("IceCream", "lunch", "dining out","sweet", "casual", "light"))
foodList.append(Fooditem("IceCream", "dinner", "dining out","sweet", "casual", "light"))
foodList.append(Fooditem("HotDog","lunch", "dining out","salty", "casual", "light"))



# 00001       lunch, dining out, sweet, healthy, heavy = 
# 00010       lunch, dining out, sweet, casual, light  = IceCream
# 00011       lunch, dining out, sweet, casual, heavy  = Ravioli
# 00100       lunch, dining out, salty, healthy, light = Baked Salmon, Steak, GrilledChicken, GrilledSalmon
# 00101       lunch, dining out, salty, healthy, heavy = 
# 00110       lunch, dining out, salty, casual, light  = Fries,HotDog
# 00111       lunch, dining out, salty, casual, heavy  = Nachos, Burrito, Hamburger,Spaghetti, Omelette
# 01000       lunch, dining in, sweet, healthy, light  =
# 01001       lunch, dining in, sweet, healthy, heavy  =
# 01010       lunch, dining in, sweet, casual, light   =
# 01011       lunch, dining in, sweet, casual, heavy   =
# 01100       lunch, dining in, salty, healthy, light  =
# 01101       lunch, dining in, salty, healthy, heavy  =
# 01110       lunch, dining in, salty, casual, light   =
# 01111       lunch, dining in, salty, casual, heavy   =
# 10001       dinner, dining out, sweet, healthy, heavy = 
# 10010       dinner, dining out, sweet, casual, light  = IceCream
# 10011       dinner, dining out, sweet, casual, heavy  =
# 10100       dinner, dining out, salty, healthy, light = 
# 10101       dinner, dining out, salty, healthy, heavy =
# 10110       dinner, dining out, salty, casual, light  =
# 10111       dinner, dining out, salty, casual, heavy  =
# 11000       dinner, dining in, sweet, healthy, light  =
# 11001       dinner, dining in, sweet, healthy, heavy  =
# 11010       dinner, dining in, sweet, casual, light   =
# 11011       dinner, dining in, sweet, casual, heavy   =
# 11100       dinner, dining in, salty, healthy, light  =
# 11101       dinner, dining in, salty, healthy, heavy  =
# 11110       dinner, dining in, salty, casual, light   =
# 11111       dinner, dining in, salty, casual, heavy   =
# 10001       breakfast, dining out, sweet, healthy, heavy = 
# 10010       breakfast, dining out, sweet, casual, light  = 
# 10011       breakfast, dining out, sweet, casual, heavy  =
# 10100       breakfast, dining out, salty, healthy, light = 
# 10101       breakfast, dining out, salty, healthy, heavy =
# 10110       breakfast, dining out, salty, casual, light  = Omelette
# 10111       breakfast, dining out, salty, casual, heavy  =
# 11000       breakfast, dining in, sweet, healthy, light  =
# 11001       breakfast, dining in, sweet, healthy, heavy  =
# 11010       breakfast, dining in, sweet, casual, light   =
# 11011       breakfast, dining in, sweet, casual, heavy   =
# 11100       breakfast, dining in, salty, healthy, light  =
# 11101       breakfast, dining in, salty, healthy, heavy  =
# 11110       breakfast, dining in, salty, casual, light   =
# 11111       breakfast, dining in, salty, casual, heavy   =













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