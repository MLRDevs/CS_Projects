# Alex Miller
# Pygame Basics

import pygame 

pygame.init()
screen = pygame.display.set_mode((1300, 660))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
cpu_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
cpu2_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
cpu3_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while  running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill screen with a color to wipe away anything from previous frame
    screen.fill('blue')

    # Rendering
    pygame.draw.circle(screen, "green", player_pos, 40)
    pygame.draw.circle(screen, "red", cpu_pos, 40)
    pygame.draw.circle(screen, "white", cpu2_pos, 40)
    pygame.draw.circle(screen, "black", cpu3_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        cpu_pos.y += 300 * dt
        cpu2_pos.x -= 300 * dt
        cpu3_pos.x += 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        cpu_pos.y -= 300 * dt
        cpu2_pos.x += 300 * dt
        cpu3_pos.x -= 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        cpu_pos.x += 300 * dt
        cpu2_pos.y -= 300 * dt
        cpu3_pos.y += 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        cpu_pos.x -= 300 * dt
        cpu2_pos.y += 300 * dt
        cpu3_pos.y -= 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # dt is delta time in seconds since last frame
    dt = clock.tick(60) / 1000

    #clock.tick(60) # 60 FPS limit

pygame.quit() # end program
