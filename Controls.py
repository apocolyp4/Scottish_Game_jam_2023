import appgamekit as agk
from GamePad import GamePad

class Controls:
    def __init__(self):
        self.game_pad = GamePad()

    def update(self):
        self.game_pad.update()

