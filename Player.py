import appgamekit as agk
from calculations import *
from CollisionDetection import *
from Sprite import Sprite
from copy import copy
from Vectors import Vector2D
from Stopwatch import Stopwatch
import random

class Player:
    def __init__(self):
        self.name = ""
        self.health = 100
        self.position = Vector2D(0, 0)
        self.angle = 0
        self.flower_status = "Safe"
        self.timer = Stopwatch()
        self.timer.start()

    def update(self):
        self.timer.update()



