#import nesssasery libraries
import pygame  
import os

# Initialize Pygame
pygame.init()

#setup the game window
WIDTH = 900
HEIGHT = 500
WHITE = (255,255,255)
#display the game
screen = pygame.display.set_mode((WIDTH,HEIGHT))

#speed of the gane 
FPS = 60

#WIDTH AND HEIGHT OF SPACESHIP
SPACESHIPWIDTH,SPACESHIPHEIGHT = 55,40

#our spaceship images
YELLOW_SAPCESHIP_IMAGE = pygame.image.load(os.path.join("assets","spaceship_yellow.png"))
YELLOW_SAPCESHIP =  pygame.transform.rotate(pygame.transform.scale(YELLOW_SAPCESHIP_IMAGE,(SPACESHIPWIDTH,SPACESHIPHEIGHT)),90)

RED_SAPCESHIP_IMAGE = pygame.image.load(os.path.join("assets","spaceship_red.png"))

RED_SAPCESHIP =  pygame.transform.rotate(pygame.transform.scale(RED_SAPCESHIP_IMAGE,(SPACESHIPWIDTH,SPACESHIPHEIGHT)),270)

# set capption of the game 
pygame.display.set_caption("Galaxy Fighters game Game")

#handle movement of yellow space ship 
def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a]: #press left 
            yellow.x -=  VAL
    if keys_pressed[pygame.K_d]: #press right 
            yellow.x +=  VAL
    if keys_pressed[pygame.K_w]: #press up 
            yellow.y -=  VAL
    if keys_pressed[pygame.K_s]: #press down 
            yellow.y +=  VAL
#set every move
VAL = 5
#draw window function 
def draw_window(red,yellow):
     screen.fill(WHITE)
     screen.blit(YELLOW_SAPCESHIP, (yellow.x,yellow.y))
     screen.blit(RED_SAPCESHIP, (red.x,red.y))
     pygame.display.update()   
#main function 
def main():
    red = pygame.Rect(700,300,SPACESHIPWIDTH,SPACESHIPHEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIPWIDTH,SPACESHIPHEIGHT)
    clock = pygame.time.Clock()
    run  = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed() 
        yellow_handle_movement(keys_pressed,yellow)
        draw_window(red,yellow)
    pygame.quit()
    
    
if __name__ == "__main__":
    main()