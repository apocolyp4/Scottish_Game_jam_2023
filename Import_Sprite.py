import appgamekit as agk
from Sprite import *


def import_sprite(id, visual_editor, scene_id):
    sprite_id = visual_editor.get_entity_id(id, scene_id)
    x = agk.get_sprite_x(sprite_id)
    y = agk.get_sprite_y(sprite_id)
    width = agk.get_sprite_width(sprite_id)
    height = agk.get_sprite_width(sprite_id)
    angle = agk.get_sprite_angle(sprite_id)
    depth = agk.get_sprite_depth(sprite_id)
    new_sprite = Sprite("NULL", x, y, width, height, angle, depth, 1, 1)
    new_sprite.id = sprite_id
    new_sprite.update()
    return new_sprite
