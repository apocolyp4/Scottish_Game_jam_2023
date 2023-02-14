import appgamekit as agk
from calculations import *
from CollisionDetection import *
from Sprite import Sprite
from copy import copy
from Vectors import Vector2D
from Stopwatch import Stopwatch
from SpriteAnimation import SpriteAnimation
import random

class Object:
    def __init__(self):
        self.current_animation = ""
        self.type = ""
        self.animations = {}
        self.sprite = -1
        self.health = 100
        self.position = Vector2D(0, 0)
        self.last_position = Vector2D(0, 0)
        self.angle = 0
        self.width = 0
        self.height = 0
        self.depth = 0

    def init_from_sprite(self, sprite):
        self.sprite = sprite
        self.angle = agk.get_sprite_angle(self.sprite)
        self.position = Vector2D(agk.get_sprite_x(self.sprite), agk.get_sprite_y(self.sprite))
        self.width = agk.get_sprite_width(self.sprite)
        self.height = agk.get_sprite_height(self.sprite)
        self.depth = agk.get_sprite_depth(self.sprite)

 
    def update_position(self):
        agk.set_sprite_position(self.sprite, self.position.X, self.position.Y)
        
        



