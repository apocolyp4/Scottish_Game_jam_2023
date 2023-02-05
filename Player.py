import appgamekit as agk
from calculations import *
from CollisionDetection import *
from Sprite import Sprite
from copy import copy
from Vectors import Vector2D
from Stopwatch import Stopwatch
from SpriteAnimation import SpriteAnimation
import random

class Player:
    def __init__(self):
        self.max_speed = 5.0
        self.current_animation = ""
        self.animations = {}
        self.direction = "south"
        self.status = "idle"
        self.sprite = -1
        self.name = ""
        self.health = 100
        self.position = Vector2D(100, 200)
        self.angle = 0
        self.flower_status = "Safe"
        self.timer = Stopwatch()
        self.timer.start()

    def create(self, name):
        self.name = name
        image = agk.load_image("images/player/player.png")
        self.sprite = agk.create_sprite(image)

        self.create_animations()
        self.set_animation(self.get_animation_name())


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

        self.animations["idle south"] = SpriteAnimation(1, 4, 5, 1)
        self.animations["idle north"] = SpriteAnimation(5, 8, 5, 1)
        self.animations["idle south east"] = SpriteAnimation(9, 12, 5, 1)
        self.animations["idle south west"] = SpriteAnimation(13, 16, 5, 1)
        self.animations["idle east"] = SpriteAnimation(17, 20, 5, 1)
        self.animations["idle west"] = SpriteAnimation(21, 24, 5, 1)
        self.animations["idle north east"] = SpriteAnimation(25, 28, 5, 1)
        self.animations["idle north west"] = SpriteAnimation(29, 32, 5, 1)

        self.animations["walking south"] = SpriteAnimation(65, 78, 10, 1)
        self.animations["walking north"] = SpriteAnimation(79, 92, 10, 1)
        self.animations["walking south west"] = SpriteAnimation(45, 48, 5, 1)
        self.animations["walking south east"] = SpriteAnimation(41, 44, 5, 1)
        self.animations["walking east"] = SpriteAnimation(49, 52, 5, 1)
        self.animations["walking west"] = SpriteAnimation(53, 56, 5, 1)
        self.animations["walking north east"] = SpriteAnimation(57, 60, 5, 1)
        self.animations["walking north west"] = SpriteAnimation(61, 64, 5, 1)


    def set_animation(self, animation_name):

        if animation_name in self.animations:
            start_frame = self.animations[animation_name].start_frame
            end_frame = self.animations[animation_name].end_frame
            fps = self.animations[animation_name].fps
            looped = self.animations[animation_name].looped
            self.current_animation = animation_name      
            agk.play_sprite(self.sprite, fps, looped, start_frame, end_frame)
       # else:
           # print("not found animation " + animation_name)
           # print(self.animations.keys())

    def get_animation_name(self):
        animation = self.status + " " + self.direction
        return animation

    def update_position(self):
        agk.set_sprite_position(self.sprite, self.position.X, self.position.Y)
        #agk.set_sprite_position(self.sprite, 200, 300)

    def update_animations(self):
        if self.get_animation_name() != self.current_animation:
            self.set_animation(self.get_animation_name())

    def update(self):
        self.timer.update()
        self.update_position()
        self.update_animations()
        



