import appgamekit as agk
from SearchTree import SearchTree
from VisualEditor_ImageButton import *
from VisualEditor import VisualEditor
from Sprite import Sprite
from networking import Network
from Text import Text
from Game import Game

import json

with agk.Application():
    #setup the editor
    agk.set_print_color(255, 255, 255)

    vis_editor = VisualEditor(0)
    game = Game(vis_editor)

    game.start_game()
