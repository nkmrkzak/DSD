print("3-15")
cats = [
    "Henri",
    "Grumpy",
    "Lucy",
]
animails = {
    "cats": cats,
    "octopi": {},
    "emus": {},
}
life = {
    "animals": animails,
    "plants": {},
    "other": {},
}
print(life)

print("3-16")
print(life.keys())

print("3-17")
print(life["animals"])

print("3-18")
print(life["animals"]["cats"])