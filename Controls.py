import appgamekit as agk
from GamePad import GamePad
from Mouse import Mouse

class Controls:
    def __init__(self):        
        self.init_game_pads()
        self.mouse = Mouse()


    def init_game_pads(self):
        agk.complete_raw_joystick_detection()
        self.game_pad_1 = GamePad(1)
        self.game_pad_2 = GamePad(2)
        self.game_pad_3 = GamePad(3)
        self.game_pad_4 = GamePad(4)


    def update(self):
        self.update_game_pads()
        if self.mouse.enabled:
            self.mouse.update()

    def update_game_pads(self):
        if self.game_pad_1.enabled:
            self.game_pad_1.update()

        if self.game_pad_2.enabled:
            self.game_pad_2.update()
      
        if self.game_pad_3.enabled:
            self.game_pad_3.update()

        if self.game_pad_4.enabled:
            self.game_pad_4.update()
