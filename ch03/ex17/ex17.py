print("3-17")

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

# print(life["animals"].keys())
print(life.get("animals", {}).keys()) 