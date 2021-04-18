from JUNIOR.AI.car import Car

car1 = Car("honda", 'civic', 2012)
car1.fill_tank()
car1.drive()
print(car1.get_fuel())

myCars = [Car("toyota", "corolla", 2013) for x in range(0, 5)]
for x in range(0, len(myCars)):
    myCars[x].print()
for Car in myCars:
    Car.print()

# print("""10**3
# i like apples
# no u
# 7*3""")

string = "happy"
print(string[2:3])
print(string.__contains__("pp"))
string = string.split("a")
print(string)


fuelLevels = [6,4,1,6,8,3,9,9,22,4]
fuelLevels.sort()
fuelLevels.reverse()
print(fuelLevels)
fuelLevels.insert(4,7)
print(fuelLevels.index(7))
print(fuelLevels[7])
print(fuelLevels)
fuelLevels.remove(7)
del fuelLevels[3]
print(fuelLevels)
fuelLevels.append(8)
print(fuelLevels)
numbers = fuelLevels

dictionary = {}
dictionary['chicken']=4.30 #or dictionary = {"chicken": 4.30}
dictionary[7]='happy'
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
del dictionary[7]
print (dictionary)

# Same as {"a", "b","c"}
normal_set = {"a", "b", "c"}
normal_set.add("d")
print("Normal Set")
print(normal_set)
frozen_set = frozenset(["e", "f", "g"])
print("Frozen Set")
print(frozen_set)

string4 = int(input("what is the day?"))
string4+=7
print(string4)

string6 = input("list of #").split(" ")
print('%s is greater than %s' %(15, 1))

strings = "dvfbsngfdvcvfbgkevin"
print(strings[-5:])
