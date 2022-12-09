class Planet:
    ## create attributes
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f" {self.name} is orbiting around {self.system} "


## new instance of the class
hoth = Planet("Saturn", 1620000, 7.3, "Saturn System")
print(f"Name is {hoth.name} and its gravity is {hoth.gravity} ")

print(hoth.orbit())


pluto = Planet("Pluto", 400000, 3.2, "Pluto System")

print(f"Name: {pluto.name}")
