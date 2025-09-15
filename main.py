#import nesssasery libraries
import pygame  
import os

# Initialize Pygame
pygame.init()

#setup the game window
WIDTH = 800
HEIGHT = 400

#display the game

screen = pygame.display.set_mode((WIDTH,HEIGHT))

# set capption of the game 
pygame.display.set_caption("Galaxy Fighters game Game")


#main function 
def main():
    run  = True
    while run:
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False
        
    pygame.quit()
    
    
if __name__ == "__main__":
    main()