import pygame
import os
import time
import random
import FrameCreator
import ShipCreator as sc

# created global variables of libraries
OS_LIB = os
PG_LIB = pygame
TIME_LIB = time
RANDOM_LIB = random
FrameCreator_LIB = FrameCreator

# Created global variables of Integer values
FPS = 60
LEVEL = 1
LIVES = 5
WIDTH, HEIGHT = 750, 750
PLAYER_VEL = 5
GOOD_SHIP_SIZEX, GOOD_SHIP_SIZEY = 50, 50
# Created global variables of Font
PG_LIB.font.init()
MAIN_FONT = PG_LIB.font.SysFont("comicsans", 50)


WINDOW = PG_LIB.display.set_mode((WIDTH, HEIGHT))

# Created global variables of boats images
GOOD_SHIP_PNG = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "good_ship.png")), (GOOD_SHIP_SIZEX, GOOD_SHIP_SIZEY))

BAD_SHIP_RED_PNG = PG_LIB.image.load(os.path.join("assets", "bad_ship_red.png"))
BAD_SHIP_BLUE_PNG = PG_LIB.image.load(os.path.join("assets", "bad_ship_blue.png"))
BAD_SHIP_PURPLE_PNG = PG_LIB.image.load(os.path.join("assets", "bad_ship_purple.png"))

BAD_LASER_PNG = PG_LIB.image.load(os.path.join("assets", "bad_laser.png"))
GOOD_LASER_PNG = PG_LIB.image.load(os.path.join("assets", "good_laser.png"))

# Created global variables of background images
BACKGROUND_PNG = PG_LIB.transform.scale(PG_LIB.image.load(os.path.join("assets", "background.png")), (WIDTH, HEIGHT))

# Created ships
GOOD_SHIP = sc.Player(300, 650)

