print("5-1")
import zoo

zoo.hours()

print("5-2")
import zoo as menagerie

menagerie.hours()

print("5-3")
from zoo import hours

hours()

print("5-4")
from zoo import hours as info

info()

print("5-5")
plain = {"a": 1, "b": 2, "c": 3}
print(plain)

print("5-6")
from collections import OrderedDict
fancy = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
print(fancy)

print("5-7")
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists["a"] = "something for a"
print(dict_of_lists["a"])
