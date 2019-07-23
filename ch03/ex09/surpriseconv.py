surprise = ["Groucho", "Chico", "Harpo"]
# surprise[-1] = "Harpo".lower()
# print("Harpo".lower())
surprise[-1] = surprise[-1].lower()
print(surprise[-1])
surprise[-1] = surprise[-1][::-1]
print(surprise[-1])
surprise[-1] = surprise[-1].capitalize()
print(surprise)

# result
# mbpA1989:ex09 y0k0ta19$ python3 surpriseconv.py                                                                                                  +[ex08-14]
# harpo
# oprah
# ['Groucho', 'Chico', 'Oprah']
