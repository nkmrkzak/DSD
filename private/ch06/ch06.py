print("6-1")


class Thing():
    pass


print(Thing)
example = Thing()
print(example)

print("6-2")


class Thing2():
    letter = "abc"


print(Thing2.letter)

print("6-3")


class Thing3():
    def __init__(self):
        self.letter = "xyz"


print(Thing3().letter)

print("6-4")


class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


obj = Element("Hydrogen", "H", 1)
print(f'{obj.name} {obj.symbol} {obj.number}')

print("6-5")
dic = {
    "name": "Hydrogen",
    "symbol": "H",
    "number": 1
}
obj2 = Element(**dic)
print(f'{obj2.name} {obj2.symbol} {obj2.number}')

print("6-6")


class Element2(Element):
    def dump(self):
        print(f'{self.name} {self.symbol} {self.number}')


hydrogen = Element2(**dic)
hydrogen.dump()

print("6-7")
print(hydrogen)


class Element3(Element):
    def __str__(self):
        return (f'{self.name} {self.symbol} {self.number}')


hydrogen = Element3(**dic)
print(hydrogen)

print("6-8")


class Element4():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number


obj3 = Element4(**dic)
print(obj3.name)

print("6-9")


class Bear():
    def eats(self):
        return "berries"


class Rabbit():
    def eats(self):
        return "clover"


class Octohorpe():
    def eats(self):
        return "campers"


print(Bear().eats())
print(Rabbit().eats())
print(Octohorpe().eats())

print("6-10")


class Laser():
    def does(self):
        return "disintegrate"


class Claw():
    def does(self):
        return "crush"


class SmartPhone():
    def does(self):
        return "ring"


class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return f"{self.laser.does()} {self.claw.does()} {self.smartphone.does()}"


robot = Robot()
print(robot.does())