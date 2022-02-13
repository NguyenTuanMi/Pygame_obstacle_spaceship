import pygame
import random
import math
from constants import *
pygame.font.init()

def generate_asteroid():
    for i in range(NUM_OF_ASTEROIDS):
        ASTEROIDS.append(ASTEROID)
        ASTEROID_X.append(WIDTH*random.random())
        ASTEROID_Y.append(0)

def shooting_asteroid():
    for i in range(NUM_OF_ASTEROIDS):
        ASTEROID_Y[i] += random.randint(5, 10)
    
def is_hit(SPACESHIP, i):
    rect = pygame.Rect(ASTEROID_X[i], ASTEROID_Y[i], ASTEROID_WIDTH, ASTEROID_HEIGHT)
    if SPACESHIP.colliderect(rect):
        return True
    else:
        return False

def draw_winner(text, COLOR):
    draw_text = WINNER_FONT.render(text, 1, COLOR)
    WIN.blit(draw_text,(
    WIDTH/2 - draw_text.get_width() /2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def draw_window(red_health, yellow_health):
    WIN.blit(SPACE, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    for i in range(NUM_OF_ASTEROIDS):
        WIN.blit(ASTEROIDS[i], (ASTEROID_X[i], ASTEROID_Y[i]))

    red_health_text = HEALTH.render(
    "Health :" + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH.render(
    "Health :" + str(yellow_health), 1, WHITE)
    
    WIN.blit(red_health_text, (10,10))
    WIN.blit(yellow_health_text, (
    (WIDTH - 10 - yellow_health_text.get_width()),10))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update() 

def handle_bullet_function(red_bullets, yellow_bullets):
    for bullet in yellow_bullets:
        bullet.x -= bullet_velocity
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x += bullet_velocity
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)

def red_spaceship_controller(key_pressed):
    if key_pressed[pygame.K_a] and red.x - VEL > 0:
            red.x -= VEL   
    if key_pressed[pygame.K_d] and red.x + VEL + SPACESHIP_WIDTH < BORDER.x:
            red.x += VEL  
    if key_pressed[pygame.K_w] and red.y - VEL > 0:
            red.y -= VEL
    if key_pressed[pygame.K_s] and red.y + VEL + SPACESHIP_HEIGHT < HEIGHT:
            red.y += VEL    

""" Speed controller of yellow spaceship """  
def yellow_spaceship_controller(key_pressed):
    if key_pressed[pygame.K_LEFT] and yellow.x - VEL > BORDER.x + BORDER.width:
            yellow.x -= VEL   
    if key_pressed[pygame.K_RIGHT] and yellow.x + VEL + SPACESHIP_WIDTH < WIDTH :
            yellow.x += VEL  
    if key_pressed[pygame.K_UP] and yellow.y - VEL > 0:
            yellow.y -= VEL
    if key_pressed[pygame.K_DOWN] and yellow.y + VEL + SPACESHIP_HEIGHT < HEIGHT:
            yellow.y += VEL    


