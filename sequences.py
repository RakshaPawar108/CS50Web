name = "Raksha"             #sequence of characters

coordinates = (10.0, 20.0)          #python tuple, grouping values under a single name

names = ["Alice", "Raksha", "Bob", "Charlie"]          #python list allows us to store a bunch of different values under a single name

print(names[1])

#DS in Py is Set
s = set()           #A collection of items where no item shows up twice
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(2)
print(s)

#Python dictionaries DS in Py
#maps keys to values

ages = {"Raksha": 19, "Bob": 27, "Alice": 22}
ages["Charlie"] = 30
ages["Alice"] += 1
print(ages)
