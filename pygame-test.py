import pygame
from character import Character

SCREEN_WIDTH = 980
SCREEN_HEIGHT = 680

def main():
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True

    bonnie = Character(2, 20)
    current_cam = bonnie.starting_cam
    

    while run:
        screen.fill((255, 10, 120))
        
        current_cam = bonnie.calculate_movement(current_cam)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    main()
