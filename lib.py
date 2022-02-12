import pygame
import os
import random

""" Generate and shoot the asteroids """
def shooting_asteroids(rect_1, WIN, ASTEROID_WIDTH, ASTEROID_HEIGHT, ASTEROIDS, ASTEROID_RECT):
    for asteroid in ASTEROIDS:
        asteroid_rect = pygame.Rect(rect_1.x, rect_1.y, ASTEROID_WIDTH, ASTEROID_HEIGHT)
        ASTEROID_RECT.append(asteroid_rect)
        WIN.blit(asteroid,(rect_1.x,rect_1.y))
        rect_1.y += 16

""" Generate and shoot the meteors """  
def shooting_meteors(rect_2, WIN, ASTEROID_WIDTH, ASTEROID_HEIGHT, METEORS, METEOR_RECT):
    for meteor in METEORS:
        meteor_rect = pygame.Rect(rect_2.x, rect_2.y, ASTEROID_WIDTH, ASTEROID_HEIGHT)
        METEOR_RECT.append(meteor_rect)
        WIN.blit(meteor, (rect_2.x, rect_2.y))
        rect_2.y += 16

""" Generate and shoot the satellites """  
def shooting_satellites(rect_4, WIN, ASTEROID_WIDTH, ASTEROID_HEIGHT, SATELLITES, SATELLITE_RECT):
    for satellite in SATELLITES:
        satellite_rect = pygame.Rect(rect_4.x, rect_4.y, ASTEROID_WIDTH, ASTEROID_HEIGHT)
        SATELLITE_RECT.append(satellite_rect)
        WIN.blit(satellite, (rect_4.x, rect_4.y))
        rect_4.y += 16

""" Generate and shoot the comets """  
def shooting_comets(rect_3, WIN, ASTEROID_WIDTH, ASTEROID_HEIGHT, COMETS, COMET_RECT):
    for comet in COMETS:
        comet_rect = pygame.Rect(rect_3.x, rect_3.y, ASTEROID_WIDTH, ASTEROID_HEIGHT)
        COMET_RECT.append(comet_rect)
        WIN.blit(comet, (rect_3.x, rect_3.y))
        rect_3.y += 16

""" Check whether any spaceship has been strucked by an obstacle or not """  
def red_hitting_obstacle(red, ASTEROID_RECT, METEOR_RECT, COMET_RECT, SATELLITE_RECT, RED_OBSTACLE_HIT):
    for asteroid in ASTEROID_RECT:
        if red.colliderect(asteroid):
            pygame.event.post(pygame.event.Event(RED_OBSTACLE_HIT))

    for meteor in METEOR_RECT:
        if red.colliderect(meteor):
            pygame.event.post(pygame.event.Event(RED_OBSTACLE_HIT))
    
    for comet in COMET_RECT:
        if red.colliderect(comet):
            pygame.event.post(pygame.event.Event(RED_OBSTACLE_HIT))

    for satellite in SATELLITE_RECT:
        if red.colliderect(satellite):
            pygame.event.post(pygame.event.Event(RED_OBSTACLE_HIT))

def yellow_hitting_obstacle(yellow, ASTEROID_RECT, METEOR_RECT, COMET_RECT, SATELLITE_RECT, YELLOW_OBSTACLE_HIT):
    for asteroid in ASTEROID_RECT:
        if yellow.colliderect(asteroid):
            pygame.event.post(pygame.event.Event(YELLOW_OBSTACLE_HIT))

    for meteor in METEOR_RECT:
        if yellow.colliderect(meteor):
            pygame.event.post(pygame.event.Event(YELLOW_OBSTACLE_HIT))
    
    for comet in COMET_RECT:
        if yellow.colliderect(comet):
            pygame.event.post(pygame.event.Event(YELLOW_OBSTACLE_HIT))

    for satellite in SATELLITE_RECT:
        if yellow.colliderect(satellite):
            pygame.event.post(pygame.event.Event(YELLOW_OBSTACLE_HIT))


""" Speed controller of red spaceship """  
def red_spaceship_controller(key_pressed, red, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, BORDER, VEL, HEIGHT):
    if key_pressed[pygame.K_a] and red.x - VEL > 0:
            red.x -= VEL   
    if key_pressed[pygame.K_d] and red.x + VEL + SPACESHIP_WIDTH < BORDER.x:
            red.x += VEL  
    if key_pressed[pygame.K_w] and red.y - VEL > 0:
            red.y -= VEL
    if key_pressed[pygame.K_s] and red.y + VEL + SPACESHIP_HEIGHT < HEIGHT:
            red.y += VEL    

""" Speed controller of yellow spaceship """  
def yellow_spaceship_controller(key_pressed, yellow,SPACESHIP_WIDTH, SPACESHIP_HEIGHT, VEL, BORDER, WIDTH, HEIGHT):
    if key_pressed[pygame.K_LEFT] and yellow.x - VEL > BORDER.x + BORDER.width:
            yellow.x -= VEL   
    if key_pressed[pygame.K_RIGHT] and yellow.x + VEL + SPACESHIP_WIDTH < WIDTH :
            yellow.x += VEL  
    if key_pressed[pygame.K_UP] and yellow.y - VEL > 0:
            yellow.y -= VEL
    if key_pressed[pygame.K_DOWN] and yellow.y + VEL + SPACESHIP_HEIGHT < HEIGHT:
            yellow.y += VEL    

""" Function deals with bullets of two spaceships """  
def handle_bullet_function(red_bullets, yellow_bullets, red, yellow, WIDTH, RED_HIT, YELLOW_HIT, bullet_velocity):
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

""" Show the winner """  
def draw_winner(text, COLOR, WINNER_FONT, WIDTH, HEIGHT, WIN):
    draw_text = WINNER_FONT.render(text, 1, COLOR)
    WIN.blit(draw_text,(
    WIDTH/2 - draw_text.get_width() /2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

""" Draw the window """  
def draw_window(red, yellow, red_bullets, yellow_bullets, 
red_health, yellow_health, WIN, BORDER, 
YELLOW_SPACESHIP, RED_SPACESHIP, HEALTH, WHITE, BLACK, RED, YELLOW, WIDTH):
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    
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

    





    



