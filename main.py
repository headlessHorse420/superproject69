import pygame

pygame.init()

WHITE = (255, 255, 255)

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
image = pygame.image.load('mario.png')
image = pygame.transform.scale(image, (920/4, 920/4))

game_is_running = True
while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
    window.blit(image, ((window.get_rect().centerx)-115, (window.get_rect().centery)-115))

    pygame.display.update()
pygame.quit()