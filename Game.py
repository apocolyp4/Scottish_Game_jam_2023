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
from GameControls import GameControls
from Vectors import Vector2D
from Stopwatch import Stopwatch
import requests
from networking import Network
import json
from CollisionDetection import *
from Object import Object

class Game:
    def __init__(self, vis_editor, type, user_name):
        agk.set_print_color(255, 255, 255)
        self.network_type = type
        self.user_name = user_name
        self.vis_editor = vis_editor     
        self.vis_editor.open_scene(0)   
        self.init_controls()
        self.init_players()
        self.init_network()
        self.init_level()

    def init_level(self):
        self.enemy_garden = agk.create_sprite(agk.load_image("ground/zone.png"))
        agk.set_sprite_depth(self.enemy_garden, 5001)
        agk.set_sprite_size(self.enemy_garden, agk.get_virtual_width() / 2, agk.get_virtual_height() + 200)
        agk.set_sprite_color(self.enemy_garden, 0, 50, 0, 100)
        self.ground_sprite = agk.create_sprite(agk.load_image("ground/grass1.png"))
        agk.set_sprite_depth(self.ground_sprite, 5002)
        agk.set_sprite_position(self.ground_sprite, 0, 0)
        self.init_hedges()
        
        self.network_id = 0
        self.game_network = None
        self.host_ip = '77.103.255.35' #agk.get_edit_box_text(ip_editbox)
        self.host_port = '5689' #agk.get_edit_box_text(port_editbox)    
        self.status = ''


    def init_hedges(self):
        self.level_hedges = []

        self.level_sprites = self.vis_editor.get_scene_sprites(0)

        for sprite in self.level_sprites:
            image_no = agk.get_sprite_image_id(sprite)
            if agk.get_image_exists(image_no):
                image_name = agk.get_image_filename(image_no).split("/")
                image_name = image_name[len(image_name) - 1]
                if image_name == "Trees3.png":
                    object = Object()
                    object.init_from_sprite(sprite)
                    self.level_hedges.append(object)
    


    def connect_players(self):
        print("GetDeviceIP() " + agk.get_device_ip())
        self.game_network = Network("Game Deally", self.host_ip, self.host_port)

        if self.status == 'server':
            #host_ip_text = self.vis_editor.get_entity_id("Address", 4)
            self.host_ip = "77.103.255.35"
            self.host_port = "5689"
            self.network_id = self.game_network.host()
        else:
            #host_ip_text = self.vis_editor.get_entity_id("Address", 3)
            self.network_id = self.game_network.client()


        host_ip_string = self.host_ip + ":" + self.host_port
        #agk.set_text_string(host_ip_text, host_ip_string)

        while True:
            if agk.get_raw_key_pressed(27):                
                self.start_main_menu()

            #The user detail below is to be replaced with the data being passed
            user_detail = {"sprite_name": self.status, "sprite_x": 600, "sprite_y": 500, "sprite_z": 0, "health": 123}

            #below checks for a connection if none is present then one is created, this will continually 
            #loop creating new connections and holding awaititing a connection from host or client

            if agk.is_network_active(self.network_id) != 0:
                id = agk.get_network_first_client(self.network_id )
                #Get players online
                while id != 0:
                    id = agk.get_network_next_client(self.network_id )
                self.send_server_data()
                retreived_message = self.receive_server_data()
                print("Incoming - " + str(retreived_message))
            else:
                print("still waiting for that dildo")
                if self.status == 'server':
                    self.network_id  = self.game_network.host()  
                else:  
                    self.network_id = self.game_network.client()

            self.vis_editor.update()
            self.update()
            agk.sync()

    def connect_to_host(self):
        self.connect_players()
        self.vis_editor.update()
        agk.sync()

    def init_network(self):
        self.network_clock = Stopwatch()
        self.network_clock.repeat_duration = 1.0 / 15
         
    def init_players(self):
        self.players = {}
        self.players["Player"] = Player()
        self.players["Player"].create(self.user_name)

        if self.network_type == "host":
            self.players["Player"].garden_side = "left"
            
        self.players["Player"].spawn()
        self.players["Enemy"] = Player()
        self.players["Enemy"].create("Fannybaws")
        self.players["Enemy"].spawn()

        self.players["Player"].enemy = self.players["Enemy"]
        self.players["Enemy"].enemy = self.players["Player"]


    def init_controls(self):
        self.controls = GameControls()


    def start_controls(self):
        self.controls.start(self.players["Player"])

    def start_game(self):
        self.start_controls()

        if self.network_type == "host":
            pass
            #agk.message("im a host")
            #self.connect_players()
        else:
            pass
            #agk.message("im a client")                 
            #self.connect_to_host()

        self.update()

    def receive_server_data(self):
        retreived_message = self.game_network.retreive_message(self.network_id )
        print("Incoming - " + str(retreived_message))

        try:
            outputData = json.loads(retreived_message)
            self.players["Enemy"].name = outputData["character_name"]
            self.players["Enemy"].direction = outputData["character_rotation"]
            self.players["Enemy"].position.X = outputData["characters_position"]["x"]
            self.players["Enemy"].position.Y = outputData["characters_position"]["y"]
            self.players["Player"].flower_status = outputData["flower_status"]
        except Exception as e:
            print(e)

    def send_server_data(self):
        #print("send_server_data")

        # import random
        # xpos = random.randrange(20, 50, 3)
        # ypos = random.randrange(20, 50, 3)
        # rotation = random.randrange(20, 50, 3)

        

        # self.players["Player"].name = "dave" 
        # self.players["Player"].angle = rotation
        # self.players["Player"].position.X = xpos
        # self.players["Player"].position.Y = ypos  
        # self.players["Enemy"].flower_status = "plucked"

        data = {
            "character_name": self.players["Player"].name,
            "flower_status": self.players["Enemy"].flower_status,
            "character_rotation": self.players["Player"].direction,
            "characters_position": { "x":self.players["Player"].position.X , "y":self.players["Player"].position.Y }
        }

        self.game_network.send_message(self.network_id , data)
        # self.players["Player"].name
        # self.players["Player"].angle
        # self.players["Player"].position.X
        # self.players["Player"].position.Y   
        # self.players["Enemy"].flower_status

    def update_collisions(self):
        collision = check_tile_collisions(self.players["Player"].object, self.level_hedges, "Sprite")
        if collision:
            self.players["Player"].object.position = where_can_i_get_to(self.players["Player"].object, self.level_hedges)


    def update_level(self):
        if self.players["Player"].garden_side == "left":
            agk.set_sprite_position(self.enemy_garden, agk.get_virtual_width() / 2, 0)
        else:
            agk.set_sprite_position(self.enemy_garden, 0, 0)

        self.update_collisions()


    def update_players(self):
        self.players["Player"].update()
        self.players["Enemy"].update()

        agk.set_sprite_color_alpha(self.players["Player"].object.sprite, 255)
        agk.set_text_color_alpha(self.players["Player"].name_text, 255)

        #agk.set_sprite_color_alpha(self.players["Enemy"].sprite, 255)
        #agk.set_text_color_alpha(self.players["Enemy"].name_text, 255)

        #check_wall_collision(self.players["Player"].sprite, self.level_hedges)
        #agk.print_value("hedges touched " + str(check_wall_collision(self.players["Player"].sprite, self.level_hedges)))


        if self.players["Player"].danger_zone:
            if agk.get_sprite_collision(self.players["Player"].object.sprite, self.players["Enemy"].object.sprite):
                 self.players["Player"].status = "caught"


        #self.test_network()



    def update(self):
        while True:
            self.network_clock.update()
            access_network = self.network_clock.check_pulse()

         #   if access_network:
               # self.receive_server_data()

            self.controls.update()
            self.update_players()
            self.update_level()

         #   if access_network:
          #      self.send_server_data()

            self.vis_editor.update()



            agk.sync()