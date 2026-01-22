import pygame
from setup import Q3

class Camera():
    def __init__(self):
        self.background = "assets/camera_ph.png"
        self.cam_flick = "assets/FNaF 1 Placeholders/Other/420.png"
        self.on = False
        self.can_toggle = True

        self.vacant_cameras = {"1a": True,
                               "1b": True,
                               "1c (1)": True,
                               "1c (2)": True,
                               "1c (3)": True,
                               "2a": True,
                               "2b": True,
                               "3": True,
                               "4a": True,
                               "4b": True,
                               "5": True,
                               "6": True,
                               "7": True,
                               "K Right Hall": True,
                               "K Left Hall": True,
                               "K Left Corridor": True,
                               "O": True
                            }

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

    def reset_cameras(self):
        for cam in self.vacant_cameras:
            self.vacant_cameras[cam] = True
