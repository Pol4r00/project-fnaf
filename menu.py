import pygame
from setup import *


class Menu():

    def __init__(self):
        
        self.background = "assets/FNaF 1 Placeholders/Static & Menu/Menu/431.png"
        self.start = False
        self.font = pygame.font.Font(None, size=50)
        self.theme = "assets/titlemusic.wav"
        self.ng_button = "assets/FNaF 1 Placeholders/Numbers & Nights/Camera and Nights/448.png"
        self.load_icon = "assets/FNaF 1 Placeholders/Other/482.png"

    def draw_title(self, screen):
        title = self.font.render("PROJECT FNAF", True, (255, 255, 255))
        screen.blit(title, (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.1))
    
    def load_theme(self):
        pygame.mixer.music.load(self.theme)

    def play_theme(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def stop_theme(self):
        pygame.mixer.music.stop()

    def load_background(self):
        menu_bg = pygame.image.load(self.background)
        return menu_bg
    
    def blit_background(self, screen, menu_bg):
        screen.blit(menu_bg, (0, 0))
    
    def load_ng_button(self):
        ng_button = pygame.image.load(self.ng_button)
        ng_hitbox = pygame.Rect(SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.3, ng_button.get_width(), ng_button.get_height())

        return ng_button, ng_hitbox

    def blit_ng_button(self, screen, ng_button):
        screen.blit(ng_button, (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.3))
    
    def mouse_in_ng(self, ng_button):
        if ng_button.collidepoint(pygame.mouse.get_pos()):
            return True
        
        return False
    
