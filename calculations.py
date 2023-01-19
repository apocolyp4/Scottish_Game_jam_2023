# import the math module
import math
from math import sin, cos, radians, degrees, pi, atan2

def get_distance(x1, y1, x2, y2):
    b = abs(x1 - x2)
    c = abs(y1 - y2)

    distance = math.sqrt(pow(b, 2) + pow(c, 2))
    return distance

def get_angle(x1, y1, x2, y2):
    angle = atan2(y1 - y2, x1 - x2)
    angle = degrees(angle) + 270

    if angle < 0:
        angle += 360
    elif angle > 360:
        angle -= 360

    return angle

def get_relative_angle(angle, orientation):
    relative_angle = (angle - orientation)

    if relative_angle < 0:
        relative_angle = relative_angle + 360

    if relative_angle > 360:
        relative_angle = relative_angle - 360

    return relative_angle


def get_velocity(angle, speed):
    x = cos(radians(angle - 90)) * speed
    y = sin(radians(angle - 90)) * speed
    velocity = (x, y)
    return velocity
