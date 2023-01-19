import appgamekit as agk
from calculations import *

class GamePad:
    def __init__(self):
        self.id = -1
        self.name = ""

        for i in range(1, 8):
            if agk.get_raw_joystick_exists(i):
                self.id = i
                break

        if self.id > 0:
            self.name = agk.get_raw_joystick_name(self.id)

        self.left_stick_x = 0.0
        self.left_stick_y = 0.0
        self.left_force = 0.0
        self.left_angle = 0.0
        self.left_last_angle = 0.0
        self.left_trigger = 0.0

        self.right_stick_x = 0.0
        self.right_stick_y = 0.0
        self.right_force = 0.0
        self.right_angle = 0.0
        self.right_last_angle = 0.0
        self.left_trigger = 0.0

    def update_left_stick(self):
        self.left_stick_x = agk.get_raw_joystick_x(self.id)
        self.left_stick_y = agk.get_raw_joystick_y(self.id)
        self.left_force = get_distance(0.0, 0.0, self.left_stick_x, self.left_stick_y)
        self.left_angle = get_angle(0.0, 0.0, self.left_stick_x, self.left_stick_y)
        self.left_trigger = agk.get_raw_joystick_z(self.id)

    def update_right_stick(self):
        self.right_stick_x = agk.get_raw_joystick_rx(self.id)
        self.right_stick_y = agk.get_raw_joystick_ry(self.id)
        self.right_force = get_distance(0.0, 0.0, self.right_stick_x, self.right_stick_y)
        self.right_angle = get_angle(0.0, 0.0, self.right_stick_x, self.right_stick_y)
        self.right_trigger = agk.get_raw_joystick_rz(self.id)

    def update(self):
        self.update_left_stick()
        self.update_right_stick()
