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

foodList.append(Fooditem("Angel Food Cake", "lunch", "dining out", "sweet", "healthy", "light", "images/angelcake.jpg", "No Recipe"))
foodList.append(Fooditem("Fruit Smoothie", "lunch", "dining out", "sweet", "healthy", "light", "images/fruitsmoothies.jpg", "No Recipe"))

foodList.append(Fooditem("Strawberry Cake", "lunch", "dining out", "sweet", "healthy", "full", "images/strawberrycake.jpg", "No Recipe"))
foodList.append(Fooditem("Sweet Crepes", "lunch", "dining out", "sweet", "healthy", "full", "images/sweetcrepes.jpg", "No Recipe"))
foodList.append(Fooditem("Muffins", "lunch", "dining out", "sweet", "healthy", "full", "images/muffins.jpg", "No Recipe"))

foodList.append(Fooditem("Ice Cream", "lunch", "dining out","sweet", "casual", "light", "images/icecream.jpg", "No Recipe"))
foodList.append(Fooditem("Cupcakes", "lunch", "dining out", "sweet", "casual", "light", "images/cupcakes.jpg", "No Recipe"))
foodList.append(Fooditem("Croissants", "lunch", "dining out", "sweet", "casual", "light", "images/croissant.jpg", "No Recipe"))
foodList.append(Fooditem("Boba", "lunch", "dining out", "sweet", "casual", "light", "images/boba.jpg", "No Recipe"))
foodList.append(Fooditem("Castella", "lunch", "dining out", "sweet", "casual", "light", "images/castella.jpg", "No Recipe"))

foodList.append(Fooditem("Puffle Waffles", "lunch", "dining out", "sweet", "casual", "full", "images/pufflewaffles.jpg", "No Recipe"))
foodList.append(Fooditem("Banana Split", "lunch", "dining out", "sweet", "casual", "full", "images/bananasplit.jpg", "No Recipe"))
foodList.append(Fooditem("Cheesecake", "lunch", "dining out", "sweet", "casual", "full", "images/cheesecake.jpg", "No Recipe"))
foodList.append(Fooditem("Peach Cobbler", "lunch", "dining out", "sweet", "casual", "full", "images/peachcobbler.jpg", "No Recipe"))

foodList.append(Fooditem("Baked Salmon", "lunch", "dining out", "salty", "healthy", "light", "images/bakedsalmon.jpeg", "No Recipe"))
foodList.append(Fooditem("Grilled Chicken", "lunch", "dining out","salty",  "healthy", "light", "images/grilledchicken.jpg", "No Recipe"))
foodList.append(Fooditem("Grilled Salmon", "lunch", "dining out","salty", "healthy",  "light", "images/grilledsalmon.jpg", "No Recipe"))

foodList.append(Fooditem("Meatloaf", "lunch", "dining out", "salty", "healthy", "full", "images/meatloaf.jpg", "No Recipe"))

foodList.append(Fooditem("Fries", "lunch", "dining out", "salty", "casual", "light", "images/fries.jpg", "No Recipe"))
foodList.append(Fooditem("Hot Dog","lunch", "dining out","salty", "casual", "light", "images/hotdog.jpg", "No Recipe"))
foodList.append(Fooditem("Ravioli", "lunch", "dining out", "salty", "healthy", "light", "images/ravioli.jpg", "No Recipe"))
foodList.append(Fooditem("Wings", "lunch", "dining out", "salty", "casual", "light", "images/wings.jpg", "No Recipe"))
foodList.append(Fooditem("Fried Mozzarella", "lunch", "dining out", "salty", "casual", "light", "images/friedmozzarella.jpg", "No Recipe"))

