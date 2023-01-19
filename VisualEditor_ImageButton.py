import appgamekit as agk
from Sprite import Sprite
from Text import Text
from Border import Border
from Color import Color
from CollisionDetection import *

class ImageButton:
    def __init__(self, image_name, text):
        self.name = ""
        self.image_name = image_name
        self.id = ""
        self.active = True
        self.images = []
        self.depth = 0
        self.active = True
        self.angle = 0.0
        self.is_switch = False
        self.is_visible = True
        self.is_centered = False
        self.fixed_to_screen = False
        self.update_with_orientation = True
        self.mode = 0

        self.image_frame = 0
        self.pressed_frame = 0
        self.update_if_pressed = True

        self.pressed_alpha = 100
        self.pressed_frame_no = 0

        self.x = 0
        self.y = 0
        self.last_pointer_x = 0
        self.last_pointer_y = 0

        self.width = 200
        self.height = 50
        self.pressed_alpha = 0
        self.fixed_to_screen = 0

        self.state = False
        self.pressed = False
        self.released = False
        self.update_if_pressed = False

        self.border_visible = False
        self.border_color = Color(0, 0, 0, 0)
        self.border_size = 0
        self.border_image = 0
        self.border_sprites = []

        self.image_color = Color(255, 255, 255, 255)
        self.previous_state = False
        self.mode = 0

        if self.image_name == "":
            self.image_no = agk.create_image_color(255, 255, 255, 255)
            self.width = 200
            self.height = 50
            self.border_visible = True
        else:
            self.image_no = agk.load_image(self.image_name)
            self.width = agk.get_image_width(self.image_no)
            self.height = agk.get_image_height(self.image_no)
            self.border_visible = False

        self.images.append(self.image_no)
        self.depth = 0
        self.sprite = Sprite(self.image_no, 0, 0, self.width, self.height, self.angle, self.depth, False, True)
        self.sprite.set_color(self.image_color)
        self.pressed_frame = 0
        self.pressed_alpha = 100
        self.alpha = 255

        self.text_size = 48
        self.text_color = Color(0, 0, 0, 255)
        self.text_offset_x = 0
        self.text_offset_y = 0
        self.text = Text(text, self.text_color, self.text_size, 0, 0, self.depth, True, True)

        self.border = Border(self.sprite)
        self.border.visible = self.border_visible
        self.update_if_pressed = True
        self.set_position(0, 0)
        self.set_visible(True)

    def make_switch(self, x, y, width, height, alignment, depth ):
        self.is_switch = True
        self.is_centered = alignment
        self.set_size(width, height)
        self.set_depth(depth)
        self.set_position(x, y)

    def set_size(self, width, height):
        self.width = width
        self.height = height
        self.sprite.resize(self.width, self.height)
        self.update_position()

    def set_depth(self, depth):
        self.depth = depth
        self.sprite.set_depth(self.depth)
        self.text.set_depth(self.depth)
        self.border.set_depth(self.depth)

    def set_position(self, x, y):
        self.x = x
        self.y = y

        if self.is_centered:
            self.sprite.centered = 1
        else:
            self.sprite.centered = 0

        self.sprite.set_position(x, y)

        x = self.sprite.get_centre_x()
        y = self.sprite.get_centre_y()
        self.text.set_position(x, y)

    def update_position(self):
        self.set_position(self.x, self.y)

    def set_button_color(self, color):
        self.image_color = color
        self.sprite.set_color(self.image_color)

    def set_text_color(self, color):
        self.text_color = color
        self.text.set_color(color)

    def set_visible(self, visible):
        self.sprite.set_visible(visible)
        self.text.set_visible(visible)
        self.border.set_visible(visible)

    def fixed_to_screen(self, fixed):
        self.fixed_to_screen = fixed
        self.sprite.set_fixed_to_screen(self.fixed_to_screen)
        self.text.set_fixed_to_screen(self.fixed_to_screen)
        self.border.fixed_to_screen(self.fixed_to_screen)

    def update(self):
        if self.active:
            self.update_state()
        else:
            self.pressed = False
            self.released = False

        self.update_size()
        self.update_position()

        if self.update_if_pressed:
            self.update_state_appearance()

        self.set_visible(True)
        self.border.update()

    def update_size(self):
        pass

    def update_state_appearance(self):

        if self.pressed_frame_no > 0:
            if self.state:
               self.set_frame(self.pressed_frame_no)
            else:
                self.set_frame(0)
        else:
            if self.state:
                self.sprite.set_alpha(self.pressed_alpha)
                self.text.set_alpha(self.pressed_alpha)
                self.border.set_alpha(self.pressed_alpha)
            else:
                self.sprite.set_alpha(255)
                self.text.set_alpha(255)
                self.border.set_alpha(255)

    def set_frame(self, frame_no):
        pass

    def delete(self):
        self.text.delete()
        self.sprite.delete()
        self.border.delete()

    def update_state(self):
        pointer_x = agk.get_pointer_x()
        pointer_y = agk.get_pointer_y()

        if not self.is_switch:
            if agk.get_pointer_state() == 1:
                sprite_hit = agk.get_sprite_in_circle(self.sprite.id, pointer_x, pointer_y, 0)
                text_hit = get_text_point_collision(self.text, pointer_x, pointer_y)
                if sprite_hit or text_hit:
                    self.state = 1
                else:
                    self.state = 0
            else:
                self.state = 0
        else:
            if agk.get_pointer_pressed() == 1:
                sprite_hit = agk.get_sprite_in_circle(self.sprite.id, pointer_x, pointer_y, 0)
                text_hit = get_text_point_collision(self.text, pointer_x, pointer_y)

                if sprite_hit or text_hit:
                    self.pressed = True
                else:
                    self.pressed = False

                if self.pressed:
                    if not self.state:
                        self.state = True
                    else:
                        self.state = False

        # Check if button was clicked
        if not self.previous_state and self.state:
            self.pressed = True
        else:
            self.pressed = False

        # Check if button was released
        if agk.get_pointer_released() == 1:
            self.released = agk.get_sprite_in_circle(self.sprite.id, self.last_pointer_x, self.last_pointer_y, 0)
            if self.released:
                self.released = True
            else:
                self.released = False
        else:
            self.released = False

        self.previous_state = self.state
        self.last_pointer_x = pointer_x
        self.last_pointer_y = pointer_y

