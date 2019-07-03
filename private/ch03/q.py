print("3-1")
years_list = [1990, 1991, 1992, 1993, 1994, 1995]
print(years_list)

print("3-2")
print(years_list[3])

print("3-3")
print(max(years_list))

print("3-4")
things = ["mozzarella", "cinderella", "salmonella"]
print(things)

print("3-5")
print(things[1].capitalize())
print(things)

print("3-6")
print(things[0].upper())

print("3-7")
del things[things.index("salmonella")]
print(things)

print("3-8")
surprise = ["Groucho", "Chico", "Harpo"]
print(surprise)

print("3-9")
surprise[-1] = surprise[-1].lower()
surprise.reverse()
print(surprise)
surprise[0] = surprise[0].capitalize()
print(surprise)

print("3-10")
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}
print(e2f)

print("3-11")
print(e2f["walrus"])

print("3-12")
f2e = {v:k for k, v in e2f.items()}
print(f2e)

print("3-13")
print(f2e["chien"])

print("3-14")
print(set(e2f))

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
