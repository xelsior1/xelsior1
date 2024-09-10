import pygame, sys, random
y = 500

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
    def shoot(self):
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, y]
    def new(self):
        target_group.add(new_target)
        target_group.draw(screen)

pygame.init()
clock = pygame.time.Clock()

screen_width = 1100
screen_hight = 800
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.mouse.set_visible(False)
crosshair = Crosshair("C:/Users/itish/Downloads/New Piskel(1)(1).png")
background = pygame.image.load("C:/Users/itish/Downloads/New Piskel(5).png")

crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("C:/Users/itish/Downloads/New Piskel(2).png", random.randrange(0, screen_width), random.randrange(0, screen_hight))
    target_group.add(new_target)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()





    pygame.display.flip()
    screen.blit(background,(0, 0))
    target_group.draw(screen)
    target_group.update()
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)
