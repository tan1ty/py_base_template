import csv


with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["lenguage"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

def get_value(language):
    return counts[language]

favorite = input("Favorite: ")
if favorite in counts:
    print(f"{favorite}: {counts[favorite]}")