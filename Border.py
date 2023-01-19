from Sprite import Sprite
from Color import Color
import appgamekit as agk


class Border:
    def __init__(self, host_sprite):
        self.host_sprite = host_sprite
        self.size = 5
        self.fixed_to_screen = False
        self.visible = False
        self.color = Color(0, 0, 0, 255)
        self.depth = self.host_sprite.depth

        self.sprites = []
        for i in range(0, 4):
            sprite = Sprite(-1, 0, 0, 0, 0, 0, self.depth, False, False)
            self.sprites.append(sprite)
        self.set_color(Color(0, 0, 0, 255))

    def set_alpha(self, alpha):
        self.color.alpha = alpha
        self.set_color(self.color)

    def set_depth(self, depth):
        self.depth = depth
        for sprite in self.sprites:
            sprite.set_depth(self.depth)

    def set_visible(self, visible):
        if self.visible:
            for sprite in self.sprites:
                sprite.set_visible(visible)
        else:
            for sprite in self.sprites:
                sprite.set_visible(0)

    def delete(self):
        for sprite in self.sprites:
            sprite.delete()

    def set_color(self, color):
        self.color = color
        for sprite in self.sprites:
            sprite.set_color(self.color)

    def set_size(self, size):
        self.size = size
        self.update()

    def update(self):
        sprite = self.host_sprite
        size = self.size
        x = sprite.x
        y = sprite.y
        top_y = y - size
        bottom_y = sprite.get_bottom_y()
        left_x = x - size
        right_x = sprite.get_right_x()

        width = sprite.get_width() + (size * 2)
        height = sprite.get_height()

        # Top Border
        self.sprites[0].set_size(width, size)
        self.sprites[0].set_position(left_x, top_y)

        # Right Border
        self.sprites[1].set_size(size, height)
        self.sprites[1].set_position(right_x, y)

        # Bottom Border
        self.sprites[2].set_size(width, size)
        self.sprites[2].set_position(left_x, bottom_y)

        # Left Border
        self.sprites[3].set_size(size, height)
        self.sprites[3].set_position(left_x, y)
