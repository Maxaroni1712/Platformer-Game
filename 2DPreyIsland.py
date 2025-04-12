import pygame

pygame.init()

gamedisplay = pygame.display.set_mode((900,450))
red = (255,0,0)
brown = (165,42,42)
running = True
#player = pygame.draw.rect(gameisplay,red,(100,100,75,100))
player = pygame.Rect(400,200,50,75)
ground = pygame.image.load("Images/platform-removebg-preview.png")
ground = pygame.transform.scale(ground,(10000,1000))
ground_rect = pygame.Rect(-500,350,10000,125)
ground_rect.x = -5000
ground_rect.y = 350
# sky = pygame.image.load("Images/")
# sky =   pygame.transform.scale(900,450)
gravity = 2
jumping_force = 8
player_velocity_y = 0
on_ground = True
jumps = 1
clock = pygame.time.Clock()
add_jump = False

while running:
    #print(jumps)
    #print(add_jump)
    print(on_ground)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.x -= 10
    
    if keys[pygame.K_d]:
        player.x += 10

    if keys[pygame.K_SPACE] and jumps > 0:
        add_jump = True
        player_velocity_y = 20
        on_ground = False

    if add_jump:
        jumps -= 1
        add_jump = False
    #apply gravity
    #print(player_velocity_y, player.y)
    player_velocity_y -= gravity
    player.y -= player_velocity_y

    #collision with ground

    if player.colliderect(ground_rect):
        player.y = 275
        player_velocity_y = 0
        jumps = 1
        on_ground = True
    

    gamedisplay.fill((0,0,0))
    #gamedisplay.blit(sky,(0,0))
    pygame.draw.rect(gamedisplay,red,player)
    pygame.draw.rect(gamedisplay,red,ground_rect)
    gamedisplay.blit(ground,(-500,-75))

    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)