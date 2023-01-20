import appgamekit as agk
from Button import Button

class Mouse:
    def __init__(self):
        self.enabled = False
        self.X = 0.0
        self.Y = 0.0
        self.left = Button()
        self.middle= Button()
        self.right = Button()
        self.wheel = 0.0
        self.wheel_delta = 0.0
    
    def update(self):
        self.X = agk.get_pointer_x()
        self.Y = agk.get_pointer_y()
        self.left.update(agk.get_raw_mouse_left_state())
        self.middle.update(agk.get_raw_mouse_middle_state())
        self.right.update(agk.get_raw_mouse_right_state())
        self.wheel = agk.get_raw_mouse_wheel()
        self.wheel_delta = agk.get_raw_mouse_wheel_delta()
