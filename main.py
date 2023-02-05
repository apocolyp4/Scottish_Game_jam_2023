import appgamekit as agk
from SearchTree import SearchTree
from VisualEditor_ImageButton import *
from VisualEditor import VisualEditor
from Sprite import Sprite
from networking import Network
from Text import Text
from Game import Game
from MainMenu import MainMenu
import json

with agk.Application():
    #setup the editor
    agk.set_print_color(255, 255, 255)

    vis_editor = VisualEditor(0)
    main_menu = MainMenu(vis_editor)
    main_menu.start()

    game = Game(vis_editor, main_menu.type, main_menu.name)
    game.start_game()
