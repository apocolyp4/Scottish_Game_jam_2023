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
        self.name = ""
        self.type = ""

    def start(self):
        self.update()

    def update(self):
        host_button = self.vis_editor.get_entity_id("IB:Host", 1)
        client_button = self.vis_editor.get_entity_id("IB:Client", 1)
        edit_box = self.vis_editor.get_entity_id("edit box 0", 1)
        run_main_menu = True

        while run_main_menu:
            if host_button.pressed:
                self.type = "host"
                if len(agk.get_edit_box_text(edit_box)) > 1:
                    run_main_menu = False
                    self.name = agk.get_edit_box_text(edit_box)
                else:
                    agk.message("Please enter a name")

            elif client_button.pressed:
                self.type  = 'client'
                if len(agk.get_edit_box_text(edit_box)) > 1:
                    run_main_menu = False
                    self.name = agk.get_edit_box_text(edit_box)
                else:
                    agk.message("Please enter a name")
                    
            self.vis_editor.update()
            agk.sync()