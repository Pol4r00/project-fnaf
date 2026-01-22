import pygame
import random
import time
from setup import *

from menu import Menu
from office import Office
from camera import Camera
from character import Character

GAME_OVER = pygame.USEREVENT +1

#Main game loop
def main():
    pygame.init()

    screen = init_screen()
    menu = Menu()
    office = Office()
    camera = Camera()
    game_over = pygame.event.Event(GAME_OVER)

    freddy = Character(0, 20)
    bonnie = Character(1, 20)
    chica = Character(2, 20)
    foxy = Character(3, 20)

    characters = [freddy, bonnie, chica, foxy]
 
    menu_bg = menu.load_background()
    ng_button, ng_hitbox = menu.load_ng_button()

    office_bg = office.load_background()
    lbuttons, rbuttons = office.load_buttons()
    door_l_frames = office.get_door_l_frames()
    door_r_frames = office.get_door_r_frames()
    
    freddy_frames = freddy.get_freddy_frames()
    bonnie_frames = bonnie.get_bonnie_frames()
    chica_frames = chica.get_chica_frames()
    foxy_frames = foxy.get_foxy_frames()
    
    theme = menu.load_theme()
    
    camera_bg = camera.load_background()

    font = pygame.font.Font(None, size=20)

    quadrants = False
    coordinates = False
    run = True
    
    freddy_current_cam, bonnie_current_cam, chica_current_cam, foxy_current_cam = reset_characters(characters) 

    clock = pygame.time.Clock()

    menu.play_theme()

    while run:
        screen.fill(DEFAULT_COLOR)     

        camera.check_toggled(screen, Q3)
        
        if not menu.start:
            menu.blit_background(screen, menu_bg)
            menu.draw_title(screen)
            menu.blit_ng_button(screen, ng_button)
        
        elif menu.start:
            if camera.on:
                camera.blit_background(screen, camera_bg)

            else:
                
                office.blit_background(screen, office_bg)
                office.blit_buttons(screen, lbuttons, rbuttons, office_bg)

                if office.door_l_closed:
                    office.play_left_door_anim(screen, door_l_frames)

                else:
                    office.play_left_door_anim(screen, door_l_frames, reverse=True)
            
                if office.door_r_closed:
                    office.play_right_door_anim(screen, door_r_frames, office_bg)

                else:
                    office.play_right_door_anim(screen, door_r_frames, office_bg, reverse=True)

                camera.draw_cam_flick(screen)
            
                office.update_bg_pos()

                if freddy_current_cam == "O" or bonnie_current_cam == "O" or chica_current_cam == "O" or foxy_current_cam == "O":
                    if foxy_current_cam == "O": 
                        foxy.play_scream()
                        if foxy.jumpscare_frame >= 0:
                            foxy.play_jumpscare(screen, foxy_frames)

                        else:
                            foxy.jumpscare_frame = 0
                            pygame.event.post(game_over)

                    elif freddy_current_cam == "O":
                        freddy.play_scream()
                        if freddy.jumpscare_frame >= 0:
                            freddy.play_jumpscare(screen, freddy_frames)

                        else:
                            freddy.jumpscare_frame = 0
                            pygame.event.post(game_over)

                    elif bonnie_current_cam == "O":
                        bonnie.play_scream()
                        if bonnie.jumpscare_frame >= 0:
                            bonnie.play_jumpscare(screen, bonnie_frames)

                        else:
                            bonnie.jumpscare_frame = 0
                            pygame.event.post(game_over)

                    elif chica_current_cam == "O":
                        chica.play_scream()
                        if chica.jumpscare_frame >= 0:
                            chica.play_jumpscare(screen, chica_frames)

                        else:
                            chica.jumpscare_frame = 0
                            pygame.event.post(game_over)

                else:
                    bonnie_current_cam = bonnie.calculate_movement(bonnie_current_cam, camera, office.door_l_closed)
                    chica_current_cam = chica.calculate_movement(chica_current_cam, camera, office.door_r_closed)
                    foxy_current_cam = foxy.calculate_movement(foxy_current_cam, camera, office.door_l_closed)
                    freddy_current_cam = freddy.calculate_movement(freddy_current_cam, camera, office.door_r_closed)
                    
            if quadrants:
                show_quadrants(screen)
                office.show_hitboxes(screen)
            
            if coordinates:
                show_mouse_coords(screen, font, freddy_current_cam, bonnie_current_cam, chica_current_cam, foxy_current_cam)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:          
                    quadrants = not quadrants

                elif event.key == pygame.K_i:
                    coordinates = not coordinates
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not menu.start:
                    if menu.mouse_in_ng(ng_hitbox):
                        menu.start = True
                        pygame.mixer.music.stop()

                        office.load_ambiance()
                        office.play_ambiance()
                        office.play_humming()

                elif not camera.on:
                    if office.mouse_in_hitbox(office.door_hb_l):
                        office.play_metal_clank()
                        office.door_l_closed = not office.door_l_closed

                    elif office.mouse_in_hitbox(office.light_hb_l):
                        office.play_error()

                    elif office.mouse_in_hitbox(office.door_hb_r):
                        office.play_metal_clank()
                        office.door_r_closed = not office.door_r_closed

                    elif office.mouse_in_hitbox(office.light_hb_r):
                        office.play_error()

            if event.type == GAME_OVER:
                    
                    foxy.play_jumpscare(screen, foxy_frames)
                    office.play_boop()
                    office.stop_humming()
                    menu.stop_theme()
                    
                    freddy_current_cam, bonnie_current_cam, chica_current_cam, foxy_current_cam = reset_characters(characters)

                    camera.reset_cameras()
                    
                    menu.start = not menu.start
                    
                    menu.load_theme()
                    menu.play_theme()

        

        pygame.display.flip()

        clock.tick(FRAMERATE_CAP)

    pygame.quit()

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
def show_mouse_coords(screen, font, freddy, bonnie, chica, foxy):
    
    freddy_loc = font.render(f"Freddy: {freddy}", True, (255, 255, 255))
    bonnie_loc = font.render(f"Bonnie: {bonnie}", True, (255, 255, 255))
    chica_loc = font.render(f"Chica: {chica}", True, (255, 255, 255))
    foxy_loc = font.render(f"Foxy: {foxy}", True, (255, 255, 255))

    screen.blit(freddy_loc, (15, 15))
    screen.blit(bonnie_loc, (15, 30))
    screen.blit(chica_loc, (15, 45))
    screen.blit(foxy_loc, (15, 60))



def reset_characters(characters):
    starters = []

    for character in characters:
        character_current_cam = character.starting_cam
        starters.append(character_current_cam)
    
    return starters

if __name__ == "__main__":
    main()
