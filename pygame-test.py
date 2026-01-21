import pygame

SCREEN_WIDTH = 980
SCREEN_HEIGHT = 680

def get_frames():
    frames = []

    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/105.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/89.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/91.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/92.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/93.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/94.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/96.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/97.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/98.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/99.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/100.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/101.png").convert_alpha())
    frames.append(pygame.image.load("assets/FNaF 1 Placeholders/Office/Door & Lights/L. Door/102.png").convert_alpha())

    return frames

def play_animation(screen, frames, frame=0, last_updated=pygame.time.get_ticks(), reverse=False):
    cooldown = 50
    
    current_time = pygame.time.get_ticks()
    
    if not reverse:
        if frame >= 0:
            if current_time - last_updated >= cooldown:
                frame += 1
                last_updated = current_time
        
                if frame >= len(frames):
                    frame = -1

    else:
        if frame <= -1:
            if current_time - last_updated >= cooldown:
                frame -= 1
                last_updated = current_time

            if frame <= -len(frames):
                frame = 0


    screen.blit(frames[frame], (0, 0))

    return frame, last_updated


def main():
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run = True
    
    frame = 0
    frames = get_frames()
    last_updated = pygame.time.get_ticks()

    door_closed = False

    while run:
        screen.fill((255, 10, 120))
    
        #frame, last_updated = play_animation(screen, frames, frame, last_updated)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    door_closed = not door_closed


        if door_closed:
            frame, last_updated = play_animation(screen, frames, frame, last_updated, reverse=False)

        else:
            frame, last_updated = play_animation(screen, frames, frame, last_updated, reverse=True)



        pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    main()
