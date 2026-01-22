import pygame
from character import Character

SCREEN_WIDTH = 980
SCREEN_HEIGHT = 680

def main():
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True
    jumpscare = False
    
    count = 0
    foxy = Character(3, 20)
    current_cam = foxy.starting_cam

    foxy_frames = foxy.get_foxy_frames()
    
    
    clock = pygame.time.Clock()
    while run:
        screen.fill((255, 10, 120))
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    jumpscare = True
                    
        if jumpscare:
            foxy.play_jumpscare(screen, foxy_frames)



        pygame.display.flip()

        clock.tick(60)

pygame.quit()


if __name__ == "__main__":
    main()