foodList.append(Fooditem("Nachos", "lunch", "dining out", "salty", "casual", "full", "images/nachos.jpeg", "No Recipe"))
foodList.append(Fooditem("Burrito", "lunch", "dining out","salty", "casual",  "full", "images/burrito.jpg", "No Recipe"))
foodList.append(Fooditem("Hamburger", "lunch", "dining out","salty", "casual", "full", "images/hamburger.jpg", "No Recipe"))
foodList.append(Fooditem("Spaghetti", "lunch", "dining out","salty", "casual",  "full", "images/spaghetti.jpg", "No Recipe"))
foodList.append(Fooditem("Casserole", "lunch", "dining out","salty", "casual",  "full", "images/casserole.jpg", "No Recipe"))

#===============================Lunch "cook at home"===============================#

foodList.append(Fooditem("Strawberry Cake", "lunch", "cook at home", "sweet", "healthy", "full", "images/strawberrycake.jpg", "https://www.allrecipes.com/recipe/272783/red-velvet-strawberry-cake/"))
foodList.append(Fooditem("Sweet Crepes", "lunch", "cook at home", "sweet", "healthy", "full", "images/sweetcrepes.jpg", "https://www.allrecipes.com/recipe/280785/sweet-peach-crepe-filling/"))
foodList.append(Fooditem("Muffins", "lunch", "cook at home", "sweet", "healthy", "full", "images/muffins.jpg", "https://www.allrecipes.com/recipe/229968/judys-pumpkin-muffins/"))

foodList.append(Fooditem("Cupcakes", "lunch", "cook at home","sweet","casual","light", "images/cupcakes.jpg", "https://www.allrecipes.com/recipe/240279/applesauce-filled-cupcakes/"))
foodList.append(Fooditem("Boba", "lunch", "cook at home","sweet","casual","light", "images/boba.jpg", "https://www.allrecipes.com/recipe/266015/boba-coconut-milk-black-tea-with-tapioca-pearls/"))

foodList.append(Fooditem("Banana Split", "lunch", "cook at home", "sweet", "casual", "full", "images/bananasplit.jpg", "https://www.allrecipes.com/recipe/8344/banana-split-cake-iii/"))
foodList.append(Fooditem("Cheesecake", "lunch", "cook at home", "sweet", "casual", "full", "images/cheesecake.jpg", "https://www.allrecipes.com/recipe/25958/basic-cheesecake/"))
foodList.append(Fooditem("Peach Cobbler", "lunch", "cook at home", "sweet", "casual", "full", "images/peachcobbler.jpg", "https://www.allrecipes.com/recipe/19044/easy-peach-cobbler/"))

foodList.append(Fooditem("Baked Salmon", "lunch", "cook at home", "salty", "healthy", "light", "images/bakedsalmon.jpeg", "https://www.allrecipes.com/recipe/22538/baked-salmon-fillets-dijon/"))
foodList.append(Fooditem("Grilled Chicken", "lunch", "cook at home","salty",  "healthy", "light", "images/grilledchicken.jpg", "https://www.allrecipes.com/recipe/256527/grilled-chicken-thighs-and-marinade/"))
foodList.append(Fooditem("Grilled Salmon", "lunch", "cook at home","salty", "healthy",  "light", "images/grilledsalmon.jpg", "https://www.allrecipes.com/recipe/48855/grilled-salmon-kyoto/"))

foodList.append(Fooditem("Meatloaf", "lunch", "cook at home", "salty", "healthy", "full", "images/meatloaf.jpg", "https://www.allrecipes.com/recipe/268958/skinny-meatloaf/"))

foodList.append(Fooditem("Fries", "lunch", "cook at home", "salty", "casual", "light", "images/fries.jpg", "https://www.allrecipes.com/recipe/35963/french-fried-potatoes/"))
foodList.append(Fooditem("Hot Dog","lunch", "cook at home","salty", "casual", "light", "images/hotdog.jpg", "https://www.allrecipes.com/recipe/24713/texas-hotdog-sauce/"))
foodList.append(Fooditem("Ravioli", "lunch", "cook at home", "salty", "healthy", "light", "images/ravioli.jpg", "https://www.allrecipes.com/recipe/219174/easy-butternut-squash-ravioli/"))
foodList.append(Fooditem("Wings", "lunch", "cook at home", "salty", "casual", "light", "images/wings.jpg", "https://www.allrecipes.com/recipe/260032/simple-grilled-hot-wings/"))
foodList.append(Fooditem("Fried Mozzarella", "lunch", "cook at home", "salty", "casual", "light", "images/friedmozzarella.jpg", "https://www.allrecipes.com/recipe/278265/fried-mozzarella-puffs/"))

