import pygame, math, sys
from pygame.locals import *

pygame.init()

pygame.mixer.music.load("Musica1SoftDes.wav")

white = (255, 255, 255)

screen = pygame.display.set_mode((960, 640))

clock = pygame.time.Clock()

font = pygame.font.SysFont('arial black', 18)

game_speed = 7

class bg (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('sky.png')
        self.image = pygame.transform.scale(self.image, (960, 640))
        self.rect = self.image.get_rect()
        self.rect.center = screen.get_rect().center

def load_image(name):
    image = pygame.image.load(name)
    return image

class Ground (pygame.sprite.Sprite):
    def __init__(self, count):
        pygame.sprite.Sprite.__init__(self)
        self.position = (count*60+30, 610)
        self.image = load_image('tile.jpg')
        self.image = pygame.transform.scale(self.image, (100, 100))

    def update (self):
        x, y = self.position
        x -= game_speed
        self.position = (x, y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        if x-self.rect[2]/2 < -50:
            self.position = (990, 610)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.d = False
        self.k = 0
        self.life = 100
        self.yspeed = 0
        self.index = 0
        self.tick = 0
        self.jump = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0
        self.load_animation()
        self.mask = pygame.mask.from_surface(self.images[self.index])
        self.position = (280, 530)

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
        self.image = self.images[self.index]
        self.image = pygame.transform.scale(self.image, (int(self.image.get_rect()[2]*1.2), int(self.image.get_rect()[3]*1.2)))
        if self.jump == 1:
            self.e = True
            self.yspeed = -20
            scott.jump = 0
        x, y = self.position
        y += self.yspeed
        if y == 530: self.d = False
        self.tick += 1
        if self.tick % 5 == 0: self.index += 1
        if self.index >= len(self.images): self.index = 0
        self.position = (x, y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        if y < 530: self.yspeed += 1
        else: self.yspeed = 0


class Obstacle (pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)


        self.image = load_image(image)
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.position = (1100, 540)
        self.acceleration = 1
        self.mask = pygame.mask.from_surface(self.image)

    def update (self):
        x, y = self.position
        x -= game_speed
        if x < -60:
            self.kill
        self.position = (x, y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        if pygame.sprite.collide_mask(scott, self):
            scott.life -= 10
            objects.remove(self)


def GUI (text, color, position):
    GUI_text = font.render(text, 1, color)
    screen.blit(GUI_text, (position))


background = bg()
objects = pygame.sprite.LayeredUpdates()

objects.add(background)
scott = Player()
ground_list = []
for i in range(0, 17):
    g = Ground(i)
    ground_list.append(g)
    objects.add(g)
objects.add(scott)

listamusica=[]
import time
temp1 = time.time()
temp3 = 0
while temp3 <= 147 :# tempo total da musica
    if temp3 < 28 and temp3%5==0: listamusica.append(temp3)
    elif temp3 < 92 and temp3 > 30 and temp3 % 4 == 0: listamusica.append(temp3)
    elif temp3 < 110 and temp3 % 3 == 0: listamusica.append(temp3)
    temp3 += 1

seconds = 0
tempo = 0
ob = 0
tree_list = []
menu = True
music = False
while 1:
    while menu:
        deltat = clock.tick(60)
        play = GUI('Press ENTER to PLAY', white, (360,300))
        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                pass
            else:
                if event.key == K_ESCAPE:
                    sys.exit(0)
                elif event.key == K_RETURN:
                    menu = False
        pygame.display.flip()

    if scott.life == 0:
        lose = True
        while lose:
            delt = clock.tick(60)
            GUI('YOU LOSE', white, (400, 300))
            GUI ('Press ESC to exit, or ENTER to play again', white, (230, 350))
            pygame.display.flip()
            for event in pygame.event.get():
                if not hasattr(event, 'key'):
                    pass
                else:
                    down = event.type == KEYDOWN
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                    elif event.key == K_RETURN:
                        scott.life = 100
                        seconds = 0
                        tree_list = []

                        lose = False

    delta = clock.tick(60)
    if not music:
        pygame.mixer.music.play(0)
        music = True
    tempo += 1
    for event in pygame.event.get():
        if not hasattr(event, 'key'):
            pass
        else:
            down = event.type == KEYDOWN
            if event.key == K_SPACE:
                if scott.position[1] >= 530:
                    if not scott.d:
                        scott.jump = 1

            elif event.key == K_ESCAPE:
                sys.exit(0)
    if tempo % 60 == 0:
        seconds += 1
    if listamusica[ob] == seconds:
        ob+=1
        tree = Obstacle('tree.png')
        tree_list.append (tree)
        objects.add(tree)

    screen.fill((0, 0, 0))

    objects.update()
    objects.draw(screen)
    GUI('Life: %d' %(scott.life), white, (50,50))
    xpos = 0
    xpos += 3
    pygame.display.flip()