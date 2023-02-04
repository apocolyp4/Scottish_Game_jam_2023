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
import requests

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
        self.players["Player"].create("Bawbag")


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
        #print("receive_server_data")

        import json

        x = requests.get('https://91788rpir7.execute-api.eu-west-2.amazonaws.com/dev?player=dood')
        #print(x.status_code)

        outputData = json.loads(x.text)

        #print(outputData["body"]["Item"])
        self.players["Enemy"].name = outputData["body"]["Item"]["player_name"]["S"]
        self.players["Enemy"].angle = outputData["body"]["Item"]["character_rotation"]["N"]
        self.players["Enemy"].position.X = outputData["body"]["Item"]["characters_position_x"]["N"]
        self.players["Enemy"].position.Y = outputData["body"]["Item"]["characters_position_y"]["N"]
        self.players["Player"].flower_status = outputData["body"]["Item"]["flower_status"]["S"]


        #self.players["Enemy"].name
        #self.players["Enemy"].angle
        #self.players["Enemy"].position.X
        #self.players["Enemy"].position.Y   
        #self.players["Player"].flower_status


    def send_server_data(self):
        #print("send_server_data")

        import random
        xpos = random.randrange(20, 50, 3)
        ypos = random.randrange(20, 50, 3)
        rotation = random.randrange(20, 50, 3)

        self.players["Player"].name = "dave" 
        self.players["Player"].angle = rotation
        self.players["Player"].position.X = xpos
        self.players["Player"].position.Y = ypos  
        self.players["Enemy"].flower_status = "plucked"

        data = {
            "character_name": self.players["Player"].name,
            "flower_status": self.players["Enemy"].flower_status,
            "character_rotation": self.players["Player"].angle,
            "characters_position": { "x":self.players["Player"].position.X , "y":self.players["Player"].position.Y }
        }

        requests.post('https://c6xrszj8oa.execute-api.eu-west-2.amazonaws.com/dev', json=data)

        #self.players["Player"].name
        #self.players["Player"].angle
        #self.players["Player"].position.X
        #self.players["Player"].position.Y   
        #self.players["Enemy"].flower_status

    def update(self):
        while True:
            agk.print_value("This should be 60! " + str(agk.screen_fps()))
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