foodList.append(Fooditem("Nachos", "lunch", "cook at home", "salty", "casual", "full", "images/nachos.jpeg", "https://www.allrecipes.com/recipe/240380/chili-nachos/"))
foodList.append(Fooditem("Burrito", "lunch", "cook at home", "salty", "casual", "full", "images/burrito.jpg", "https://www.allrecipes.com/recipe/256301/carne-asada-breakfast-burrito/"))
foodList.append(Fooditem("Hamburger", "lunch", "cook at home","salty", "casual", "full", "images/hamburger.jpg", "https://www.allrecipes.com/recipe/177115/feta-stuffed-hamburgers/"))
foodList.append(Fooditem("Spaghetti", "lunch", "cook at home", "salty", "casual", "full", "images/spaghetti.jpg", "https://www.allrecipes.com/recipe/19905/dads-spaghetti/"))
foodList.append(Fooditem("Casserole", "lunch", "cook at home", "salty", "casual", "full", "images/casserole.jpg", "https://www.allrecipes.com/recipe/275829/jalapeno-creamed-corn-casserole/"))

#=========================================Dinner=======================================#

foodList.append(Fooditem("Angel Cake", "dinner", "dining out", "sweet", "healthy", "light", "images/angelcake.jpg", "No Recipe"))
foodList.append(Fooditem("Fruit Smoothie", "dinner", "dining out","sweet","healthy","light", "images/fruitsmoothie.jpg", "No Recipe"))

foodList.append(Fooditem("Strawberry Cake", "dinner", "dining out", "sweet", "healthy", "full", "images/strawberrycake.jpg", "No Recipe"))
foodList.append(Fooditem("Sweet Crepes", "dinner", "dining out", "sweet", "healthy", "full", "images/sweetcrepes.jpg", "No Recipe"))
foodList.append(Fooditem("Muffins" ,"dinner", "dining out", "sweet", "healthy", "full", "images/muffins.jpg", "No Recipe"))

foodList.append(Fooditem("Ice Cream", "dinner", "dining out", "sweet", "casual", "light", "images/icecream.jpg", "No Recipe"))
foodList.append(Fooditem("Cupcakes", "dinner", "dining out", "sweet", "casual", "light", "images/cupcakes.jpg", "No Recipe"))
foodList.append(Fooditem("Croissants", "dinner", "dining out", "sweet", "casual", "light", "images/croissant.jpg", "No Recipe"))
foodList.append(Fooditem("Boba", "dinner", "dining out", "sweet", "casual", "light", "images/boba.jpg", "No Recipe"))
foodList.append(Fooditem("Castella", "dinner", "dining out", "sweet", "casual", "light", "images/castella.jpg", "No Recipe"))

foodList.append(Fooditem("Puffle Waffles", "dinner", "dining out", "sweet", "casual","full", "images/pufflewaffles.jpg", "No Recipe"))
foodList.append(Fooditem("Banana Split", "dinner", "dining out", "sweet", "casual", "full", "images/bananasplit.jpg", "No Recipe"))
foodList.append(Fooditem("Cheesecake", "dinner", "dining out", "sweet", "casual", "full", "images/cheesecake.jpg", "No Recipe"))
foodList.append(Fooditem("Peach Cobbler", "dinner", "dining out", "sweet", "casual", "full", "images/peachcobbler.jpg", "No Recipe"))

