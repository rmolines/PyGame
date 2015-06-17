import pygame, math, sys
from pygame.locals import *

screen = pygame.display.set_mode((960, 640))

clock = pygame.time.Clock()

def load_image(name):
    image = pygame.image.load(name)
    return image

class BallSprite(pygame.sprite.Sprite):

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.position = position
        self.yspeed = 0
        self.index = 0
        self.tick = 0
        self.jump = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0
        self.load_animation()

    def load_animation (self):
        self.images = []
        self.images.append(load_image('font01_a.png'))
        self.images.append(load_image('font02_b.png'))
        self.images.append(load_image('font03_c.png'))
        self.images.append(load_image('font04_d.png'))
        self.images.append(load_image('font05_e.png'))
        self.images.append(load_image('font06_f.png'))
        self.images.append(load_image('font07_g.png'))
        self.images.append(load_image('font08_h.png'))

    def update(self):

        if self.jump == 1:
            self.yspeed = -15
            self.jump = 0

        x, y = self.position
        y += self.yspeed
        self.tick += 1
        if self.tick % 5 == 0: self.index += 1
        if self.index >= len(self.images): self.index = 0
        self.position = (x, y)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        if y < 568: self.yspeed += 1
        else: self.yspeed = 0


class Obstacle (pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.position = (1000, 100)
        self.image = load_image(image)
        self.yspeed = 10
        self.acceleration = 1
        self.image = pygame.transform.scale(self.image, (60, 60))

    def update (self):
        x, y = self.position
        y += self.yspeed
        self.yspeed += self.acceleration
        if y > 600:
            self.yspeed = -self.yspeed*0.65
            if 0 > self.yspeed > -0.7:
                self.yspeed = 0
        x -= 3.5
        if x < -60:
            x = 1000
            y = 100
            self.yspeed = 10
        self.position = (x, y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position


scott = BallSprite((260, 570))
ball = Obstacle('ball.gif')
ball_group = pygame.sprite.RenderPlain(ball)
scott_group = pygame.sprite.RenderPlain(scott)


while 1:
    deltat = clock.tick(60)
    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            pass
        else:
            down = event.type == KEYDOWN
            if event.key == K_SPACE:
                if scott.position[1] > 568:
                    scott.jump = 1
            elif event.key == K_ESCAPE:
                sys.exit(0)

    screen.fill((0, 0, 0))
    scott_group.update()
    scott_group.draw(screen)
    ball_group.update()
    ball_group.draw(screen)
    pygame.display.flip()