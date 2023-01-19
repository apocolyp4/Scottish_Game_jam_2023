import appgamekit as agk
from Color import Color

class Text:
    def __init__(self, text, color, size, x, y, depth, centered, visible):
        self.text = text
        self.x = x
        self.y = y
        self.active = True
        self.old_x = x
        self.old_y = y

        self.fixed_to_screen = False
        self.size = size
        self.width = 0
        self.height = 0
        self.depth = depth
        self.angle = 0
        self.centered = centered
        self.visible = visible
        self.scale = 1.0
        self.color = color
        self.id = agk.create_text(self.text)
        self.update()

    def update(self):
        self.old_x = self.x
        self.old_y = self.y

        self.set_color(self.color)
        self.set_centered(self.centered)
        self.set_size(self.size)
        self.set_position(self.x, self.y)
        self.set_depth(self.depth)
        self.set_visible(self.visible)

    def set_size(self, size):
        self.size = size
        agk.set_text_size(self.id, self.size)
        self.set_position(self.x, self.y)

    def resize(self, size):
        self.size = size
        agk.set_text_size(self.id, self.size)
        self.position(self.x, self.y)

    def set_position(self, x, y):
        self.old_x = self.x
        self.old_y = self.y

        if self.centered:
            centred_x = x - ((self.get_width() * self.scale) / 2)
            centred_y = y - ((self.get_height() * self.scale) / 2)
            agk.set_text_position(self.id, centred_x, centred_y)
        else:
            self.x = x
            self.y = y
            agk.set_text_position(self.id, self.x, self.y)

    def set_angle(self, angle):
        self.angle = angle
        agk.set_text_angle(self.id, self.angle)

    def set_depth(self, depth):
        self.depth = depth
        agk.set_text_depth(self.id, self.depth)

    def set_scale(self, scale):
        self.scale = scale
        agk.set_sprite_size(self.id, self.width * self.scale, self.height * self.scale)
        self.position(self.x, self.y)

    def set_centered(self, centered):
        self.centered = centered
        self.set_position(self.x, self.y)

    def set_visible(self, visible):
        self.visible = visible
        if self.visible and self.active:
            agk.set_text_visible(self.id, 1)
        else:
            agk.set_text_visible(self.id, 0)

    def get_width(self):
        self.width = agk.get_text_total_width(self.id)
        return self.width

    def get_height(self):
        self.height = agk.get_text_total_height(self.id)
        return self.height

    def get_centre_x(self):
        centre_x = self.x - (self.get_width() / 2)
        return centre_x

    def get_centre_y(self):
        centre_y = self.y - (self.get_height() / 2)
        return centre_y

    def get_centre_position(self):
        centre_x = self.get_centre_x()
        centre_y = self.get_centre_y()
        return centre_x, centre_y

    def get_angle(self):
        angle = agk.get_text_char_angle(self.id, 0)
        return angle

    def set_alpha(self, alpha):
        if self.active:
            self.color.alpha = alpha
        else:
            self.color.alpha = 0

        self.set_color(self.color)

    def set_color(self, color):
        self.color = color
        agk.set_text_color(self.id, self.color.red, self.color.green, self.color.blue, self.color.alpha)

    def set_string(self, text):
        self.text = text
        agk.set_text_string(self.id, self.text)

    def set_fixed_to_screen(self, fixed):
        self.fixed_to_screen = fixed
        agk.fix_text_to_screen(self.id, self.fixed_to_screen)

    def delete(self):
        agk.delete_text(self.id)

    def set_active(self, active):
        self.active = active