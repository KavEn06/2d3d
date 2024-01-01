import pygame
pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("demo")
x = 0 
y = 0
direction = 0 
clock = pygame.time.Clock()

pressed = pygame.key.get_pressed()


while True:
    screen.fill((255, 255, 255))
    time = clock.tick()
    print(time)





    pygame.display.flip()
    pygame.time.delay(40)
  
