print("3-18")

cats = [
    "Henri",
    "Grumpy",
    "Lucy",
]
animals = {
    "cats": cats,
    "octopi": {},
    "emus": {},
}
life = {
    "animals": animals,
    "plants": {},
    "other": {},
}

# print(life["animals"]["cats"])
print(life.get("animals", {}).get("cats"))
