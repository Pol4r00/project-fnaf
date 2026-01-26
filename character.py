import pygame
import random

from setup import ENEMY_VEL

class Character():

    def __init__(self, character_num, ai_level):

        self.character_num = character_num
        self.ai_level = ai_level
        self.move_timer = pygame.time.get_ticks()
        
        self.jumpscare_frame = 0
        self.last_updated_frame = pygame.time.get_ticks()
        
        self.scream = pygame.mixer.Sound("assets/FNaF 1 Placeholders/sounds/XSCREAM.wav")
        if self.character_num == 0:

            self.path = {

                    '1a': ['1b'],
                    '1b': ['7'],
                    '7': ['6'],
                    '6': ['4a'],
                    '4a': ['4b'],
                    '4b': ['1b'],
                    'O': ['O']

            }

            self.starting_cam = "1a"
            self.character_name = "Freddy"
            self.killcam = "4b"
                    
        if self.character_num == 1:

            self.path = {

                        '1a': ['1b', '5'],
                        '1b': ['5', '2a', '3'],
                        '5': ['1b', '2a', '3'],
                        '3': ['2a', '1b', '5'],
                        '2a': ['2b', '3', '1b', '5'],
                        '2b': ['3', 'K Left Hall'],
                        'K Left Hall': ['1b', '5'],
                        'O': ['O']
                
                    }

            
            self.starting_cam = "1a"
            self.character_name = "Bonnie"
            self.killcam = "K Left Hall"

        if self.character_num == 2:
            
            self.path = {

                    '1a': ['1b'],
                    '1b': ['7'],
                    '7' : ['1b', '6'],
                    '6': ['7', '4a'],
                    '4a': ['4b'],
                    '4b': ['4a', 'K Right Hall'],
                    'K Right Hall': ['1b', '7'], 
                    'O': ['O']

                }

            self.starting_cam = "1a"
            self.character_name = "Chica"
            self.killcam = "K Right Hall"
        
        if self.character_num == 3:

            self.path = {

                    '1c (1)': ['1c (2)'],
                    '1c (2)': ['1c (3)'],
                    '1c (3)': ['K Left Corridor'],
                    'K Left Corridor': ['1c (1)'],
                    'O': ['O']

                }

            self.starting_cam = "1c (1)"
            self.character_name = "Foxy"
            self.killcam = "K Left Corridor"

    def get_freddy_frames(self):
        frames = []

        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/39.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/485.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/489.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/490.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/491.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/493.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/495.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/496.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/497.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/498.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/499.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/500.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/501.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/502.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/503.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/504.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/505.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/506.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/507.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/508.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/509.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/510.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/511.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/512.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/513.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/514.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/515.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/516.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/517.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Freddy/Peekaboo!/518.png").convert_alpha())

        return frames
    

    def get_bonnie_frames(self):
        frames = []

        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Bonnie/291.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Bonnie/293.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Bonnie/294.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Bonnie/295.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Bonnie/296.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Bonnie/297.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Bonnie/298.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Bonnie/299.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Bonnie/300.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Bonnie/301.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Bonnie/303.png").convert_alpha())

        return frames

    def get_chica_frames(self):
        frames = []
        
        
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/65.png").convert_alpha()) 
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/69.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/216.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/228.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/229.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/230.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/231.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/232.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/233.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/234.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/235.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/236.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/237.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/239.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/279.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Chica/281.png").convert_alpha())
        
        return frames

    def get_foxy_frames(self):
        frames = []
        
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/242.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/243.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/396.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/397.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/398.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/399.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/400.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/401.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/402.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/403.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/404.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/405.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/406.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/407.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/408.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/409.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/410.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/411.png").convert_alpha())
        frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Jumpscares/Foxy/412.png").convert_alpha())

        
        return frames
    
    def play_jumpscare(self, screen, frames, office):
        cooldown = 20

        current_time = pygame.time.get_ticks()
        
        try:
            screen.blit(frames[self.jumpscare_frame], (office.bgx, office.bgy))

        except IndexError:
            print(self.jumpscare_frame)

        if self.jumpscare_frame >= 0:
            if current_time - self.last_updated_frame >= cooldown:
                self.jumpscare_frame += 1
                self.last_updated_frame = current_time

                if self.jumpscare_frame >= len(frames):
                    self.jumpscare_frame = -1

    def play_scream(self):
        self.scream.play()
                    

    def calculate_movement(self, current_cam, camera, door_closed):
        current_time = pygame.time.get_ticks()
        enemy_vel = ENEMY_VEL

        if current_cam == self.killcam:
            enemy_vel = enemy_vel * 2

        if current_time - self.move_timer >= enemy_vel:
            random_num = random.randint(1, 20)

            if current_cam == self.killcam and not door_closed:
                return "O"

            if random_num <= self.ai_level:
                random_cam = random.choice(self.path[current_cam])
                
                if camera.vacant_cameras[random_cam]:
                    camera.vacant_cameras[current_cam] = True

                    current_cam = random_cam

                    camera.vacant_cameras[current_cam] = False
                    

            self.move_timer = current_time

        return current_cam


    
