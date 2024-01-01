import pygame

#setup display
pygame.init()
screen = pygame.display.set_mode((1280, 720))

#setup physics
clock = pygame.time.Clock()
dTime = 0
gravity = 1000
grounded = False

#setup player
player_pos = pygame.math.Vector2(0,
                                 screen.get_height() / 2)
player_size = pygame.math.Vector2(50, 50)
player_velocity = pygame.math.Vector2(0,0)
player_shape = pygame.Rect(player_pos.x, player_pos.y, player_size.x,
  player_size.y)
player_velocity.x = 100
player_velocity.y = 0

#setup ground
ground = pygame.Rect(0, screen.get_height() - 100, screen.get_width(), 100)

#3D Loop 
threeD = False

while threeD:
    #Event Handler
    #Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            threeD = False

    #Time 
    dTime = clock.tick(60) / 1000  #clock.tick returns ms since last call

    #Inputs 
    player_velocity.x = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] & grounded:
        player_velocity.y = -750
        grounded = False
    if keys[pygame.K_a]:
        player_velocity.x = -400
    if keys[pygame.K_d]:
        player_velocity.x = 400

    #Gravity 
    player_velocity.y = player_velocity.y + (gravity * dTime * 1.85)

    #Postion Updating 
    player_shape.x += int(player_velocity.x * dTime)
    player_shape.y += int(player_velocity.y * dTime)

    #Collision Checking 
    collide = player_shape.colliderect(ground)
    if collide:
        player_shape.y = ground.y - int(player_size.y)
        player_velocity.y = 0
        grounded = True

    #Update Screen 
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), player_shape)
    pygame.draw.rect(screen, (100, 100, 100), ground)

    pygame.display.update()

#2D Loop 
twoD = True 

while twoD: 
    #Event Handler
    #Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            threeD = False

    #Time 
    dTime = clock.tick(60) / 1000  #clock.tick returns ms since last call

    #Inputs 
    player_velocity.x = 0
    player_velocity.y = 0 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_velocity.y = -450
    if keys[pygame.K_s]: 
        player_velocity.y = 450
    if keys[pygame.K_a]:
        player_velocity.x = -450
    if keys[pygame.K_d]:
        player_velocity.x = 450

    #Postion Updating 
    player_shape.x += int(player_velocity.x * dTime)
    player_shape.y += int(player_velocity.y * dTime)

    #Collision 
    collide = player_shape.colliderect(ground)
    if collide:
        player_shape.y = ground.y - int(player_size.y)
    
    #Update Screen 
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), player_shape)
    pygame.draw.rect(screen, (100, 100, 100), ground)

    pygame.display.update()