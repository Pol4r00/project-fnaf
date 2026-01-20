import pygame
from office import Office
from camera import Camera

SCREEN_WIDTH = 980
SCREEN_HEIGHT = 680

#Defines screen areas in which mouse interaction is possible 
Q1 = pygame.Rect(0, 0, round(SCREEN_WIDTH / 3), SCREEN_HEIGHT)
Q2 = pygame.Rect(SCREEN_WIDTH - round(SCREEN_WIDTH / 3), 0, round(SCREEN_WIDTH / 3), SCREEN_HEIGHT)
Q3 = pygame.Rect(Q1.width * 0.75, SCREEN_HEIGHT * 0.9, SCREEN_WIDTH - Q1.width - Q2.width + (Q1.width * 0.50), SCREEN_HEIGHT * 0.1)

DOOR_HB_L = pygame.Rect(0, SCREEN_HEIGHT*0.4, SCREEN_HEIGHT*0.12, SCREEN_HEIGHT*0.12)
LIGHT_HB_L = pygame.Rect(0, (SCREEN_HEIGHT*0.4)+(SCREEN_HEIGHT*0.12), SCREEN_HEIGHT*0.12, SCREEN_HEIGHT*0.12)

DOOR_HB_R = pygame.Rect(SCREEN_WIDTH - SCREEN_HEIGHT*0.12, SCREEN_HEIGHT*0.4, SCREEN_HEIGHT*0.12, SCREEN_HEIGHT*0.12)
LIGHT_HB_R = pygame.Rect(SCREEN_WIDTH - SCREEN_HEIGHT*0.12, (SCREEN_HEIGHT*0.4)+(SCREEN_HEIGHT*0.12), SCREEN_HEIGHT*0.12, SCREEN_HEIGHT*0.12)

CAPTION = "project-fnaf"
ICON = "assets/foxy.png"

FRAMERATE_CAP = 60
PLAYER_VEL = 18

#Default color for debugging purposes
DEFAULT_COLOR = (255, 10, 120)

#Initializes the screen with custom icon and caption
def init_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    icon = pygame.image.load(ICON)

    pygame.display.set_caption(CAPTION)
    pygame.display.set_icon(icon)

    return screen

#Displays pygame Rect objects for debugging purposes
def show_quadrants(screen):
    pygame.draw.rect(screen, (255, 0, 0), Q1, width=5)
    pygame.draw.rect(screen, (255, 0, 0), Q2, width=5)
    pygame.draw.rect(screen, (0, 255, 0), Q3, width=5)

    pygame.draw.rect(screen, (0, 0, 255), DOOR_HB_L, width=5)
    pygame.draw.rect(screen, (0, 0, 255), LIGHT_HB_L, width=5)
    pygame.draw.rect(screen, (0, 0, 255), DOOR_HB_R, width=5)
    pygame.draw.rect(screen, (0, 0, 255), LIGHT_HB_R, width=5)


#Displays dynamic mouse coordinates for debbuging purposes
def show_mouse_coords(screen, font):
    mx, my = pygame.mouse.get_pos()
    mouse_coords_txt = font.render(f"MOUSE ({mx}, {my})", True, (255, 255, 255))

    screen.blit(mouse_coords_txt, (15, 15))

#Main game loop
def main():
    pygame.init()

    screen = init_screen()
    office = Office()
    camera = Camera()

    office_bg = office.load_background()
    lbuttons, rbuttons = office.load_buttons()
    ambiance = office.load_ambiance()

    camera_bg = camera.load_background()

    office.play_ambiance()

    font = pygame.font.Font(None, size=20)

    quadrants = False
    coordinates = False
    run = True

    clock = pygame.time.Clock()

    while run:
        screen.fill(DEFAULT_COLOR)

        camera.check_toggled(screen, Q3)

        if camera.on:
            camera.blit_background(screen, camera_bg)

        else:
            office.blit_background(screen, office_bg)
            office.blit_buttons(screen, lbuttons, rbuttons, office_bg, SCREEN_HEIGHT)
            office.update_bg_pos(Q1, Q2, PLAYER_VEL)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:          
                    quadrants = not quadrants

                elif event.key == pygame.K_i:
                    coordinates = not coordinates
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not camera.on:
                    if office.mouse_in_hitbox(DOOR_HB_L):
                        office.play_boop()

                    elif office.mouse_in_hitbox(LIGHT_HB_L):
                        office.play_boop()

                    elif office.mouse_in_hitbox(DOOR_HB_R):
                        office.play_boop()

                    elif office.mouse_in_hitbox(LIGHT_HB_R):
                        office.play_boop()

        if quadrants:
            show_quadrants(screen)

        if coordinates:
            show_mouse_coords(screen, font)

        pygame.display.flip()

        clock.tick(FRAMERATE_CAP)

    pygame.quit()

if __name__ == "__main__":
    main()
