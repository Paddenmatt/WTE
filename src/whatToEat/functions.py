def importFood():
    with open("Database.txt") as Database:
        FM = FoodManager()
        for row in Database:
            row = row.split(",", ":")


