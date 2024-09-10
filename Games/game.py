import pygame, sys, time, random
from pygame.locals import *
import math
when = False
t = 1
k = 500
u = 1
o = 3
z = 0
rsed1, rsed2 = 800, 800
CameraX, CameraY = 0, 0
Cx, Cy = 411 - CameraX, 406 - CameraY
Tx, Ty = 500 - CameraX, 406 - CameraY
x, y = 410, 400
my_coords = x, y
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)
width = 800
height = 800
r = 0
pygame.init()
arrows = pygame.image.load("C:/Users\itish\Downloads\pixel-art-video-game-direction-arrow-button-direction-key-icon-for-8bit-game-on-white-background-vector-removebg-preview.png")
clock = pygame.time.Clock()
pygame.display.set_caption("i dont know what to call this and im tired so be happy and make stuff")
screen = pygame.display.set_mode((width, height))
rect = pygame.Rect(*screen.get_rect().center, 0, 0).inflate(5, 5)
font = pygame.font.Font('freesansbold.ttf', 12)
background = pygame.image.load("C:/Users\itish\Downloads/night-sky-with-stars-sparkling-on-black-background-free-photo.jpg")
background2 = pygame.image.load("C:/Users\itish\Downloads/night-sky-with-stars-sparkling-on-black-background-free-photo.jpg")
current_time = pygame.time.get_ticks()


def lerp_color(colors, value):
    fract, index = math.modf(value)
    color1 = pygame.Color(colors[int(index) % len(colors)])
    color2 = pygame.Color(colors[int(index + 1) % len(colors)])
    return color1.lerp(color2, fract)
start_time = pygame.time.get_ticks()

cooldown_tracker = 0

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("C:/Users/itish/Downloads/New Piskel(7).png")
        self.rect = self.image.get_rect(center=(x, y))

    def update(self, CameraX, CameraY):
        self.rect.center = x - CameraX, y - CameraY

    def render(self):
        screen.blit(self.player, self.rect)




my_player = Player(x - CameraX, y - CameraY)
player_group = pygame.sprite.Group()
player_group.add(my_player)
value = (pygame.time.get_ticks() - start_time) / 1500

button_cooldown = 1000  # Cooldown time in milliseconds
last_button_press = 0

moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = o
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()

    if x > width - 50:
        CameraX += o
        width += o
    if y > height - 50:
        CameraY += o
        height += o
    if x < width - 750:
        CameraX += -o
        width += -o
    if y < height - 750:
        CameraY += -o
        height += -o

    if x > 900:
        x = 899
    if x < -100:
        x = -99
    if y < -100:
        y = -99
    if y > 900:
        y = 899

        """if keys[pygame.K_q]:
            current_time = pygame.time.get_ticks()
            if current_time - last_button_press >= button_cooldown:
                if z >= u:
                    o += 0.01
                    z -= u
                    u += u * 2
                    urth * 2
                    last_button_press = current_time"""



    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            moveRight = False
            moveLeft = True
        if event.key == K_RIGHT:
            moveLeft = False
            moveRight = True
        if event.key == K_UP:
            moveDown = False
            moveUp = True
        if event.key == K_DOWN:
            moveUp = False
            moveDown = True
    if event.type == KEYUP:
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.key == K_LEFT:
            moveLeft = False
            CameraX, CameraY + x, y
        if event.key == K_RIGHT:
            moveRight = False
            CameraX, CameraY + x, y
        if event.key == K_UP:
            moveUp = False
            CameraX, CameraY + x, y
        if event.key == K_DOWN:
            moveDown = False
            CameraX, CameraY + x, y
    if keys[pygame.K_r]:
        width, height, CameraX, CameraY, x, y = 800, 800, 0, 0, 410, 400


    if moveDown:
        y += MOVESPEED
    if moveUp:
        y -= MOVESPEED
    if moveLeft:
        x -= MOVESPEED
    if moveRight:
        x += MOVESPEED



    colors = ["white", "black"]
    value = (pygame.time.get_ticks() - start_time) / 1500
    current_color = lerp_color(colors, value)

    screen.blit(background, (-200 - CameraX, -70 - CameraY))
    screen.blit(background2, (-200 - CameraX, -1050 - CameraY))
    player_group.update(CameraX, CameraY)
    player_group.draw(screen)

    pygame.draw.rect(screen, current_color, (-212 - CameraX, -208 - CameraY, 1226, 1220), 100)

    pygame.display.flip()

    pygame.display.update()
    screen.fill((r, 0, 0))
    clock.tick(60)

