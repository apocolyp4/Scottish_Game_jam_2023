import appgamekit as agk
from calculations import *
from CollisionDetection import *
from Sprite import Sprite
from copy import copy
from Vectors import Vector2D
from Stopwatch import Stopwatch
from SpriteAnimation import SpriteAnimation
from Object import Object
import random

class Player:
    def __init__(self):
        self.object = Object()
        self.see_enemy = False
        self.danger_zone = False
        self.name_text = -1
        self.garden_side = "right"
        self.max_speed = 5.0
        self.current_animation = ""
        self.animations = {}
        self.direction = "south"
        self.status = "idle"
        self.sprite = -1
        self.enemy = -1
        self.name = ""
        self.health = 100
        self.position = Vector2D(0, 0)
        self.last_position = Vector2D(0, 0)
        self.hit_box = -1
        self.angle = 0
        self.flower_status = "Safe"
        self.timer = Stopwatch()
        self.timer.start()
        self.debug_ray_cast = -1

    def spawn(self):
        self.status = "idle"
        if self.garden_side == "left":
            self.object.position.X = 60
            self.object.position.Y = agk.get_virtual_height() / 2
            self.direction = "east"
        else:
            self.object.position.X = agk.get_virtual_width() - 100
            self.object.position.Y = agk.get_virtual_height() / 2 
            self.direction = "west"         

    def create(self, name):
        self.name = name

        self.create_name_text()
        self.create_sprite()
        self.create_animations()
        self.set_animation(self.get_animation_name())
        width = agk.get_sprite_width(self.object.sprite) / 1.5
        height = agk.get_sprite_height(self.object.sprite) / 1.5
        agk.set_sprite_size(self.object.sprite, width, height)
        agk.set_sprite_shape(self.object.sprite, 1)

    def create_sprite(self):
        image = agk.load_image("images/player/player.png")
        self.object.sprite = agk.create_sprite(image)

        #image = agk.load_image("block.png")
        #self.debug_ray_cast = agk.create_sprite(image)


    def create_name_text(self):
        self.name_text = agk.create_text("")
        agk.set_text_depth(self.name_text, 5)
        agk.set_text_size(self.name_text, 25)
        agk.set_text_alignment(self.name_text, 1)

    def create_animations(self):
        agk.set_sprite_animation(self.object.sprite, 64, 128, 64)
        agk.set_sprite_frame(self.object.sprite, 1)

        for i in range(1, 15):
            image_name = "images/player/down-walk" + str(i)+ ".png"
            image = agk.load_image(image_name)
            agk.add_sprite_animation_frame(self.object.sprite, image)

        for i in range(1, 15):
            image_name = "images/player/up-walk" + str(i)+ ".png"
            image = agk.load_image(image_name)
            agk.add_sprite_animation_frame(self.object.sprite, image)

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
            agk.play_sprite(self.object.sprite, fps, looped, start_frame, end_frame)
       # else:
           # print("not found animation " + animation_name)
           # print(self.animations.keys())

    def update_angle(self):
        if self.direction == "north":
            self.object.angle = 0
        elif self.direction == "north east":
            self.object.angle = 45
        elif self.direction == "east":
            self.object.angle = 90
        elif self.direction == "south east":
            self.object.angle = 135
        elif self.direction == "south":
            self.object.angle = 180
        elif self.direction == "south west":
            self.object.angle = 225
        elif self.direction == "west":
            self.object.angle = 270
        elif self.direction == "north west":
            self.object.angle = 315


    def get_animation_name(self):
        animation = self.status + " " + self.direction
        return animation

    def update_position(self):

        if self.object.position.Y < 10:
            self.object.position.Y = 10

        if self.object.position.Y > 970:
            self.object.position.Y = 970  

        if self.object.position.X < 40:
            self.object.position.X = 40

        if self.object.position.X > 1840:
            self.object.position.X = 1840

        self.object.update_position()

    def update_animations(self):
        if self.get_animation_name() != self.current_animation:
            self.set_animation(self.get_animation_name())

    def update_name_text(self):
        agk.set_text_string(self.name_text, self.name)
        x = self.object.position.X + (agk.get_sprite_width(self.object.sprite) / 2)
        y = self.object.position.Y - 20
        agk.set_text_position(self.name_text, x, y)

    def update_ray_cast(self):
        self.see_enemy = False

        x = self.object.position.X + (agk.get_sprite_width(self.object.sprite) / 2)
        y = self.object.position.Y + (agk.get_sprite_height(self.object.sprite) / 2)


        sweep_range = 120
        angle = self.object.angle - (sweep_range / 2)
        sweep_step = 5
        sweep_steps = int(sweep_range / sweep_step)

        for i in range(0, sweep_steps):
            velocity = get_velocity(angle, 500)
            x2 = x + velocity[0]
            y2 = y + velocity[1]

            #agk.set_sprite_position(self.debug_ray_cast, x2, y2)         
            angle += sweep_step

            if agk.sprite_ray_cast( x, y, x2, y2 ) == 1:        
                if agk.get_ray_cast_sprite_id() == self.enemy.object.sprite:
                    self.see_enemy = True
                    break

        alpha = agk.get_sprite_color_alpha(self.enemy.object.sprite)
        alpha_step = 10

        if self.see_enemy:
            alpha += alpha_step
            if alpha > 255:
                alpha = 255

        else:
            alpha -= alpha_step
            if alpha < 0:
                alpha = 0

        agk.set_sprite_color_alpha(self.enemy.object.sprite, alpha)   
        agk.set_text_color_alpha(self.enemy.name_text, alpha)        

    def check_in_danger_zone(self):
        self.danger_zone = False   
        x = self.position.X + (agk.get_sprite_width(self.object.sprite) / 2)

        if self.garden_side == "right":
            if x < agk.get_virtual_width() / 2:
                self.danger_zone = True

        if self.garden_side == "left":
            if x >= agk.get_virtual_width() / 2:
                self.danger_zone = True

    def check_state(self):
        if self.status == "caught":
            self.spawn()

    def update(self):
        self.check_state()
        self.timer.update()
        self.update_angle()
        self.update_position()
        self.check_in_danger_zone()
        self.update_ray_cast()
        self.update_name_text()
        self.update_animations()
        
        