foodList.append(Fooditem("Baked Salmon", "dinner", "dining out", "salty", "healthy", "light", "images/bakedsalmon.jpeg", "No Recipe"))
foodList.append(Fooditem("Grilled Chicken", "dinner", "dining out", "salty", "healthy", "light", "images/grilledchicken.jpg", "No Recipe"))
foodList.append(Fooditem("Grilled Salmon", "dinner", "dining out", "salty", "healthy", "light", "images/grilledsalmon.jpg", "No Recipe"))

foodList.append(Fooditem("Steak", "dinner", "dining out", "salty", "healthy", "full", "images/steak.jpg", "No Recipe"))
foodList.append(Fooditem("Omelette", "dinner", "dining out", "salty", "healthy", "full", "images/omelet.jpg", "No Recipe"))
foodList.append(Fooditem("Pot Roast", "dinner", "dining out", "salty", "healthy", "full", "images/potroast.jpg", "No Recipe"))
foodList.append(Fooditem("Meatloaf", "dinner", "dining out", "salty", "healthy", "full", "images/meatloaf.jpg", "No Recipe"))

foodList.append(Fooditem("Fries", "dinner", "dining out", "salty", "casual", "light", "images/fries.jpg", "No Recipe"))
foodList.append(Fooditem("Hot Dog", "dinner", "dining out", "salty", "casual", "light", "images/hotdog.jpg", "No Recipe"))
foodList.append(Fooditem("Ravioli", "dinner", "dining out", "salty", "casual", "light", "images/ravioli.jpg", "No Recipe"))
foodList.append(Fooditem("Wings", "dinner", "dining out", "salty", "casual", "light", "images/wings.jpg", "No Recipe"))
foodList.append(Fooditem("Fried Mozzerella", "dinner", "dining out", "salty", "casual", "light", "images/friedmozzarella.jpg", "No Recipe"))
foodList.append(Fooditem("Noodles", "dinner", "dining out", "salty", "casual", "light", "images/noodles.jpg", "No Recipe"))

foodList.append(Fooditem("Nachos", "dinner", "dining out", "salty", "casual", "full", "images/nachos.jpeg", "No Recipe"))
foodList.append(Fooditem("Burrito", "dinner", "dining out", "salty", "casual", "full", "images/burrito.jpg", "No Recipe"))
foodList.append(Fooditem("Hamburger", "dinner", "dining out", "salty", "casual", "full", "images/hamburger.jpg", "No Recipe"))
foodList.append(Fooditem("Spaghetti", "dinner", "dining out", "salty", "casual", "full", "images/spaghetti.jpg", "No Recipe"))
foodList.append(Fooditem("Casserole", "dinner", "dining out", "salty", "casual", "full", "images/casserole.jpg", "No Recipe"))

#=====================================Dinner "cook at home"===================================#

foodList.append(Fooditem("Fruit Smoothie", "dinner", "cook at home", "sweet", "healthy", "light", "images/fruitsmoothies.jpg", "https://www.allrecipes.com/recipe/87961/triple-threat-fruit-smoothie/"))

foodList.append(Fooditem("Strawberry Cake", "dinner", "cook at home", "sweet", "healthy", "full", "images/strawberrycake.jpg", "https://www.allrecipes.com/recipe/272783/red-velvet-strawberry-cake/"))
foodList.append(Fooditem("Muffins", "dinner", "cook at home", "sweet", "healthy", "full", "images/muffins.jpg", "https://www.allrecipes.com/recipe/229968/judys-pumpkin-muffins/"))

foodList.append(Fooditem("Cupcakes", "dinner", "cook at home", "sweet", "casual", "light", "images/cupcakes.jpg", "https://www.allrecipes.com/recipe/240279/applesauce-filled-cupcakes/"))
foodList.append(Fooditem("Croissants", "dinner", "cook at home", "sweet", "casual", "light", "images/croissant.jpg", "https://www.allrecipes.com/recipe/240268/chocolate-croissant-bread-pudding/"))

