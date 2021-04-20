class Fooditem(object): 
    def __init__(self, itemName, mealType, dining, flavor1, health, weight, image, link, attribute=0):
        self.itemName = itemName
        self.mealType = mealType
        self.dining = dining
        self.flavor1 = flavor1
        self.health = health
        self.weight = weight
        self.image = image
        self.link = link
        self.attribute = attribute

    def __gt__(self, other):
        return self.attribute < other.attribute

    def getItemName():
        return self.itemName



# Creates an array of Fooditem objects
foodList = []

foodList.append(Fooditem("Fries", "dinner", "dining out", "salty", "casual", "light"))
foodList.append(Fooditem("Steak", "dinner", "dining out", "salty", "healthy", "light"))
foodList.append(Fooditem("Grilled Salmon", "dinner", "dining out","salty",  "healthy",  "light"))
foodList.append(Fooditem("Ravioli", "dinner", "dining in","salty", "casual",  "full"))
foodList.append(Fooditem("Spaghetti", "dinner", "dining out","salty", "casual",  "full"))
foodList.append(Fooditem("Omelette", "breakfast", "dining out","salty", "casual",  "full"))


foodList.append(Fooditem("Angel Food Cake", "lunch", "dining out", "sweet", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Fruit Smoothie", "lunch", "dining out", "sweet", "healthy", "light", "img", "No Recipe"))

foodList.append(Fooditem("Strawberry Cake", "lunch", "dining out", "sweet", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Sweet Crepes", "lunch", "dining out", "sweet", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Muffins", "lunch", "dining out", "sweet", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Ice Cream", "lunch", "dining out","sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Cupcakes", "lunch", "dining out", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Croissants", "lunch", "dining out", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Boba", "lunch", "dining out", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Castella", "lunch", "dining out", "sweet", "casual", "light", "img", "No Recipe"))

foodList.append(Fooditem("Puffle Waffles", "lunch", "dining out", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Banana Split", "lunch", "dining out", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Cheesecake", "lunch", "dining out", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Peach Cobbler", "lunch", "dining out", "sweet", "casual", "full", "img", "No Recipe"))

foodList.append(Fooditem("Baked Salmon", "lunch", "dining out", "salty", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Grilled Chicken", "lunch", "dining out","salty",  "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Grilled Salmon", "lunch", "dining out","salty", "healthy",  "light", "img", "No Recipe"))

foodList.append(Fooditem("Meatloaf", "lunch", "dining out", "salty", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Fries", "lunch", "dining out", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Hot Dog","lunch", "dining out","salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Ravioli", "lunch", "dining out", "salty", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Wings", "lunch", "dining out", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Fried Mozzerlla", "lunch", "dining out", "salty", "casual", "light", "img", "No Recipe"))

foodList.append(Fooditem("Nachoes", "lunch", "dining out", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Burrito", "lunch", "dining out","salty", "casual",  "full", "img", "No Recipe"))
foodList.append(Fooditem("Hamburger", "lunch", "dining out","salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Spaghetti", "lunch", "dining out","salty", "casual",  "full", "img", "No Recipe"))
foodList.append(Fooditem("Casserole", "lunch", "dining out","salty", "casual",  "full", "img", "No Recipe"))

#===============================Lunch "dining in"===============================#

foodList.append(Fooditem("Strawberry Cake", "lunch", "dining in", "sweet", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Sweet Crepes", "lunch", "dining in", "sweet", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Muffins", "lunch", "dining in", "sweet", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Cupcakes", "lunch", "dining in","sweet","casual","light", "img", "No Recipe"))
foodList.append(Fooditem("Boba", "lunch", "dining in","sweet","casual","light", "img", "No Recipe"))

foodList.append(Fooditem("Banana Split", "lunch", "dining in", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Cheesecake", "lunch", "dining in", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Peach Cobbler", "lunch", "dining in", "sweet", "casual", "full", "img", "No Recipe"))

foodList.append(Fooditem("Baked Salmon", "lunch", "dining in", "salty", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Grilled Chicken", "lunch", "dining in","salty",  "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Grilled Salmon", "lunch", "dining in","salty", "healthy",  "light", "img", "No Recipe"))

foodList.append(Fooditem("Meatloaf", "lunch", "dining in", "salty", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Fries", "lunch", "dining in", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Hot Dog","lunch", "dining in","salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Ravioli", "lunch", "dining in", "salty", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Wings", "lunch", "dining in", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Fried Mozzerlla", "lunch", "dining in", "salty", "casual", "light", "img", "No Recipe"))

foodList.append(Fooditem("Nachoes", "lunch", "dining in", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Burrito", "lunch", "dining in","salty", "casual",  "full", "img", "No Recipe"))
foodList.append(Fooditem("Hamburger", "lunch", "dining in","salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Spaghetti", "lunch", "dining in","salty", "casual",  "full", "img", "No Recipe"))
foodList.append(Fooditem("Casserole", "lunch", "dining in","salty", "casual",  "full", "img", "No Recipe"))
#=========================================Dinner=======================================#

foodList.append(Fooditem("Angel Cake", "dinner", "dining out", "sweet", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Fruit Smoothie", "dinner", "dining out","sweet","healthy","light", "img", "No Recipe"))

foodList.append(Fooditem("Strawberry Cake", "dinner", "dining out","sweet","healthy","full", "img", "No Recipe"))
foodList.append(Fooditem("Sweet Crepes", "Muffins" ,"dinner", "dining out","sweet","healthy","full", "img", "No Recipe"))
foodList.append(Fooditem("Muffins" ,"dinner", "dining out", "sweet", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Ice Cream", "dinner", "dining out", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Cupcakes", "dinner", "dining out", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Croissants", "dinner", "dining out", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Boba", "dinner", "dining out", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Castella", "dinner", "dining out", "sweet", "casual", "light", "img", "No Recipe"))

foodList.append(Fooditem(
foodList.append(Fooditem(
foodList.append(Fooditem(
foodList.append(Fooditem(
foodList.append(Fooditem(
foodList.append(Fooditem(
foodList.append(Fooditem(
foodList.append(Fooditem(
foodList.append(Fooditem(
foodList.append(Fooditem(
foodList.append(Fooditem(

# 00001       "lunch", "dining out","sweet","healthy"", "light"  = Angelcake, Fruit Smoothie
# 00001       "lunch", "dining out","sweet", "healthy", "full"   = Strawberry Cake,"sweet" Crepes, Muffins 
# 00010       "lunch", "dining out", "sweet", "casual", "light"   = IceCream, Cupcakes, Croissants , Boba, Castella
# 00011       "lunch", "dining out", "sweet", "casual", "full"    = Puffle Waffles, Banana Split, Cheesecake, Peach Cobbler 
# 00100       "lunch", "dining out", "salty", "healthy", "light"  = Baked Salmon, GrilledSalmon, GrilledChicken


"Steak", "Omelette", "Pot Roast"," Meatloaf", "lunch", "dining out", "salty", "healthy", "full"   
"Fries", "HotDog", "Ravioli", "Wings", "Fried Mozzerella", "lunch", "dining out", "salty", "casual", "light" 
"Nachos", "Burrito", "Hamburger,Spaghetti", "Casserole", "lunch", "dining out", "salty", "casual", "full" 
"Strawberry Cake", "Sweet Crepes", "Muffins" ,  "lunch", "dining in", "sweet", "healthy", "full"     
"Cupcakes", "Croissants" , "Boba", "Castella", "lunch", "dining in","sweet","casual","light"    
"Puffle Waffles", "Banana Split", "Cheesecake", "Peach Cobbler",  "lunch", "dining in","sweet","casual","full"     
"Baked Salmon", "GrilledChicken", "GrilledSalmon",  "lunch", "dining in","salty","healthy","light"   
"Steak", "Omelette", "Pot Roast", "Meatloaf", "lunch", "dining in","salty","healthy","full"     
"Fries", "HotDog", "Ravioli", "Wings", "Fried Mozzerella", "Noodles", "lunch", "dining in","salty","casual","light"     
"Nachos", "Burrito", "Hamburger","Spaghetti", "Casserole", "lunch", "dining in","salty","casual","full"


#################################Dinner############################
"Angelcake", "Fruit Smoothie", "dinner", "dining out","sweet","healthy","light"   
"Strawberry Cake", "Sweet Crepes", "Muffins" ,"dinner", "dining out","sweet","healthy","full"  = Strawberry Cake,"sweet" Crepes, Muffins
"IceCream", "Cupcakes", "Croissants" , "Boba", "Castella","dinner", "dining out","sweet","casual","light"  = IceCream, Cupcakes, Croissants , Boba, Castella



"Puffle Waffles", "Banana Split", "Cheesecake", "Peach Cobbler", "dinner", "dining out","sweet","casual","full"   = Puffle Waffles, Banana Split, Cheesecake, Peach Cobbler
"Baked Salmon", "GrilledChicken", "GrilledSalmon", "dinner", "dining out","salty","healthy","light" = Baked Salmon, GrilledChicken, GrilledSalmon
"Steak", "Omelette", "Pot Roast", "Meatloaf", "dinner", "dining out","salty","healthy","full"  = Steak, Omelette, Pot Roast, Meatloaf
"Fries", "HotDog", "Ravioli", "Wings", "Fried Mozzerella", "Noodles", "dinner", "dining out","salty","casual","light"  = Fries, HotDog, Ravioli, Wings, Fried Mozzerella, Noodles
"Nachos", "Burrito", "Hamburger","Spaghetti", "Casserole", "dinner", "dining out","salty","casual","full"   = Nachos, Burrito, Hamburger,Spaghetti, Casserole 
"Angelcake", "Fruit Smoothie", "dinner", "dining in","sweet","healthy","light"  = Angelcake, Fruit Smoothie
"Strawberry Cake", "Sweet Crepes", "Muffins", "dinner", "dining in","sweet","healthy","full"   = Strawberry Cake,"sweet" Crepes, Muffins 
"IceCream", "Cupcakes", "Croissants" , "Boba", "Castella", "dinner", "dining in","sweet","casual","light"   = IceCream, Cupcakes, Croissants , Boba, Castella
"Puffle Waffles", "Banana Split", "Cheesecake", "Peach Cobbler", "dinner", "dining in","sweet","casual","full"    = Puffle Waffles, Banana Split, Cheesecake, Peach Cobbler
"Baked Salmon", "GrilledChicken", "GrilledSalmon", "dinner", "dining in","salty","healthy","light"  = Baked Salmon, GrilledChicken, GrilledSalmon
"Steak", "Omelette", "Pot Roast", "Meatloaf", "dinner", "dining in","salty","healthy","full"   = Steak, Omelette, Pot Roast, Meatloaf
"Fries", "HotDog", "Ravioli", "Wings", "Fried Mozzerella", "Noodles", "dinner", "dining in","salty","casual","light"   = Fries, HotDog, Ravioli, Wings, Fried Mozzerella, Noodles
"Nachos", "Burrito", "Hamburger","Spaghetti", "Casserole", "dinner", "dining in","salty","casual","full"    = Nachos, Burrito, Hamburger,Spaghetti, Casserole 
"Fruit bowl", "Smoothie", "Muffins", "Rice", "breakfast","dining out","sweet","healthy","light"  = Fruit bowl, Smoothie, Muffins, Rice
"Acai Bowl", "Protein Smoothie", "Oatmeal", "breakfast","dining out","sweet","healthy","full"   = Acai Bowl, Protein Smoothie, Oatmeal
"Donut", "Cereal", "breakfast","dining out","sweet","casual","light"   = Donut, Cereal
"Pancakes", "Waffles", "Crepes", "French Toast", "breakfast","dining out","sweet","casual","full"    = Pancakes, Waffles, Crepes, French Toast
"Bagel", "Avocado Toast", "Buttered Toast", "breakfast","dining out","salty","healthy","light"  = Bagel, Avocado Toast, Buttered Toast
"Omelette", "Salmon Toast,"  "breakfast","dining out","salty","healthy","full"   = Omelette, Salmon Toast 
"Sausages", "Miso Soup", "breakfast","dining out","salty","casual","light"   = Sausages, Miso Soup 
"Bacon", "Breakfast Burrito"  "breakfast","dining out","salty","casual","full"    = Bacon,"breakfast" Burrito 
"Yogurt", "Parfait" "breakfast","dining in","sweet","healthy","light"   = Yogurt, Parfait
"Acai Bowl", "Protein Smoothie", "Oatmeal", "breakfast","dining in","sweet","healthy","full"    = Acai Bowl, Protein Smoothie, Oatmeal
"Poptarts", "Cereal", "Donuts", "breakfast","dining in","sweet","casual","light"    = Poptarts, Cereal, Donuts
"Pancakes", "Waffles", "Crepes" "Buttered Toast", "breakfast","dining in","salty","healthy","light"   = Bagel, Avocado Toast, Buttered Toast
"Omelette", "Salmon Toast", "breakfast","dining in","salty","healthy","full"    = Omelette, Salmon Toast 
"Sausages", "Miso Soup", "breakfast","dining in","salty","casual","light"    = Sausages, Miso Soup 
"Bacon","Breakfast Burrito", "Omelette", "breakfast","dining in","salty","casual","full"     = Bacon,"breakfast" Burrito, Omelette













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