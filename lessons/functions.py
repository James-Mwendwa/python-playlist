# use def to declare a function which means defined

# def greet(name, time):
#     print(f"Good {time} {name} hope you are fine")

# name = input('enter your name:')
# time = input('enter the time of day:')
# greet(name, time)


def area(radius):
    return 3.142 * (radius)**2

def vol(area, length):
    print(area * length)

radius = int(input('Enter the radius:'))   
length = int(input('Enter the length:'))
   
# area_calc = area(radius)
# vol(area_calc, length)

#pass functions into functions
vol(area(radius), length)



