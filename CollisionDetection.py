import appgamekit as agk
from calculations import *
import copy

def get_text_point_collision(text, point_x, point_y):
    width = text.get_width()
    height = text.get_height()
    angle = text.get_angle()

    x, y = text.get_centre_position()
    collision = get_point_box_collision(point_x, point_y, x, y, width, height, angle)
    return collision


def get_sprite_point_collision(sprite, point_x, point_y):
    width = sprite.get_width()
    height = sprite.get_height()
    angle = sprite.get_angle()
    x, y = sprite.get_centre_position()
    collision = get_point_box_collision(point_x, point_y, x, y, width, height, angle)
    return collision

def get_bubble_collision(sprite1, sprite2):
    collision = False

    distance = get_distance(sprite1.x, sprite1.y, sprite2.x, sprite2.y)
    if distance < (sprite1.width/2) + (sprite2.width/2):
        return True

    return False


def get_point_box_collision(point_x, point_y, x, y, width, height, angle):
    collision = True

    velocity = get_velocity(angle, height / 2)
    x1 = x + velocity[0]
    y1 = y + velocity[1]

    velocity = get_velocity(angle - 180, height / 2)
    x2 = x + velocity[0]
    y2 = y + velocity[1]

    velocity = get_velocity(angle - 90, width / 2)
    x3 = x + velocity[0]
    y3 = y + velocity[1]

    velocity = get_velocity(angle + 90, width / 2)
    x4 = x + velocity[0]
    y4 = y + velocity[1]

    # Box top side
    angle1 = get_angle(x1, y1, point_x, point_y)
    angle1 = get_relative_angle(angle1, angle)

    # Box bottom side
    angle2 = get_angle(x2, y2, point_x, point_y)
    angle2 = get_relative_angle(angle2, angle - 180)

    # Box left side
    angle3 = get_angle(x3, y3, point_x, point_y)
    angle3 = get_relative_angle(angle3, angle - 90)

    # Box right side
    # Box left  side
    angle4 = get_angle(x4, y4, point_x, point_y)
    angle4 = get_relative_angle(angle4, angle + 90)

    if angle1 > 270 or angle1 < 90:
        collision = False

    if angle2 > 270 or angle2 < 90:
        collision = False

    if angle3 > 270 or angle3 < 90:
        collision = False

    if angle4 > 270 or angle4 < 90:
        collision = False

    return collision



def check_wall_collision(sprite_id, walls):
    for wall in walls:
        collision = agk.get_sprite_collision(sprite_id, wall)
        if collision == 1:
            return True

    return False

