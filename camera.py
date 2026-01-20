import pygame
from setup import Q3

class Camera():
    def __init__(self):
        self.background = "assets/FNaF 1 Placeholders/Locations/East Hall/67.png"
        self.cam_flick = "assets/FNaF 1 Placeholders/Other/420.png"
        self.on = False
        self.can_toggle = True

    def load_background(self):
        camera_bg = pygame.image.load(self.background)
        return camera_bg

    def blit_background(self, screen, camera_bg):
        screen.blit(camera_bg, (0, 0))

    def draw_cam_flick(self, screen):
        cam_flick = pygame.image.load(self.cam_flick)
        screen.blit(cam_flick, (Q3.x, Q3.y))

    def check_toggled(self, screen, toggle_box):

        if toggle_box.collidepoint(pygame.mouse.get_pos()):

            if self.can_toggle:
                self.can_toggle = False
                self.on = not self.on

        else:
            self.can_toggle = True
