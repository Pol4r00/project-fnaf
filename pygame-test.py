import pygame

pygame.init()

SCREEN_WIDTH = 980
SCREEN_HEIGHT = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('project-fnaf')

icon = pygame.image.load("foxy.png")
pygame.display.set_icon(icon)

office = pygame.image.load("office_ph.png")

font = pygame.font.Font(None, size=20)

cams = pygame.image.load("camera_test.png")

run = True
cams_up = False

clock = pygame.time.Clock()

x = 0
y = 0

while run:
    screen.fill((255, 10, 120))

    toggle = pygame.Rect(SCREEN_WIDTH / 3 - 250, 550, 500, 50)
    pygame.draw.rect(screen, (256, 0, 0), toggle, width=5)

    if toggle.collidepoint(pygame.mouse.get_pos()):
        cams_up = True
        while cams_up:
            screen.blit(cams, (0, 0))
            if toggle.collidepoint(pygame.mouse.get_pos()):
                cams_up = False
    else:
        screen.blit(office, (x, y))

    mx, my = pygame.mouse.get_pos()

    text_mouse = font.render(f"MOUSE: ({mx}, {my})", True, (255, 255, 255))
    text_office = font.render(f"OFFICE: ({x}, {y})", True, (255, 255, 255))

    screen.blit(text_mouse, (15, 15))
    screen.blit(text_office, (15, 35))
    
    if mx > 800:
        if x - 10 >= -550:
            x -= 10

    elif mx < 300:
        if x + 10 <= 0:
            x += 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
