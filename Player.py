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
        self.direction = "South"
        self.status = "Idle"
        self.sprite = -1
        self.name = ""
        self.health = 100
        self.position = Vector2D(0, 0)
        self.angle = 0
        self.flower_status = "Safe"
        self.timer = Stopwatch()
        self.timer.start()

    def create(self, name):
        self.name = name
        image = agk.load_image("images/player/player.png")
        self.sprite = agk.create_sprite(image)

        self.create_animations()
        agk.play_sprite(self.sprite)


    def create_animations(self):
        agk.set_sprite_animation(self.sprite, 64, 128, 64)
        agk.set_sprite_frame(self.sprite, 1)

        for i in range(1, 15):
            image_name = "images/player/down-walk" + str(i)+ ".png"
            image = agk.load_image(image_name)
            agk.add_sprite_animation_frame(self.sprite, image)

        for i in range(1, 15):
            image_name = "images/player/up-walk" + str(i)+ ".png"
            image = agk.load_image(image_name)
            agk.add_sprite_animation_frame(self.sprite, image)


    def update(self):
        self.timer.update()



