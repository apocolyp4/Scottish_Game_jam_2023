import appgamekit as agk
from Sprite import *

class SpeechBubble:
    def __init__(self):
        self.image = agk.load_image("Images/speech_bubble.png")
        agk.set_image_mag_filter(self.image, 0)
        agk.set_image_min_filter(self.image, 0)
        self.sprite = Sprite(self.image, 100, 100, 105, 73, 0, 10, 1, 1)

        self.text = agk.create_text("")
        agk.set_text_color_alpha(self.text, 0)
        agk.set_text_size(self.text, 24)
        agk.set_text_color(self.text, 0, 0, 0, 255)
        agk.set_text_alignment(self.text, 1)

        self.alpha = 0

        self.talk_timer_start = agk.timer()
        self.talk_timer_length = 3

    def update(self, sprite):
        x = sprite.x + 32
        y = sprite.y - 50

        self.sprite.position(x, y)
        text_offset_y = y - (agk.get_text_size(self.text) / 2)
        agk.set_text_position(self.text, x, text_offset_y)

        agk.set_text_color_alpha(self.text, self.alpha)
        agk.set_sprite_color_alpha(self.sprite.id, self.alpha)

        if agk.timer() - self.talk_timer_start > self.talk_timer_length:
            self.alpha -= 10
            if self.alpha < 0:
                self.alpha = 0


    def say(self, text):
        agk.set_text_string(self.text, text)
        self.alpha = 255
        self.talk_timer_start = agk.timer()
        self.talk_timer_length = 5




