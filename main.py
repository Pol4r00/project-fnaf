import pygame
import random
from setup import *

from office import Office
from camera import Camera


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
            office.blit_buttons(screen, lbuttons, rbuttons, office_bg)
            office.update_bg_pos()

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
                    if office.mouse_in_hitbox(office.door_hb_l):
                        office.play_boop()

                    elif office.mouse_in_hitbox(office.light_hb_l):
                        office.play_boop()

                    elif office.mouse_in_hitbox(office.door_hb_r):
                        office.play_boop()

                    elif office.mouse_in_hitbox(office.light_hb_r):
                        office.play_boop()

        if quadrants:
            show_quadrants(screen)
            office.show_hitboxes(screen)

        if coordinates:
            show_mouse_coords(screen, font)

        pygame.display.flip()

        clock.tick(FRAMERATE_CAP)

    pygame.quit()

if __name__ == "__main__":
    main()
