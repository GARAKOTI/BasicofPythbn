arr = ['Pankaj','Rohit','Monty','lucky']
print(f"hello {arr[2]}, How are you?")

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])


cars = ['B&W','Honda','Tesla']
print("________________Before______________")
print(f"I would like to own a {cars[0]}")
print(f"I would like to own a {cars[1]}")
print(f"I would like to own a {cars[-1]}")

cars[0] = 'TataSafari'
cars[-2] = 'Mahindra Thar'
cars[-1]='MG Hector'

print("_________________After________________")

print(f"I would like to own a {cars[0]}")
print(f"I would like to own a {cars[1]}")
print(f"I would like to own a {cars[2]}")


cars.insert(2,'Bolero')

print(f"I would like to own a {cars[0]}")
print(f"I would like to own a {cars[1]}")
print(f"I would like to own a {cars[2]}")
print(f"I would like to own a {cars[3]}")


#print(cars)

#del cars[0]
print(cars)


poped_cars = cars.pop(0)
print(cars)
cars.remove('Mahindra Thar')
print(cars)

cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars.sort(reverse=False)
print(cars)

print(sorted(cars))
cars.sort(reverse=True)
print(cars)
print(len(cars))

location = ['U.S','Japan','Australia','Iceland','Britrain']
print(location)
print(sorted(location))
print(location)
location.reverse()
print(location)
location.reverse()
print(location)
location.sort()
print(location)
location.sort(reverse=True)
print(location)
print(len(location))

items = ['Moutans','Computer','Japneese']
items[0] = 'Flower'
print(items)
items.append('sun')
items.insert(0,'Rock')
del items[0]
items.remove('Computer')
items.reverse()
print(items)
print(len(items))