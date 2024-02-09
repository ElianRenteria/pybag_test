import pygame

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speedx = 20
        self.speedy = -10
        self.gravity = 1
        self.size = size
        self.color = color
        self.lifespan = 5
        self.maxlifespan = 10
        self.fading = False
        self.fade = 2
        self.fade_speed = 3
        self.fade_color = (255, 0, 0)
        self.fade_size = 0
        self.fade_size_speed = 3
        self.fading_size = False
        self.fading_color = False
        self.fading_size_speed = .5
        self.fading_color_speed = 2
        self.fade_color_speed = (0, 255, 0)

    def update(self):
        self.speedy += self.gravity
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.lifespan += 1
        if self.fading:
            self.fade += self.fade_speed
            self.image.fill((self.color[0]+self.fade_color[0]*self.fade, self.color[1]+self.fade * self.fade_color[1], self.color[2]+self.fade*self.fade_color[2]))
        if self.fading_size:
            self.fade_size += self.fade_size_speed
            self.image = pygame.Surface((self.size+self.fade_size, self.size+self.fade_size))
            self.image.fill((self.color[0], self.color[1], self.color[2]))
            self.rect = self.image.get_rect()
            self.rect.center = (self.rect.x, self.rect.y)
        if self.fading_color:
            self.fade_color += self.fade_color_speed
