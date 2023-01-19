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
        self.controls = Controls()


    def start_game(self):
        self.vis_editor.open_scene(0)              
        self.update()

    def update(self):
        while True:
            self.controls.update()
            self.vis_editor.update()

            #checks if user using controller 1 has pressed the a button on their control pad
            agk.print_value("Is Controller 1 connected: " + str(self.controls.game_pad_1.connected))
            agk.print_value("Button A state: " + str(self.controls.game_pad_1.A.state))
            agk.print_value("Button A being pressed: " + str(self.controls.game_pad_1.A.pressed))
            agk.print_value("Button A being released: " + str(self.controls.game_pad_1.A.released))

            agk.sync()