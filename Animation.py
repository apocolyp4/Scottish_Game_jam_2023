import appgamekit as agk

class Animation:
    def __init__(self, sprite, start_pos, end_pos, speed, looped):
        self.sprite = sprite
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.speed = speed
        self.looped = looped

    def play(self):
        frame_no = agk.get_sprite_current_frame(self.sprite)
        if frame_no < self.start_pos or frame_no > self.end_pos:
            agk.play_sprite(self.sprite, self.speed, self.looped, self.start_pos, self.end_pos)


