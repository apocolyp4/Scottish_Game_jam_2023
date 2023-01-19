import appgamekit as agk
from GamePad import GamePad

class Controls:
    def __init__(self):
        agk.complete_raw_joystick_detection()
        self.game_pad_1 = GamePad(1)
        self.game_pad_2 = GamePad(2)
        self.game_pad_3 = GamePad(3)
        self.game_pad_4 = GamePad(4)

    def update(self):
        self.game_pad_1.update()
        self.game_pad_2.update()
        self.game_pad_3.update()
        self.game_pad_4.update()

