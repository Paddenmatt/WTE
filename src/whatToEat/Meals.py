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
foodList.append(Fooditem("Burrito", "lunch", "dining in", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Hamburger", "lunch", "dining in","salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Spaghetti", "lunch", "dining in", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Casserole", "lunch", "dining in", "salty", "casual", "full", "img", "No Recipe"))

#=========================================Dinner=======================================#

foodList.append(Fooditem("Angel Cake", "dinner", "dining out", "sweet", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Fruit Smoothie", "dinner", "dining out","sweet","healthy","light", "img", "No Recipe"))

foodList.append(Fooditem("Strawberry Cake", "dinner", "dining out", "sweet", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Sweet Crepes", "dinner", "dining out", "sweet", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Muffins" ,"dinner", "dining out", "sweet", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Ice Cream", "dinner", "dining out", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Cupcakes", "dinner", "dining out", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Croissants", "dinner", "dining out", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Boba", "dinner", "dining out", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Castella", "dinner", "dining out", "sweet", "casual", "light", "img", "No Recipe"))

foodList.append(Fooditem("Puffle Waffles", "dinner", "dining out", "sweet", "casual","full", "img", "No Recipe"))
foodList.append(Fooditem("Banana Split", "dinner", "dining out", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Cheesecake", "dinner", "dining out", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Peach Cobbler", "dinner", "dining out", "sweet", "casual", "full", "img", "No Recipe"))

foodList.append(Fooditem("Baked Salmon", "dinner", "dining out", "salty", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Grilled Chicken", "dinner", "dining out", "salty", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Grilled Salmon", "dinner", "dining out", "salty", "healthy", "light", "img", "No Recipe"))

foodList.append(Fooditem("Steak", "dinner", "dining out", "salty", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Omelette", "dinner", "dining out", "salty", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Pot Roast", "dinner", "dining out", "salty", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Meatloaf", "dinner", "dining out", "salty", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Fries", "dinner", "dining out", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Hot Dog", "dinner", "dining out", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Ravioli", "dinner", "dining out", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Wings", "dinner", "dining out", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Fried Mozzerella", "dinner", "dining out", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Noodles", "dinner", "dining out", "salty", "casual", "light", "img", "No Recipe"))

foodList.append(Fooditem("Nachoes", "dinner", "dining out", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Burrito", "dinner", "dining out", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Hamburger", "dinner", "dining out", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Spaghetti", "dinner", "dining out", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Casserole", "dinner", "dining out", "salty", "casual", "full", "img", "No Recipe"))

#=====================================Dinner "dining in"===================================#

foodList.append(Fooditem("Fruit Smoothie", "dinner", "dining in", "sweet", "healthy", "light", "img", "No Recipe"))

foodList.append(Fooditem("Strawberry Cake", "dinner", "dining in", "sweet", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Muffins", "dinner", "dining in", "sweet", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Cupcakes", "dinner", "dining in", "sweet", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Croissants", "dinner", "dining in", "sweet", "casual", "light", "img", "No Recipe"))

foodList.append(Fooditem("Banana Split", "dinner", "dining in", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Cheesecake", "dinner", "dining in", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Peach Cobbler", "dinner", "dining in", "sweet", "casual", "full", "img", "No Recipe"))

foodList.append(Fooditem("Baked Salmon", "dinner", "dining in", "salty", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Grilled Chicken", "dinner", "dining in", "salty", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Grilled Salmon", "dinner", "dining in", "salty", "healthy", "light", "img", "No Recipe"))

foodList.append(Fooditem("Steak", "dinner", "dining in", "salty", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Omelette", "dinner", "dining in", "salty", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Pot Roast", "dinner", "dining in", "salty", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Meatloaf", "dinner", "dining in", "salty", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Fries", "dinner", "dining in", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Hot Dog", "dinner", "dining in", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Ravioli", "dinner", "dining in", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Wings", "dinner", "dining in", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Noodles", "dinner", "dining in", "salty", "casual", "light", "img", "No Recipe"))

foodList.append(Fooditem("Nachoes", "dinner", "dining in", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Burrito", "dinner", "dining in", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Hamburger", "dinner", "dining in", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Spaghetti", "dinner", "dining in", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Casserole", "dinner", "dining in", "salty", "casual", "full", "img", "No Recipe"))

#====================================Breakfast==================================#

foodList.append(Fooditem("Fruit bowl", "breakfast", "dining out", "sweet", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Smoothie", "breakfast", "dining out", "sweet", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Muffins", "breakfast", "dining out", "sweet", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Rice", "breakfast", "dining out", "sweet", "healthy", "light", "img", "No Recipe"))

foodList.append(Fooditem("Acai Bowl", "breakfast", "dining out", "sweet", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Protein Smoothie", "breakfast", "dining out", "sweet", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Oatmeal", "breakfast", "dining out", "sweet", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Donut", "breakfast", "dining out", "sweet", "casual", "light", "img", "No Recipe"))

foodList.append(Fooditem("Pancakes", "breakfast", "dining out", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Waffles", "breakfast", "dining out", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Crepes", "breakfast", "dining out", "sweet", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("French Toast", "breakfast", "dining out", "sweet", "casual", "full", "img", "No Recipe"))

foodList.append(Fooditem("Bagel", "breakfast", "dining out", "salty", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Avocado Toast", "breakfast", "dining out", "salty", "healthy", "light", "img", "No Recipe"))

foodList.append(Fooditem("Omelette", "breakfast", "dining out", "salty", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Salmon Toast", "breakfast", "dining out", "salty", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Sausages", "breakfast", "dining out", "salty", "casual","light", "img", "No Recipe"))
foodList.append(Fooditem("Miso Soup", "breakfast", "dining out", "salty", "casual", "light", "img", "No Recipe"))

foodList.append(Fooditem("Bacon", "breakfast", "dining out", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Breakfast Burrito", "breakfast", "dining out", "salty", "casual", "full", "img", "No Recipe"))

#=========================================Breakfast "dining in"=========================================#

foodList.append(Fooditem("Yogurt", "breakfast", "dining in", "sweet", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Parfait", "breakfast", "dining in", "sweet", "healthy", "light", "img", "No Recipe"))

foodList.append(Fooditem("Acai Bowl", "breakfast", "dining in", "sweet", "healthy", "full", "img", "No Recipe"))  
foodList.append(Fooditem("Protein Smoothie", "breakfast", "dining in", "sweet", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Oatmeal", "breakfast", "dining in", "sweet", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Poptarts", "breakfast", "dining in", "sweet", "casual", "light", "img", "No Recipe")) 
foodList.append(Fooditem("Donuts", "breakfast", "dining in", "sweet", "casual", "light", "img", "No Recipe")) 
foodList.append(Fooditem("Cereal", "breakfast", "dining in", "sweet", "casual", "light", "img", "No Recipe"))

foodList.append(Fooditem("Buttered Toast", "breakfast", "dining in", "salty", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Crepes", "breakfast", "dining in", "salty", "healthy", "light", "img", "No Recipe"))
foodList.append(Fooditem("Waffles","breakfast", "dining in", "salty", "healthy", "light", "img", "No Recipe"))

foodList.append(Fooditem("Salmon Toast", "breakfast", "dining in", "salty", "healthy", "full", "img", "No Recipe"))
foodList.append(Fooditem("Omelette", "breakfast", "dining in", "salty", "healthy", "full", "img", "No Recipe"))

foodList.append(Fooditem("Miso Soup", "breakfast", "dining in", "salty", "casual", "light", "img", "No Recipe"))
foodList.append(Fooditem("Sausages", "breakfast", "dining in", "salty", "casual", "light", "img", "No Recipe"))
 
foodList.append(Fooditem("Omelette", "breakfast", "dining in", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Bacon", "breakfast", "dining in", "salty", "casual", "full", "img", "No Recipe"))
foodList.append(Fooditem("Breakfast Burrito", "breakfast", "dining in", "salty", "casual", "full", "img", "No Recipe"))