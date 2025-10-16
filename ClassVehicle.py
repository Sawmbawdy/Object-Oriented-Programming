class Model:
    def __init__(self, maxspeed, milage):
        self.maxspeed = maxspeed
        self.milage = milage


ModelX = Model(240, 1000)

print(ModelX.maxspeed,'---', ModelX.milage)