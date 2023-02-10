import appgamekit as agk
from calculations import *
from Vectors import Vector2D, Vector3D
from Tools import *
import copy
import math

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


def where_can_i_get_to(object, obstruction_objects):
    movement_to_try = Vector2D(0, 0)
    movement_to_try.X = object.position.X - object.last_position.X
    movement_to_try.Y = object.position.Y - object.last_position.Y
    furthest_available_location_so_far = Vector2D(0, 0)
    furthest_available_location_so_far = object.last_position

    temp_object = copy.deepcopy(object)
    length = get_distance(0, 0, movement_to_try.X, movement_to_try.Y)

    number_of_steps_to_break_movement_into = math.floor(length * 2) + 1
    one_step = Vector2D(0, 0)
    one_step.X = movement_to_try.X / number_of_steps_to_break_movement_into
    one_step.Y = movement_to_try.Y / number_of_steps_to_break_movement_into

    agk.print_value("number_of_steps_to_break_movement_into " + str(number_of_steps_to_break_movement_into))

    for i in range(0, number_of_steps_to_break_movement_into):
        position_to_try = Vector2D(0, 0)
        position_to_try.X = object.last_position.X + (one_step.X * i)
        position_to_try.Y = object.last_position.Y + (one_step.Y * i)
        agk.set_sprite_position(object.sprite, position_to_try.X, position_to_try.Y)

        collision = check_tile_collisions(object, obstruction_objects, "Sprite")
        if not collision:
            furthest_available_location_so_far = position_to_try
        else:
            if movement_to_try.X != 0.0 and movement_to_try.Y != 0.0:
                is_diagonal_move = True
            else:
                is_diagonal_move = False

            agk.print_value("is_diagonal_move " + str(is_diagonal_move))

            if is_diagonal_move:
                steps_left = number_of_steps_to_break_movement_into - (i - 1)        
                remaining_horizontal_movement = Vector2D(0, 0)
                remaining_horizontal_movement.X = one_step.X * steps_left
                remaining_horizontal_movement.Y = 0.0

                final_position_if_moving_horizontally = Vector2D(0, 0)
                final_position_if_moving_horizontally.X = furthest_available_location_so_far.X + remaining_horizontal_movement.X
                final_position_if_moving_horizontally.Y = furthest_available_location_so_far.Y + remaining_horizontal_movement.Y

                temp_object.last_position = furthest_available_location_so_far
                temp_object.position = final_position_if_moving_horizontally
                furthest_available_location_so_far = where_can_i_get_to(temp_object)
            
                remaining_vertical_movement = Vector2D(0, 0)
                remaining_vertical_movement.X = 0.0
                remaining_vertical_movement.Y = one_step.Y * steps_left

                final_position_if_moving_vertically = Vector2D(0, 0)
                final_position_if_moving_vertically.X = furthest_available_location_so_far.X  + remaining_vertical_movement.X 
                final_position_if_moving_vertically.Y = furthest_available_location_so_far.Y  + remaining_vertical_movement.Y 

                temp_object.last_position = furthest_available_location_so_far
                temp_object.position = final_position_if_moving_vertically
                furthest_available_location_so_far = where_can_i_get_to(temp_object)

    return furthest_available_location_so_far



def check_tile_collisions(object, obstruction_objects, collision_mode):
    for obstruction_object in obstruction_objects:
        if collision_mode == "Sprite":
            if check_sprite_collision(object.sprite, obstruction_object.sprite):
                return True


    return False


def check_sprite_collision(sprite1, sprite2):
    if agk.get_sprite_collision(sprite1, sprite2) == 1:
        return True
    else:
        return False

