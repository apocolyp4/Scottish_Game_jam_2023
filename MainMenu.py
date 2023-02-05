import appgamekit as agk
from Player import Player
from SearchTree import SearchTree
from VisualEditor_ImageButton import *
from calculations import *
from VisualEditor import VisualEditor
from Sprite import Sprite
from networking import Network
from Text import Text
from Planet import Planet
import os
import random

class MainMenu:
    def __init__(self, vis_editor):
        self.vis_editor = vis_editor
        self.vis_editor.open_scene(1) 

    def start(self):
        self.update()

    def update(self):
        while True:
            self.vis_editor.update()
            agk.sync()