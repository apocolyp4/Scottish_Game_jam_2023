import appgamekit as agk
from calculations import *
from CollisionDetection import *
from Sprite import Sprite
from copy import copy
from Planet import Planet

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.planet = None

    def set_planet(self, player):
        pass

    def update(self, controls):
        pass



