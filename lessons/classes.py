class Planet:
    ## create attributes
    def __init__(self):
        self.name = 'Saturn'
        self.radius = 1620000
        self.gravity = 7.3
        self.system = 'Saturn System'

    def orbit(self):
        return f' {self.name} is orbiting around {self.system} '    

## new instance of the class
hoth = Planet()
print(f'Name is {hoth.name} and its gravity is {hoth.gravity} ')

print(hoth.orbit())