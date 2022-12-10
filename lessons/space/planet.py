class Planet:
    shape = "round"  ## class level attribute

    ## create attributes
    def __init__(self, name, radius, gravity, system):
        ##instant attributes
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f" {self.name} is orbiting around {self.system} "

    @classmethod  ## has access to class level attributes
    def commons(cls):
        return f"All planets are {cls.shape} due to gravity "

    @staticmethod  ## only take the parameters passed
    def spin(speed="20000 m/s"):
        return f"the planet spins at {speed} "


## new instance of the class
