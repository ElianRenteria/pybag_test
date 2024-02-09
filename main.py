import pygame
from player import Player
from animations import bg
from particle import Particle

root = pygame.display.set_mode((1920, 930))
pygame.display.set_caption("Game3")
def draw():
    root.blit(bg, (0, 0))
    if player.alive:
        player.update(root)
    if player.attacking:
        if player.direction == "Right":
            parties.add(Particle(player.x+player.rect.width, player.y+player.rect.height/2, (255, 0, 0), 10))
        else:
            parties.add(Particle(player.x, player.y+player.rect.height/2, (255, 0, 0), 10))
        player.attacking = False
    parties.update()
    parties.draw(root)
    if not player.alive:
        parties.empty()
        player.animation = "Die"
        player.update(root)


player = Player()
parties = pygame.sprite.Group()
clock = pygame.time.Clock()
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw()
    pygame.display.update()
