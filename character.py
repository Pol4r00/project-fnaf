import pygame
import random

class Character():

    def __init__(self, character_num, ai_level):

        self.character_num = character_num
        self.ai_level = ai_level
        self.timer = pygame.time.get_ticks()
        
        if self.character_num == 0:

            self.path = {

                    '1a': ['1b'],
                    '1b': ['7'],
                    '7': ['6'],
                    '6': ['4a'],
                    '4a': ['4b'],
                    '4b': ['K'],
                    'K': ['1b']
            }

            self.starting_cam = "1a"
            self.character_name = "Freddy"
                    
        if self.character_num == 1:

            self.path = {

                        '1a': ['1b', '5'],
                        '1b': ['5', '2a', '3'],
                        '5': ['1b', '2a', '3'],
                        '3': ['2a', '1b', '5'],
                        '2a': ['2b', '3', '1b', '5'],
                        '2b': ['3', 'K'],
                        'K': ['1b', '5'],
                
                    }

            
            self.starting_cam = "1a"
            self.character_name = "Bonnie"

        if self.character_num == 2:
            
            self.path = {

                    '1a': ['1b'],
                    '1b': ['7'],
                    '7' : ['1b', '6'],
                    '6': ['7', '4a'],
                    '4a': ['4b'],
                    '4b': ['4a', 'K'],
                    'K': ['1b', '7']

                }

            self.starting_cam = "1a"
            self.character_name = "Chica"
        
        if self.character_num == 3:

            self.path = {

                    '1c (1)': ['1c (2)'],
                    '1c (2)': ['1c (3)'],
                    '1c (3)': ['K'],
                    'K': ['1c (1)']

                }

            self.starting_cam = "1c (1)"
            self.character_name = "Foxy"

    def calculate_movement(self, current_cam):
        current_time = pygame.time.get_ticks()

        if current_time - self.timer >= 5000:
            print(f"{self.character_name}: Cam {current_cam}")
            random_num = random.randint(1, 20)

            if random_num <= self.ai_level:
                random_cam = random.choice(self.path[current_cam])
                current_cam = random_cam

            self.timer = current_time

        return current_cam

