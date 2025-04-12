import pygame
import time

pygame.init()

# Set up the display
gamedisplay = pygame.display.set_mode((900, 450))
pygame.display.set_caption("Health Display Fix")

# Colors
red = (255, 0, 0)
brown = (165, 42, 42)
white = (225, 225, 225)

# Font
font = pygame.font.SysFont(None, 36)
font2 = pygame.font.SysFont(None, 150)

# Player setup
player = pygame.Rect(400, 200, 50, 75)
player_health = 100

# Ground setup
ground = pygame.image.load("Images/platform-removebg-preview.png")
ground = pygame.transform.scale(ground, (10000, 1000))
ground_rect = pygame.Rect(-5000, 350, 10000, 125)

# Background
sky = pygame.image.load("Images/bg.png")
sky = pygame.transform.scale(sky, (900, 450))

# Enemy setup
enemy_1 = pygame.Rect(700, 275, 50, 75)

# Physics and state variables
gravity = 2
jumping_force = 8
player_velocity_y = 0
on_ground = True
jumps = 1
clock = pygame.time.Clock()
add_jump = False
player_disabled = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and not player_disabled:
        player.x -= 10

    if keys[pygame.K_d] and not player_disabled:
        player.x += 10

    if keys[pygame.K_SPACE] and jumps > 0 and not player_disabled:
        add_jump = True
        player_velocity_y = 20
        on_ground = False

    if add_jump:
        jumps -= 1
        add_jump = False

    # Apply gravity
    player_velocity_y -= gravity
    player.y -= player_velocity_y

    # Collision with ground
    if player.colliderect(ground_rect):
        player.y = 275
        player_velocity_y = 0
        jumps = 1
        on_ground = True

    # Collision with enemy
    if player.colliderect(enemy_1):
        player_health -= 10
        player_velocity_y = 10
        for i in range(15):
            player.x -= 10
            player_disabled = True
        player_disabled = False  # Re-enable player after knockback

    # Update health text display inside the loop
    playerhealthdisplay = font.render(f"Health: {player_health}", True, white)
    gameoverdisplay = font2.render(f"GAME OVER", True, red)

    # Drawing
    gamedisplay.fill((0, 0, 0))
    gamedisplay.blit(sky, (0, 0))
    pygame.draw.rect(gamedisplay, red, player)
    pygame.draw.rect(gamedisplay, brown, enemy_1)
    pygame.draw.rect(gamedisplay, red, ground_rect)
    gamedisplay.blit(ground, (-500, -75))
    gamedisplay.blit(playerhealthdisplay, (10, 10))
    if player_health <= 0:
        gamedisplay.blit(gameoverdisplay, (150,150))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
