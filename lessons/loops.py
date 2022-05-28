        # FOR LOOPS
 # To pass through a list of items

cities = ['Nairobi', 'NewYork', 'Tokyo', 'London']

for city in cities:
     print(city)


 # pass through a portion of the list from index 1 to 3(exclusive)
for city in cities[1:3]:
    print(city)


  # break keywork used to break out of a loop
for city in cities:
    if city == 'Tokyo':
        print(f'{city} is a beautiful city')
        break
    else:
        print(city)



         # WHILE LOOPS
 # used to cycle through a code until a certain condition is true
 # Keyword continue to exclude zero while running

age = 20
num = 0

while num < age:
    if num == 0:
        num += 1
    if num % 2 == 0:
      print(num)
    if num > 10:
        break
    num += 1
