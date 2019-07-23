e2f = { "dog" : "chien", "cat" : "chat", "walrus" : "morse"}
f2e = dict()
for e, f in e2f.items():
    f2e[f] = e
print(f2e)

# result
# mbpA1989:ex12 y0k0ta19$ python3 e2fWithForLoop.py                                                                                                  [master]
# {'chien': 'dog', 'chat': 'cat', 'morse': 'walrus'}
