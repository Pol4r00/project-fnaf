import pygame
from setup import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_VEL, Q1, Q2

class Office():

    def __init__(self):

        self.background = "assets/FNaF 1 Placeholders/Office/Office Inside/126.png"
        self.bgx = 0
        self.bgy = 0

        self.ambiance = "assets/FNaF 1 Placeholders/sounds/EerieAmbienceLargeSca_MV005.wav"
        self.humming = pygame.mixer.Sound("assets/FNaF 1 Placeholders/sounds/Buzz_Fan_Florescent2.wav")
        self.boop = pygame.mixer.Sound("assets/FNaF 1 Placeholders/sounds/PartyFavorraspyPart_AC01__3.wav")
        self.error = pygame.mixer.Sound("assets/FNaF 1 Placeholders/sounds/error.wav")

        self.rbuttons = "assets/FNaF 1 Placeholders/Office/Door & Lights/R. Light/134.png"
        self.lbuttons = "assets/FNaF 1 Placeholders/Office/Door & Lights/L. Light/122.png"

        self.door_hb_l = pygame.Rect(0, SCREEN_HEIGHT * 0.4, SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12)
        self.light_hb_l = pygame.Rect(0, SCREEN_HEIGHT * 0.4 + SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12)
        self.door_hb_r = pygame.Rect(SCREEN_WIDTH - SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.4, SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12)
        self.light_hb_r = pygame.Rect(SCREEN_WIDTH - SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.4 + SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12)
        
    def load_background(self):
        office_bg = pygame.image.load(self.background)
        return office_bg

    def blit_background(self, screen, office_bg):
        screen.blit(office_bg, (self.bgx, self.bgy))

    def load_ambiance(self):
        pygame.mixer.music.load(self.ambiance)    

    def load_buttons(self):
        lbuttons = pygame.image.load(self.lbuttons)
        rbuttons = pygame.image.load(self.rbuttons)
        return lbuttons, rbuttons
    
    def blit_buttons(self, screen, lbuttons, rbuttons, office_bg):
        screen.blit(lbuttons, (self.bgx, SCREEN_HEIGHT/3.2))
        screen.blit(rbuttons, ((self.bgx + (office_bg.get_width()-lbuttons.get_width())), SCREEN_HEIGHT/3.2)) 
    
    def show_hitboxes(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.door_hb_l, width=5)
        pygame.draw.rect(screen, (0, 0, 255), self.light_hb_l, width=5)
        pygame.draw.rect(screen, (0, 0, 255), self.door_hb_r, width=5)
        pygame.draw.rect(screen, (0, 0, 255), self.light_hb_r, width=5)

    def play_ambiance(self):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)

    def play_boop(self):
        self.boop.play()
    
    def play_humming(self):
        self.humming.set_volume(0.5)
        pygame.mixer.Sound(self.humming).play(-1)

    def play_error(self):
        self.error.play()
    
    #Updates office background based on the current mouse position
    def update_bg_pos(self):
        if Q1.collidepoint(pygame.mouse.get_pos()):
            if self.bgx + PLAYER_VEL <= 0:
                self.bgx += PLAYER_VEL

        elif Q2.collidepoint(pygame.mouse.get_pos()):
            if self.bgx + PLAYER_VEL >= (-Q2.width) * 1.8:
                self.bgx -= PLAYER_VEL
    
    def mouse_in_hitbox(self, hitbox):
        if hitbox.collidepoint(pygame.mouse.get_pos()):
            return True
        
        return False
