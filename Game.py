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
            agk.print_value(agk.timer())
            self.controls.update()
            self.vis_editor.update()
            agk.sync()