foodList.append(Fooditem("Banana Split", "dinner", "cook at home", "sweet", "casual", "full", "images/bananasplit.jpg", "https://www.allrecipes.com/recipe/8344/banana-split-cake-iii/"))
foodList.append(Fooditem("Cheesecake", "dinner", "cook at home", "sweet", "casual", "full", "images/cheesecake.jpg", "https://www.allrecipes.com/recipe/25958/basic-cheesecake/"))
foodList.append(Fooditem("Peach Cobbler", "dinner", "cook at home", "sweet", "casual", "full", "images/peachcobbler.jpg", "https://www.allrecipes.com/recipe/19044/easy-peach-cobbler/"))

foodList.append(Fooditem("Baked Salmon", "dinner", "cook at home", "salty", "healthy", "light", "images/bakedsalmon.jpeg", "https://www.allrecipes.com/recipe/22538/baked-salmon-fillets-dijon/"))
foodList.append(Fooditem("Grilled Chicken", "dinner", "cook at home", "salty", "healthy", "light", "images/grilledchicken.jpg", "https://www.allrecipes.com/recipe/256527/grilled-chicken-thighs-and-marinade/"))
foodList.append(Fooditem("Grilled Salmon", "dinner", "cook at home", "salty", "healthy", "light", "images/grilledsalmon.jpg", "https://www.allrecipes.com/recipe/48855/grilled-salmon-kyoto/"))

foodList.append(Fooditem("Steak", "dinner", "cook at home", "salty", "healthy", "full", "images/steak.jpg", "https://www.allrecipes.com/recipe/258804/butchers-steak-hanger-steak/"))
foodList.append(Fooditem("Omelette", "dinner", "cook at home", "salty", "healthy", "full", "images/omelet.jpg", "https://www.allrecipes.com/recipe/257918/chef-johns-french-omelette/"))
foodList.append(Fooditem("Pot Roast", "dinner", "cook at home", "salty", "healthy", "full", "images/potroast.jpg", "https://www.allrecipes.com/recipe/232756/pot-roast/"))
foodList.append(Fooditem("Meatloaf", "dinner", "cook at home", "salty", "healthy", "full", "images/meatloaf.jpg", "No Recipe"))

foodList.append(Fooditem("Fries", "dinner", "cook at home", "salty", "casual", "light", "images/fries.jpg", "https://www.allrecipes.com/recipe/35963/french-fried-potatoes/"))
foodList.append(Fooditem("Hot Dog", "dinner", "cook at home", "salty", "casual", "light", "images/hotdog.jpg", "https://www.allrecipes.com/recipe/24713/texas-hotdog-sauce/"))
foodList.append(Fooditem("Ravioli", "dinner", "cook at home", "salty", "casual", "light", "images/ravioli.jpg", "https://www.allrecipes.com/recipe/219174/easy-butternut-squash-ravioli/"))
foodList.append(Fooditem("Wings", "dinner", "cook at home", "salty", "casual", "light", "images/wings.jpg", "https://www.allrecipes.com/recipe/260032/simple-grilled-hot-wings/"))
foodList.append(Fooditem("Noodles", "dinner", "cook at home", "salty", "casual", "light", "images/noodles.jpg", "https://www.allrecipes.com/recipe/222405/polish-noodles-cottage-cheese-and-noodles/"))

foodList.append(Fooditem("Nachos", "dinner", "cook at home", "salty", "casual", "full", "images/nachos.jpg", "https://www.allrecipes.com/recipe/240380/chili-nachos/"))
foodList.append(Fooditem("Burrito", "dinner", "cook at home", "salty", "casual", "full", "images/burrito.jpg", "https://www.allrecipes.com/recipe/256301/carne-asada-breakfast-burrito/"))
foodList.append(Fooditem("Hamburger", "dinner", "cook at home", "salty", "casual", "full", "images/hamburger.jpg", "https://www.allrecipes.com/recipe/177115/feta-stuffed-hamburgers/"))
foodList.append(Fooditem("Spaghetti", "dinner", "cook at home", "salty", "casual", "full", "images/spaghetti.jpg", "https://www.allrecipes.com/recipe/19905/dads-spaghetti/"))
foodList.append(Fooditem("Casserole", "dinner", "cook at home", "salty", "casual", "full", "images/casserole.jpg", "https://www.allrecipes.com/recipe/275829/jalapeno-creamed-corn-casserole/"))

