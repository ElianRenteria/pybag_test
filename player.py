from animations import *


class Player:
    def __init__(self):
        self.alive = True
        self.x = 0
        self.y = 760
        self.speed = 10
        self.gravity = 10
        self.jumping = False
        self.attacking = False
        self.direction = "Right"
        self.animation = "Idle"
        self.frame = 0
        self.images = turtle
        self.rect = self.images[self.animation][self.frame].get_rect()

    def update(self, window):
        self.move()
        self.rect.x = self.x
        self.rect.y = self.y
        self.frame += 1
        if self.frame >= len(self.images[self.animation]):
            self.frame = 0
            if self.animation == "Die":
                self.alive = False
        try:
            if self.direction == "Left" and self.alive:
                window.blit(pygame.transform.flip(self.images[self.animation][self.frame], True, False), (self.x, self.y))
            elif self.alive:
                window.blit(self.images[self.animation][self.frame], (self.x, self.y))
            self.rect = self.images[self.animation][self.frame].get_rect()
        except IndexError:
            print("IndexError")
    def move(self):
        if self.animation != "Die":
            user_input = pygame.key.get_pressed()
            if user_input[pygame.K_a]:
                self.animation = "Walk"
                self.direction = "Left"
                self.x -= self.speed
            elif user_input[pygame.K_d]:
                self.animation = "Walk"
                self.direction = "Right"
                self.x += self.speed
            elif not self.jumping and not self.attacking:
                self.animation = "Idle"
            if user_input[pygame.K_SPACE] and not user_input[pygame.K_d] and not user_input[pygame.K_a]:
                self.attacking = True
                self.frame = 0
            if user_input[pygame.K_w] and not self.jumping and not user_input[pygame.K_e]:
                self.gravity = 10
                self.jumping = True
                self.frame = 0
            if self.jumping and not self.attacking:
                self.animation = "Roll"
                self.y -= self.gravity*self.speed/3
                self.gravity -= 1
                if self.gravity < -10:
                    self.jumping = False
                    self.gravity = 10
            if user_input[pygame.K_s] and not self.jumping and not self.attacking:
                self.animation = "Glide"
                self.speed = 20
            else:
                self.speed = 10
            if self.attacking and not user_input[pygame.K_s]:
                self.animation = "Throw"
                if self.frame == 21:
                    self.attacking = False
            if user_input[pygame.K_q]:
                self.animation = "Celebrate"
            if not self.jumping and self.y < 760 and not user_input[pygame.K_e]:
                self.y += self.gravity*.8
                self.gravity += 1
                self.animation = "Fall"
            elif self.y >= 760:
                self.y = 760
                if self.gravity > 40:
                    self.animation = "Die"
                    self.frame = 0
                self.gravity = 10
            if user_input[pygame.K_e] and not self.jumping and not self.attacking:
                self.animation = "Fly"
                self.y -= self.gravity