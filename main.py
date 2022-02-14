import pygame
import os
import random
from lib import * #import all in lib.py
from constants import * #import all in constants.py
pygame.font.init()
#pygame.mixer.init()

def main():
    red_health =    30  # health bar
    yellow_health = 30
    generate_asteroid()
    clock = pygame.time.Clock() # Create a clock for counting time
    run = True
    while run:
        clock.tick(FPS) #This will make sure that the code run with the given fps
        for event in pygame.event.get():  #for all the event in the pygame list
            if event.type == pygame.QUIT: #check if it quit, quit the game
                run = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN: # Check all the key have been pressed
                
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS: 
                    # If we press the left control and the length of red_bullets is 
                    # smaller than the maximum bullets we could during a momment, 
                    # append a bullet, which is a black colored rectangle, to our list
                    bullet = pygame.Rect(
                    red.x + red.width, red.y + red.height,10,5)
                    red_bullets.append(bullet)
                    #BULLER_FIRE_SOUND.play()
                
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    # Same for the rightcontrol
                    bullet = pygame.Rect(
                    yellow.x + yellow.width,yellow.y + yellow.height,10,5)
                    yellow_bullets.append(bullet)
                    #BULLER_FIRE_SOUND.play()
             
            # If the event is the RED_HIT, occured when the red is hit by the enemy's bullet, 
            # disminish 1 point for the red
            if event.type == RED_HIT:
                red_health -= 1
            
            # Same for the yellow
            if event.type == YELLOW_HIT:
                yellow_health -= 1
        # Shoot all the asteroids
        shooting_asteroid()

        # If any asteroid have surpassed the window's borders, replace that coordiante by a new one
        for i in range(NUM_OF_ASTEROIDS):
            if ASTEROID_Y[i] > HEIGHT:
                ASTEROID_Y[i] = 0
                ASTEROID_X[i] = WIDTH*random.random()

            # If the red is hit, change the coordinates of the asteroid
            if is_hit(red, i):
                red_health -= 2
                ASTEROID_X[i] = 0
                ASTEROID_Y[i] = 0

            # Same for the yellow
            if is_hit(yellow, i):
                yellow_health -= 2
                ASTEROID_X[i] = 0
                ASTEROID_Y[i] = 0


        winner_text = ""
        # If the red_health is smaller than 0, decleare that the winner is the yellow
        if red_health <= 0:
            winner_text = "Yellow win "
            draw_winner(winner_text, YELLOW)
            break
        # Same for the yellow
        if yellow_health <= 0:
            winner_text = "Red win "
            draw_winner(winner_text, RED)
            break
        
        # Get the keypressed
        key_pressed = pygame.key.get_pressed()
        # Activate the controller of 2 spaceships
        red_spaceship_controller(key_pressed)
        yellow_spaceship_controller(key_pressed)
        
        #Handle the bullet function
        handle_bullet_function(red_bullets, yellow_bullets)
        
        #Draw the window
        draw_window(red_health, yellow_health)
     
if __name__ == "__main__": #only run in file name main 
    main()
