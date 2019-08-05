print("4-1")
guess_me = 7


def compareTo7(val):
    th = 7
    if(val < th):
        print("too low")
    elif(val == th):
        print("just right")
    else:
        print("too high")


compareTo7(2)
compareTo7(9)
compareTo7(7)

print("\n4-2")
start = 1
while True:
    if(start < guess_me):
        print("too low")
    elif(start == guess_me):
        print("found it!")
    else:
        print("oops")
        break
    start += 1

print("\n4-3")
my_list = [3, 2, 1, 0]
for l in my_list:
    print(l)

print("\n4-4")
print([num for num in range(10) if num % 2 == 0])

print("\n4-5")
squares = {val: val * val for val in range(10)}
print(squares)

print("\n4-6")
print({val for val in range(10) if val % 2 == 1})

print("\n4-7")
got_numbers = ("Got %s" % num for num in range(10))
for val in got_numbers:
    print(val)

print("\n4-8")


def good():
    return ["Harry", "Ron", "Hermione"]


print(good())

print("\n4-9")


def get_odds():
    for number in range(1, 10, 2):
        yield number


gen = get_odds()

i = 1
for g in gen:
    if (i == 3):
        print(g)
        break
    i += 1

print("\n4-10")


def test(func):
    def new_func(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return new_func


@test
def hello_world(name):
    print("hello %s" % name)


hello_world("kaz")

print("\n4-11")


class OopsException(Exception):
    pass


try:
    raise OopsException()
except OopsException:
    print("Caught an oops")


print("\n4-12")
titles = ["Creature of Habit", "Crewel Fate"]
plots = ["A nun turns into a monster", "A haunted yarn shop"]
movies = dict(zip(titles, plots))

print(movies)
