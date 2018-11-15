# this file is still in progress #WIP

"""
The module frontend is part of RoboProject by Pyladies Brno.

Key library is pyglet Python library  https://bitbucket.org/pyglet/pyglet/wiki/Home
This module imports the backend module and is imported in game module.

The frontend module
    - creates a Pyglet window for drawing
    - loads pyglet sprites
    - draws images to display the game board
"""

import pyglet
from pathlib import Path
import random

def init_window(WINDOW_WIDTH, WINDOW_HEIGHT):
    """
    creates a pyglet window for graphic output

    is called in the game module and uses arguments
    WINDOW_WIDTH and WINDOW_HEIGHT from the game module
    """
    window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    return window


def load_images(data, state, TILE_WIDTH, TILE_HEIGHT):
    """
    makes a list of images

    calls backends' get_real_ids function (returning a dictionary of IDs)
    creates empty list of images and fills it with data from JSON
    (including layers, coordinates, rotation)
    """
    images = []

    #filling the empty list of images
    for layer in state:
        # state is distioary created in backends function get_coordiante_dict
# !!!!!!!!!!!!!!!!!!! tuhle cast asi jeste rozsirit !!!!!!!!!!!!!!!!
        for key, value in state[layer].items():
            rotation = value.rotation
            path = value.path
            if path != 0:
                img = pyglet.image.load(path)
                img.anchor_x = img.width//2
                img.anchor_y = img.height//2
                x, y = key
                tile_x = x*TILE_WIDTH
                tile_y = y*TILE_HEIGHT
                img = pyglet.sprite.Sprite(img, x=img.anchor_x+tile_x, y=img.anchor_y+tile_y)
                img.rotation = rotation
                images.append(img)
    return images

def load_robots(starting_coordinate_list, TILE_WIDTH, TILE_HEIGHT):
    robots = []
    robot_list = []
    for robot in Path('./img/robots_map/png/').iterdir():
        robot_list.append(robot)

    for coordinate in starting_coordinate_list:
        x, y = coordinate
        i = random.choice(robot_list)
        robot_list.remove(i)
        img = pyglet.image.load(i)
        img.anchor_x = img.width//2
        img.anchor_y = img.height//2
        tile_x = x*TILE_WIDTH
        tile_y = y*TILE_HEIGHT
        img = pyglet.sprite.Sprite(img, x=img.anchor_x+tile_x, y=img.anchor_y+tile_y)
        robots.append(img)
    return robots

def draw_board(state, images, robots):
    """
    draws the game map
    """
    images.extend(robots)
    for tile in images:
        tile.draw()


# WIP
