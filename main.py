import pygame
import os
import random
from lib import *
from constants import *
pygame.font.init()
#pygame.mixer.init()

HEALTH = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 70)

def main():
    red_health = 15
    yellow_health = 15

    clock = pygame.time.Clock()

    red = pygame.Rect(100,100,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700,100,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    while True:
        rect_1 = pygame.Rect(
        WIDTH*random.random(), 0, ASTEROID_WIDTH, ASTEROID_HEIGHT)
        rect_2 = pygame.Rect(
        WIDTH*random.random(), 0, ASTEROID_WIDTH, ASTEROID_HEIGHT)
        rect_3 = pygame.Rect(
        WIDTH*random.random(), 0, ASTEROID_WIDTH, ASTEROID_HEIGHT)
        rect_4 = pygame.Rect(
        WIDTH*random.random(), 0, ASTEROID_WIDTH, ASTEROID_HEIGHT)
    
        while True: #
            clock.tick(FPS) #
            WIN.blit(SPACE, (0,0))

            ASTEROIDS.append(ASTEROID)
            METEORS.append(ASTEROID)
            COMETS.append(ASTEROID)
            SATELLITES.append(ASTEROID)
            shooting_asteroids(rect_1, WIN, ASTEROID_WIDTH, ASTEROID_HEIGHT, ASTEROIDS, ASTEROID_RECT)
            shooting_comets(rect_3, WIN, ASTEROID_WIDTH, ASTEROID_HEIGHT, COMETS, COMET_RECT)
            shooting_meteors(rect_2, WIN, ASTEROID_WIDTH, ASTEROID_HEIGHT, METEORS, METEOR_RECT)
            shooting_satellites(rect_4, WIN, ASTEROID_WIDTH, ASTEROID_HEIGHT, SATELLITES, SATELLITE_RECT)
            red_hitting_obstacle(red, ASTEROID_RECT, METEOR_RECT, COMET_RECT, SATELLITE_RECT, RED_OBSTACLE_HIT)
            yellow_hitting_obstacle(yellow, ASTEROID_RECT, METEOR_RECT, COMET_RECT, SATELLITE_RECT, YELLOW_OBSTACLE_HIT)
            
            for event in pygame.event.get():  #for all the event in the pygame list
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                
                    if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(
                        red.x + red.width, red.y + red.height,10,5)
                        red_bullets.append(bullet)
                    #BULLER_FIRE_SOUND.play()
                
                    if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(
                        yellow.x + yellow.width,yellow.y + yellow.height,10,5)
                        yellow_bullets.append(bullet)
                    #BULLER_FIRE_SOUND.play()
            
                if event.type == RED_HIT:
                    red_health -= 1
            
                if event.type == YELLOW_HIT:
                    yellow_health -= 1

                if event.type == RED_OBSTACLE_HIT:
                    print("red_hit")

                if event.type == YELLOW_OBSTACLE_HIT:
                    print("yellow_hit")

            winner_text = ""
            if red_health <= 0:
                winner_text = "Yellow win "
                draw_winner(winner_text, YELLOW, WINNER_FONT, WIDTH, HEIGHT, WIN)
                break
            if yellow_health <= 0:
                winner_text = "Red win "
                draw_winner(winner_text, RED, WINNER_FONT, WIDTH, HEIGHT, WIN)
                break
            if rect_1.y > HEIGHT:
                ASTEROIDS.clear()
                SATELLITES.clear()
                COMETS.clear()
                METEORS.clear()
                break
            
        
            key_pressed = pygame.key.get_pressed()
            red_spaceship_controller(key_pressed, red, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, BORDER, VEL, HEIGHT)
            yellow_spaceship_controller(key_pressed, yellow, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, VEL, BORDER,WIDTH, HEIGHT )

            handle_bullet_function(red_bullets, yellow_bullets, red, yellow, WIDTH, RED_HIT, YELLOW_HIT, bullet_velocity)
        
            draw_window(red, yellow, red_bullets, 
            yellow_bullets, red_health, yellow_health, WIN, BORDER, YELLOW_SPACESHIP, RED_SPACESHIP, HEALTH, WHITE, BLACK, RED, YELLOW, WIDTH)

            
     
if __name__ == "__main__": #only run in file name main 
    main()