#====================================Breakfast==================================#

foodList.append(Fooditem("Fruit bowl", "breakfast", "dining out", "sweet", "healthy", "light", "images/fruitbowl.jpg", "No Recipe"))
foodList.append(Fooditem("Smoothie", "breakfast", "dining out", "sweet", "healthy", "light", "images/smoothie.jpg", "No Recipe"))
foodList.append(Fooditem("Muffins", "breakfast", "dining out", "sweet", "healthy", "light", "images/muffins.jpg", "No Recipe"))
foodList.append(Fooditem("Rice", "breakfast", "dining out", "sweet", "healthy", "light", "images/rice.jpg", "No Recipe"))

foodList.append(Fooditem("Acai Bowl", "breakfast", "dining out", "sweet", "healthy", "full", "images/acaibowl.jpg", "No Recipe"))
foodList.append(Fooditem("Protein Smoothie", "breakfast", "dining out", "sweet", "healthy", "full", "images/proteinsmoothie.jpg", "No Recipe"))
foodList.append(Fooditem("Oatmeal", "breakfast", "dining out", "sweet", "healthy", "full", "images/oatmeal.jpg", "No Recipe"))

foodList.append(Fooditem("Donut", "breakfast", "dining out", "sweet", "casual", "light", "images/donut.jpg", "No Recipe"))

foodList.append(Fooditem("Pancakes", "breakfast", "dining out", "sweet", "casual", "full", "images/pancakes.jpg", "No Recipe"))
foodList.append(Fooditem("Waffles", "breakfast", "dining out", "sweet", "casual", "full", "images/waffles.jpg", "No Recipe"))
foodList.append(Fooditem("Crepes", "breakfast", "dining out", "sweet", "casual", "full", "images/savorycrepe.jpg", "No Recipe"))
foodList.append(Fooditem("French Toast", "breakfast", "dining out", "sweet", "casual", "full", "images/frenchtoast.jpg", "No Recipe"))

foodList.append(Fooditem("Bagel", "breakfast", "dining out", "salty", "healthy", "light", "images/bagel.jpg", "No Recipe"))
foodList.append(Fooditem("Avocado Toast", "breakfast", "dining out", "salty", "healthy", "light", "images/avocadotoast.jpg", "No Recipe"))

foodList.append(Fooditem("Omelette", "breakfast", "dining out", "salty", "healthy", "full", "images/omelet.jpg", "No Recipe"))
foodList.append(Fooditem("Salmon Toast", "breakfast", "dining out", "salty", "healthy", "full", "images/salmontoast.jpg", "No Recipe"))

foodList.append(Fooditem("Sausages", "breakfast", "dining out", "salty", "casual","light", "images/sausages.jpg", "No Recipe"))
foodList.append(Fooditem("Miso Soup", "breakfast", "dining out", "salty", "casual", "light", "images/misosoup.jpg", "No Recipe"))

foodList.append(Fooditem("Bacon", "breakfast", "dining out", "salty", "casual", "full", "images/bacon.jpg", "No Recipe"))
foodList.append(Fooditem("Breakfast Burrito", "breakfast", "dining out", "salty", "casual", "full", "images/breakfastburrito.jpg", "No Recipe"))

#=========================================Breakfast "cook at home"=========================================#

