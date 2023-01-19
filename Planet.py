import appgamekit as agk
from calculations import *
from CollisionDetection import *
from Sprite import Sprite

class Planet:
    def __init__(self, name):
        self.name = name
        self.image_name = "NULL"
        self.health = 100
        self.gravity = 50
        self.sprite = None
        self.angle = 0
        self.x = 0
        self.y = 0
        self.image_id = -1
        self.sprite_id = -1
        self.status = "Alive"
        self.vel_x = 0
        self.vel_y = 0
        self.width = 0
        self.height = 0
        self.planet_no = 1
        self.age = 0

    def update(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.angle = self.angle
        self.age += agk.get_frame_time()

        self.sprite.update()