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
        self.metal_clank = pygame.mixer.Sound("assets/FNaF 1 Placeholders/sounds/SFXBible_12478.wav")

        self.rbuttons = "assets/FNaF 1 Placeholders/Office/Door & Lights/R. Light/134.png"
        self.lbuttons = "assets/FNaF 1 Placeholders/Office/Door & Lights/L. Light/122.png"

        self.door_hb_l = pygame.Rect(0, SCREEN_HEIGHT * 0.4, SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12)
        self.light_hb_l = pygame.Rect(0, SCREEN_HEIGHT * 0.4 + SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12)
        self.door_hb_r = pygame.Rect(SCREEN_WIDTH - SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.4, SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12)
        self.light_hb_r = pygame.Rect(SCREEN_WIDTH - SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.4 + SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12, SCREEN_HEIGHT * 0.12)

        self.door_l_frame = 0
        self.door_r_frame = 0
        self.last_up_door_l = pygame.time.get_ticks()
        self.last_up_door_r = pygame.time.get_ticks()

        self.door_l_closed = False
        self.door_r_closed = False

    def get_door_l_frames(self):
        frames = []

        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/103.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/89.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/91.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/92.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/93.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/94.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/95.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/96.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/97.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/98.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/99.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/100.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/101.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/102.png").convert_alpha())

        return frames

    def get_door_r_frames(self):
        frames = []

        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/88.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/106.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/107.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/108.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/109.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/110.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/111.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/112.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/113.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/114.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/115.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/116.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/117.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/R. Door/118.png").convert_alpha())
        
        return frames


    def play_left_door_anim(self, screen, frames, reverse=False):
        cooldown = 20

        current_time = pygame.time.get_ticks()

        if not reverse:
            if self.door_l_frame >= 0:
                if current_time - self.last_up_door_l >= cooldown:
                    self.door_l_frame += 1
                    self.last_up_door_l = current_time

                    if self.door_l_frame >= len(frames):
                        self.door_l_frame = -1

        else:
            if self.door_l_frame <= -1:
                if current_time - self.last_up_door_l >= cooldown:
                    self.door_l_frame -= 1
                    self.last_up_door_l = current_time

                    if self.door_l_frame <= -len(frames):
                        self.door_l_frame = 0

        screen.blit(frames[self.door_l_frame], (self.bgx + SCREEN_HEIGHT * 0.12, 0))


    def play_right_door_anim(self, screen, frames, office_bg, reverse=False):
        cooldown = 20

        current_time = pygame.time.get_ticks()

        if not reverse:
            if self.door_r_frame >= 0:
                if current_time - self.last_up_door_r >= cooldown:
                    self.door_r_frame += 1
                    self.last_up_door_r = current_time

                    if self.door_r_frame >= len(frames):
                        self.door_r_frame = -1

        else:
            if self.door_r_frame <= -1:
                if current_time - self.last_up_door_r >= cooldown:
                    self.door_r_frame -= 1
                    self.last_up_door_r = current_time

                    if self.door_r_frame <= -len(frames):
                        self.door_r_frame = 0

        screen.blit(frames[self.door_r_frame], (self.bgx + (office_bg.get_width() * 0.78), 0))


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
        self.humming.play(-1)

    def stop_humming(self):
        self.humming.stop()

    def play_error(self):
        self.error.play()

    def play_metal_clank(self):
        self.metal_clank.play()
    
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
