import pygame
import os
import random
from thread import *
from constants import *
pygame.font.init()
#pygame.mixer.init()

def main():
    red_health =    30  
    yellow_health = 30
    generate_asteroid()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
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
      
        shooting_asteroid()

        for i in range(NUM_OF_ASTEROIDS):
            if ASTEROID_Y[i] > HEIGHT:
                ASTEROID_Y[i] = 0
                ASTEROID_X[i] = WIDTH*random.random()

            if is_hit(red, i):
                red_health -= 2
                ASTEROID_X[i] = 0
                ASTEROID_Y[i] = 0

            if is_hit(yellow, i):
                yellow_health -= 2
                ASTEROID_X[i] = 0
                ASTEROID_Y[i] = 0
               
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow win "
            draw_winner(winner_text, YELLOW)
            break
        if yellow_health <= 0:
            winner_text = "Red win "
            draw_winner(winner_text, RED)
            break
        
        key_pressed = pygame.key.get_pressed()
        red_spaceship_controller(key_pressed)
        yellow_spaceship_controller(key_pressed)

        handle_bullet_function(red_bullets, yellow_bullets)
        
        draw_window(red_health, yellow_health)
     
if __name__ == "__main__": #only run in file name main 
    main()
