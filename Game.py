import appgamekit as agk
from Player import Player
from SearchTree import SearchTree
from VisualEditor_ImageButton import *
from calculations import *
from VisualEditor import VisualEditor
from Sprite import Sprite
from networking import Network
from Text import Text
import os
import random
from Controls import Controls

class Game:
    def __init__(self, vis_editor):
        self.type = ""
        self.vis_editor = vis_editor       
        self.init_controls()

    def init_controls(self):
        self.controls = Controls()
        self.mouse = self.controls.mouse
        self.gamepad = self.controls.game_pad_1

    def start_controls(self):
        self.gamepad.enabled = True
        self.mouse.enabled = True

    def start_game(self):
        self.start_controls()
        self.vis_editor.open_scene(0)     
        self.update()

    def update(self):
        while True:
            self.controls.update()
            self.vis_editor.update()

            #checks if user using controller 1 has pressed the a button on their control pad
            agk.print_value("Is Controller 1 connected: " + str(self.gamepad.connected))
            agk.print_value("Is Controller 1 enabled: " + str(self.gamepad.enabled))
            agk.print_value("Button A state: " + str(self.gamepad.A.state))
            agk.print_value("Button A being pressed: " + str(self.gamepad.A.pressed))
            agk.print_value("Button A being released: " + str(self.gamepad.A.released))

            agk.print_value("Mouse position " + str(self.mouse.X) + " " + str(self.mouse.Y))
            agk.print_value("Mouse left button state " + str(self.mouse.left.state) + " " + str(self.mouse.left.pressed)+ " " + str(self.mouse.left.released))
            agk.print_value("Mouse middle button state " + str(self.mouse.middle.state) + " " + str(self.mouse.middle.pressed)+ " " + str(self.mouse.middle.released))
            agk.print_value("Mouse right button state " + str(self.mouse.right.state) + " " + str(self.mouse.right.pressed)+ " " + str(self.mouse.right.released))
            agk.print_value("Mouse wheel " + str(self.mouse.wheel) + " wheel_delta " + str(self.mouse.wheel_delta))

            agk.sync()