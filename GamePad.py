import appgamekit as agk
from calculations import *
from Button import Button

class GamePad:
    def __init__(self, id):
        self.id = id
        self.name = ""
        self.connected = False
        self.enabled = False
        
        self.A = Button()
        self.B = Button()
        self.X = Button()
        self.Y = Button()
        self.start = Button()
        self.back = Button()

        self.left_stick_x = 0.0
        self.left_stick_y = 0.0
        self.left_force = 0.0
        self.left_angle = 0.0
        self.left_last_angle = 0.0
        self.left_trigger = 0.0
        self.left_button = Button()
        self.left_thumb_stick = Button()

        self.right_stick_x = 0.0
        self.right_stick_y = 0.0
        self.right_force = 0.0
        self.right_angle = 0.0
        self.right_last_angle = 0.0
        self.left_trigger = 0.0
        self.right_button = Button()
        self.right_thumb_stick = Button()

        self.setup()

    def setup(self): 
        if agk.get_raw_joystick_exists(self.id):           
            self.connected = True          
            self.name = agk.get_raw_joystick_name(self.id)


    def update_left_stick(self):
        self.left_stick_x = agk.get_raw_joystick_x(self.id)
        self.left_stick_y = agk.get_raw_joystick_y(self.id)
        self.left_trigger = agk.get_raw_joystick_z(self.id)

        if self.left_stick_x != 0 or self.left_stick_y != 0:
            self.left_force = get_distance(0.0, 0.0, self.left_stick_x, self.left_stick_y)
            self.left_angle = get_angle(0.0, 0.0, self.left_stick_x, self.left_stick_y)
        else:
            self.left_force = 0
            self.left_angle = 0

        

    def update_right_stick(self):
        self.right_stick_x = agk.get_raw_joystick_rx(self.id)
        self.right_stick_y = agk.get_raw_joystick_ry(self.id)
        self.right_trigger = agk.get_raw_joystick_rz(self.id)

        if self.right_stick_x != 0 or self.right_stick_y != 0:
            self.right_force = get_distance(0.0, 0.0, self.right_stick_x, self.right_stick_y)
            self.right_angle = get_angle(0.0, 0.0, self.right_stick_x, self.right_stick_y)
        else:
            self.right_force = 0
            self.right_angle = 0           
        

    def update_buttons(self):
        self.A.update(agk.get_raw_joystick_button_state(self.id, 1))
        self.B.update(agk.get_raw_joystick_button_state(self.id, 2))
        self.X.update(agk.get_raw_joystick_button_state(self.id, 3))
        self.Y.update(agk.get_raw_joystick_button_state(self.id, 4))
        self.start.update(agk.get_raw_joystick_button_state(self.id, 8))
        self.back.update(agk.get_raw_joystick_button_state(self.id, 7))
        self.left_thumb_stick.update(agk.get_raw_joystick_button_state(self.id, 9))
        self.left_button.update(agk.get_raw_joystick_button_state(self.id, 5))
        self.right_thumb_stick.update(agk.get_raw_joystick_button_state(self.id, 10))
        self.right_button.update(agk.get_raw_joystick_button_state(self.id, 6))       


    def update(self):
        if self.connected:
            self.update_buttons()
            self.update_left_stick()
            self.update_right_stick()
        else:
            self.setup()

