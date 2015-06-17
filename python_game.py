import sys, pygame


def load_image(name):
    image = pygame.image.load(name)
    return image

class Sprite (pygame.sprite.Sprite):
    def __init__(self):
        super(Sprite, self).__init__()
        self.images = []
        self.images.append(load_image('font01_a.png' ))
        self.images.append(load_image('font02_b.png' ))
        self.images.append(load_image('font03_c.png' ))

        self.index = 0
        self.image = self.images[self.index]

        self.position = [50, 50]

        def update(self):
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = pygame.transform.rotate(self.images[self.index], 0)
            self.rect = self.image.get_rect()
            self.rect.center = self.position

def main ():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))

    my_sprite = Sprite()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        my_group.update()
        my_group.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
