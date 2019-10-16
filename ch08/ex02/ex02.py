test1 = 'This is a test of the emergency text system'

with open('test.txt', 'rt') as fp:
    test2 = fp.read()

print(test1 == test2)
