import appgamekit as agk
from Controls import Controls
from calculations import *

class GameControls:
    def __init__(self):      
        self.controls = Controls()
        self.mouse = self.controls.mouse
        self.gamepad = self.controls.game_pad_1

    def start(self, player):
        self.player = player
        self.gamepad.enabled = True
        self.mouse.enabled = True

    def update(self):
        self.controls.update()
        if self.gamepad.connected:
            self.move()

    def direction(self):
        angle = self.gamepad.left_angle
        if angle > 337.5 or angle < 22.5:
            self.player.direction = "north"
            self.player.angle = 0
        elif angle >= 22.5 and angle < 67.5:
            self.player.direction = "north east"
            self.player.angle = 45
        elif angle >= 67.5 and angle < 112.5:
            self.player.direction = "east"
            self.player.angle = 90
        elif angle >= 112.5 and angle < 157.5:
            self.player.direction = "south east"
            self.player.angle = 135
        elif angle >= 157.5 and angle < 202.5:
            self.player.direction = "south"
            self.player.angle = 180        
        elif angle >= 202.5 and angle < 247.5:
            self.player.direction = "south west"
            self.player.angle = 225
        elif angle >= 247.5 and angle < 292.5:
            self.player.direction = "west"
            self.player.angle = 270       
        elif angle >= 292.5 and angle < 337.5:
            self.player.direction = "north west"
            self.player.angle = 315       

    def move(self):
        if self.gamepad.left_force > 0.2:
            self.direction()
            speed = self.player.max_speed * self.gamepad.left_force
            if self.player.danger_zone:
                speed *= 0.8

            velocity = get_velocity(self.player.angle, speed)
            self.player.position.X += velocity[0]
            self.player.position.Y += velocity[1]
            self.player.status = "walking"
        else:
            self.player.status = "idle"


       # else:
           # self.player.status = "idle"