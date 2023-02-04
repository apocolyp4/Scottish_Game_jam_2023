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
from Vectors import Vector2D
from Stopwatch import Stopwatch

class Game:
    def __init__(self, vis_editor):
        self.type = ""
        self.vis_editor = vis_editor       
        self.init_controls()
        self.init_players()
        self.init_network()

    def init_network(self):
        self.network_clock = Stopwatch()
        self.network_clock.repeat_duration = 1.0 / 15
         


    def init_players(self):
        self.players = {}
        self.players["Player"] = Player()
        self.players["Player"].name = "Player " + str(int(random.uniform(1, 200)))
        self.players["Enemy"] = Player()

    def test_network(self):
        if self.players["Player"].timer.time > 1:
            self.players["Player"].timer.reset()
            self.players["Player"].position.X = random.uniform(20, 600)
            self.players["Player"].position.Y = random.uniform(20, 600)
            self.players["Player"].angle = random.uniform(0, 360)


        agk.print_value("Name " + self.players["Player"].name)
        agk.print_value("Angle " + str(int(self.players["Player"].angle)))
        agk.print_value("Flower status " + self.players["Player"].flower_status)
        agk.print_value("Position " + str(int(self.players["Player"].position.X)) + " " + str(int(self.players["Player"].position.Y)))
     
        agk.print_value("Name " + self.players["Enemy"].name)
        agk.print_value("Angle " + str(int(self.players["Enemy"].angle)))
        agk.print_value("Flower status " + self.players["Enemy"].flower_status)
        agk.print_value("Position " + str(int(self.players["Enemy"].position.X)) + " " + str(int(self.players["Enemy"].position.Y)))

    def update_players(self):
        self.players["Player"].update()
        self.players["Enemy"].update()
        self.test_network()


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

    def receive_server_data(self):
        print("receive_server_data")
        #self.players["Enemy"].name
        #self.players["Enemy"].angle
        #self.players["Enemy"].position.X
        #self.players["Enemy"].position.Y   
        #self.players["Player"].flower_status


    def send_server_data(self):
        print("send_server_data")
        #self.players["Player"].name
        #self.players["Player"].angle
        #self.players["Player"].position.X
        #self.players["Player"].position.Y   
        #self.players["Enemy"].flower_status

    def update(self):
        while True:
            self.network_clock.update()
            access_network = self.network_clock.check_pulse()

            if access_network:
                self.receive_server_data()

            self.controls.update()
            self.update_players()

            if access_network:
                self.send_server_data()

            self.vis_editor.update()



            agk.sync()