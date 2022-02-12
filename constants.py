import pygame
import os

# Asteroid data
ASTEROID_VELOCITY = 10
ASTEROID_WIDTH = 60
ASTEROID_HEIGHT = 55

#Spaceship data
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 45
WIDTH, HEIGHT = 900, 500
VEL = 20
MAX_BULLETS = 10

#Border
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

#Colors (in BGR)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
#BULLER_FIRE_SOUND = pygame.mixer.Sound(os.path.join('resources', 'Gun+Silencer.mp3'))

#Bullet date
red_bullets = []
yellow_bullets = []
bullet_velocity = 68

# The list contains all obstacles
ASTEROIDS = []
COMETS = []
METEORS = []
SATELLITES = []
ASTEROID_RECT = []
COMET_RECT = []
METEOR_RECT = []
SATELLITE_RECT = []

# All the event
RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2
RED_OBSTACLE_HIT = pygame.USEREVENT + 3
YELLOW_OBSTACLE_HIT = pygame.USEREVENT + 4

#Display the window of the game
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First game!s")

#FPS time
FPS = 200

#Display and change some aspects of the asteroid's picture
ASTEROID = pygame.transform.rotate(
    pygame.image.load(os.path.join('resources', 'comet.png')), 50)
ASTEROID = pygame.transform.scale(
    ASTEROID,(ASTEROID_WIDTH, ASTEROID_HEIGHT))

#Load the spaceship's pictures
YELLOW_SPACESHIP_PIC = pygame.image.load(
    os.path.join('resources','spaceship_yellow.png'))
RED_SPACESHIP_PIC = pygame.image.load(
    os.path.join('resources','spaceship_red.png'))

#Display and change some aspects of the background's picture
SPACE = pygame.transform.scale(
pygame.image.load(os.path.join('resources', 'space.png')), (900,500))

##Display and change some aspects of the spaceship's picture
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_PIC, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 270)
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_PIC, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90)
