from random import randrange
class BME:
    def __init__(self):
        self.hp = 100
        self.level = 1
        self.attack = self.level * randrange(5,9)
        self.diningDollars = 500

class Chemical:
    def __init__(self):
        self.hp = 100
        self.level = 1
        self.attack = self.level * randrange(5,9)
        self.diningDollars = 500

class CompSci:
    def __init__(self):
        self.hp = 100
        self.level = 1
        self.attack = self.level * randrange(5,9)
        self.diningDollars = 500

class ECE:
    def __init__(self):
        self.hp = 100
        self.level = 1
        self.attack = self.level * randrange(5,9)
        self.diningDollars = 500

class Mechanical:
    def __init__(self):
        self.hp = 100
        self.level = 1
        self.attack = self.level * randrange(5,9)
        self.diningDollars = 500

class MiniBoss:
    def __init__(self):
        self.hp = 250
        self.attack = randrange(0,2)

class Klenke:
    def __init__(self):
        self.hp = 500
        self.attack = randrange(0,5)

class Motai:
    def __init__(self):
        self.hp = 500
        self.attack = randrange(0,5)

class Resler:
    def __init__(self):
        self.hp = 500
        self.attack = randrange(0,5)

class Ghosh:
    def __init__(self):
        self.hp = 500
        self.attack = randrange(0,5)