from space.planet import Planet
from space.calc import planet_mass, planet_vol

pluto = Planet("Pluto", 400000, 3.2, "Pluto System")


pluto_mass = planet_mass(pluto.gravity, pluto.radius)
pluto_vol = planet_vol(pluto.radius)

print(f"{pluto.name} has a mass o f{pluto_mass} and a volume of {pluto_vol}")