foodList.append(Fooditem("Yogurt", "breakfast", "cook at home", "sweet", "healthy", "light", "images/yogurt.jpg", "https://www.allrecipes.com/recipe/262645/instant-pot-greek-yogurt/"))
foodList.append(Fooditem("Parfait", "breakfast", "cook at home", "sweet", "healthy", "light", "images/parfait.jpg", "https://www.allrecipes.com/recipe/15592/pumpkin-parfait/"))

foodList.append(Fooditem("Acai Bowl", "breakfast", "cook at home", "sweet", "healthy", "full", "images/acaibowl.jpg", "https://www.allrecipes.com/recipe/244353/acai-bowl/"))  
foodList.append(Fooditem("Protein Smoothie", "breakfast", "cook at home", "sweet", "healthy", "full", "images/proteinsmoothie.jpg", "https://www.allrecipes.com/recipe/245552/power-9-protein-smoothie/"))
foodList.append(Fooditem("Oatmeal", "breakfast", "cook at home", "sweet", "healthy", "full", "images/oatmeal.jpg", "https://www.allrecipes.com/recipe/246423/power-oatmeal/"))

foodList.append(Fooditem("Poptarts", "breakfast", "cook at home", "sweet", "casual", "light", "images/poptart.jpg", "https://www.cookingclassy.com/homemade-pop-tarts/")) 
foodList.append(Fooditem("Donuts", "breakfast", "cook at home", "sweet", "casual", "light", "images/donut.jpg", "https://www.allrecipes.com/recipe/276267/baked-chocolate-donuts/")) 
foodList.append(Fooditem("Cereal", "breakfast", "cook at home", "sweet", "casual", "light", "images/cereal.jpg", "https://www.allrecipes.com/recipe/23927/crispy-cereal-mix/"))

foodList.append(Fooditem("Buttered Toast", "breakfast", "cook at home", "salty", "healthy", "light", "images/butteredtoast.jpg", "https://www.allrecipes.com/recipe/213730/peanut-butter-french-toast/"))
foodList.append(Fooditem("Crepes", "breakfast", "cook at home", "salty", "healthy", "light", "images/savorycrepes.jpg", "https://www.allrecipes.com/recipe/280785/sweet-peach-crepe-filling/"))
foodList.append(Fooditem("Waffles","breakfast", "cook at home", "salty", "healthy", "light", "images/waffles.jpg", "https://www.allrecipes.com/recipe/269426/eggnog-waffles/"))

foodList.append(Fooditem("Salmon Toast", "breakfast", "cook at home", "salty", "healthy", "full", "images/salmontoast.jpg", "https://www.allrecipes.com/recipe/240097/smoked-salmon-french-toast-sandwich/"))
foodList.append(Fooditem("Omelette", "breakfast", "cook at home", "salty", "healthy", "full", "images/healthyomelet.jpg", "https://easychickenrecipes.com/healthy-omelette-recipe/"))

foodList.append(Fooditem("Miso Soup", "breakfast", "cook at home", "salty", "casual", "light", "images/misosoup.jpg", "https://www.allrecipes.com/recipe/276865/vegan-miso-soup/"))
foodList.append(Fooditem("Sausages", "breakfast", "cook at home", "salty", "casual", "light", "images/sausages.jpg", "https://www.allrecipes.com/recipe/22343/sausages-in-onion-gravy/"))

foodList.append(Fooditem("Omelette", "breakfast", "cook at home", "salty", "casual", "full", "images/omelet.jpg", "https://www.allrecipes.com/recipe/257918/chef-johns-french-omelette/"))
foodList.append(Fooditem("Bacon", "breakfast", "cook at home", "salty", "casual", "full", "images/bacon.jpg", "https://www.allrecipes.com/recipe/50311/bacon/"))
foodList.append(Fooditem("Breakfast Burrito", "breakfast", "cook at home", "salty", "casual", "full", "images/breakfastburrito.jpg", "https://www.allrecipes.com/recipe/274779/avocado-and-egg-breakfast-burrito/"))