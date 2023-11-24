import pygame
pygame.init()

screen = pygame.display.set_mode((700,700))

RED = (255, 0, 0)
WHITE = (255, 255, 255)

x = 350
y = 350
pixel = 20
radius = 25

clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        if y - pixel >= 25:
            y -= pixel
        else:
            y = 25 
    elif pressed[pygame.K_DOWN]: 
        if y + pixel <= 675:
            y += pixel
        else:
            y = 675
    elif pressed[pygame.K_LEFT]: 
        if x - pixel >= 25:
            x -= pixel
        else:
            x = 25
    elif pressed[pygame.K_RIGHT]: 
        if x + pixel <= 675:
            x += pixel
        else:
            x = 675
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x,y), radius)

    pygame.display.flip()
    clock.tick(60)