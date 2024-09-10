import time
import pygame
import sys
import json
import math



clock = pygame.time.Clock()
TXT1 = 'Save Game [Q]'
TXT2 = 'Load Game [W]'
void_text = " "
run = pygame.image.load(r"C:\Users\itish\OneDrive\Documents\Untitled.jpg")
VVOID = "Hello there"
pluh = 0
rad = 20
rad1 = 20
rad2 = 20
IT = 0
x = 410
y = 400
z = 0
e = 1
v = 2
t = 4
o = 500
p = 1
i = 0
iT = 0
pp = 1
ppp = 1
PRICE = 100
PRICE2 = 700
PRICE3 = 2500
PRICE4 = 5000
PRICE5 = 20000
PRICE6 = 100000
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)
ee = white
txtcol = white
txtcol2 = white
txtcol3 = white
txtcol4 = black
voidtxtcol = black

pygame.init()
pygame.font.get_fonts()
font = pygame.font.Font('freesansbold.ttf', 30)
font2 = pygame.font.Font('freesansbold.ttf', 12)
font3 = pygame.font.Font('freesansbold.ttf', 15)
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("pineapple")
dialouge = [
    " ",
    "Hello",
    "i have not had a visitor in quite a while",
    "how did you end up here?",
    "well im glad that you are here",
    "ive been alone for so long",
    "its nice to have a visitor",
    "the others left me here",
    "they locked me in the void"
]



class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, width, color):
        super().__init__()
        self.radius, self.width = radius, width
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius, width)
        self.rect = self.image.get_rect(center=(x, y))

    def is_clicked(self, mouse_pos):
        return pygame.math.Vector2(self.rect.center).distance_to(mouse_pos) <= self.radius
    def render(self):
        screen.blit(self.image, self.rect.topleft)

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, width, color):
        super().__init__()
        self.radius, self.width = radius, width
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), 25, 5)
        self.rect = self.image.get_rect(center=(x, y))

    def is_clicked(self, mouse_pos):
        return pygame.math.Vector2(self.rect.center).distance_to(mouse_pos) <= self.radius

    def render(self):
        screen.blit(self.image, self.rect.topleft)

class Auto(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, width, price, color, clicker_type):
        super().__init__()
        self.radius, self.width, self.price = radius, width, price
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), 25, 5)
        self.rect = self.image.get_rect(center=(x, y))
        self.clicker_type = clicker_type

    def is_clicked(self, mouse_pos):
        return pygame.math.Vector2(self.rect.center).distance_to(mouse_pos) <= self.radius


    def render(self):
        screen.blit(self.image, self.rect.topleft)

class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\itish\Downloads\pngimg.com - square_PNG61.png")
        self.rect = self.image.get_rect(center=pygame.mouse.get_pos())

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

cooldown_tracker = pygame.time.get_ticks()
button_cooldown = 1000
last_button_press = 0
cooldown_active, cooldown_active2, cooldown_active3, cooldown_active4, runrun, cooldown_active5 = False, False, False, False, True, False

circle_group = pygame.sprite.Group()

my_circle = Circle(400, 400, 100, 20, (128, 0, 128))
my_circle2 = Circle(200, 250, 100, 20, (255, 242, 0))
my_circle3 = Circle(600, 250, 100, 20, green)
my_button = Button(100, 700, 100, 20, (128, 0, 128))
my_button2 = Button(250, 700, 100, 20, (255, 242, 0))
my_button3 = Button(400, 700, 100, 20, green)
my_clicker = Auto(750, 600, 100, 20, PRICE4, (128, 0, 128), "clicker")
my_clicker2 = Auto(750, 400, 100, 20, PRICE5, (255, 242, 0), "clicker2")
my_clicker3 = Auto(750, 200, 100, 20, PRICE6, green, "clicker3")

RUN = Button(-65, -65, 100, 20, (black))

circle_group.add(my_circle, my_button, my_button2, my_button3, my_clicker, my_clicker2, my_clicker3)
LOAD_TEXT_DURATION = 500
SAVE_TEXT_DURATION = 500
load_text_start_time = 0
save_text_start_time = 0
mouse = Mouse()


while True:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                TXT1 = 'Game Saved'
                game_state = {
                    'z': z,
                    'o': o
                }
                with open('../Data/save.json', 'w') as f:
                    json.dump(game_state, f)

                save_text_start_time = current_time
            elif event.key == pygame.K_w:
                TXT2 = 'Game Loaded'
                with open('../Data/save.json', 'r') as f:
                    game_state = json.load(f)
                    z = game_state['z']
                    o = game_state['o']

                load_text_start_time = current_time
        if event.type == pygame.MOUSEBUTTONDOWN:
            if z >= 100:
                cooldown_active4 = True
            if my_circle.is_clicked(pygame.mouse.get_pos()):
                z += e
            if my_circle2.is_clicked(pygame.mouse.get_pos()):
                z += v
            if my_circle3.is_clicked((pygame.mouse.get_pos())):
                z += t

            if my_button.is_clicked(pygame.mouse.get_pos()):
                if z >= PRICE:
                    z -= PRICE
                    PRICE += PRICE * 0.9
                    e += 1
            if my_button2.is_clicked(pygame.mouse.get_pos()):
                if z >= PRICE2:
                    z -= PRICE2
                    PRICE2 += PRICE2 * 1.2
                    v += 2
            if my_button3.is_clicked(pygame.mouse.get_pos()):
                if z >= PRICE3:
                    z -= PRICE3
                    PRICE3 += PRICE3 * 3
                    t += 3
            if my_clicker.is_clicked(pygame.mouse.get_pos()):
                if z >= PRICE4:
                    cooldown_active = True
                    my_clicker.kill()
                    txtcol = black
                    z -= PRICE4
                    rad = 0
            if my_clicker2.is_clicked(pygame.mouse.get_pos()):
                if z >= PRICE5:
                    cooldown_active2 = True
                    my_clicker2.kill()
                    txtcol2 = black
                    z -= PRICE5
            if my_clicker3.is_clicked(pygame.mouse.get_pos()):
                if z >= PRICE6:
                    cooldown_active3 = True
                    my_clicker3.kill()
                    txtcol3 = black
                    z -= PRICE6

            if RUN.is_clicked(pygame.mouse.get_pos()):
                screen.blit(run, (-550, -300))
                runrun = False
                cooldown_active5 = True

            if o <= 1900:
                if z >= o:
                    circle_group.add(my_circle2)
                    o += 900
                    if o >= 1401:
                        circle_group.add(my_circle3)
                        ee = black


            if circle_group.sprites()[3].is_clicked(pygame.mouse.get_pos()):
                z += t
            if circle_group.sprites()[2].is_clicked(pygame.mouse.get_pos()):
                z += v

    current_time = pygame.time.get_ticks()

    last_button_press = current_time
    if o == 500:
        circle_group.remove(my_circle2)
        circle_group.remove(my_circle3)
        ee = white
    if o == 1400:
        circle_group.remove(my_circle3)
        ee = white
    if runrun == True:
        screen.fill(black)
    if i == 3:
        sys.exit()
    if cooldown_active4:
        current_time = pygame.time.get_ticks()
        if current_time - last_button_press >= button_cooldown:
            iT += 1
            IT += 1
            last_button_press = current_time
    if z <= 100:
        cooldown_active4 = False
        pluh = 0
    if iT == 30:
        if pluh < 9:
            pluh += 1
            void_text = dialouge[pluh]
            voidtxtcol = white
            iT = 0
    if IT == 32:
        voidtxtcol = black
        IT = 0

    if cooldown_active:
        current_time = pygame.time.get_ticks()
        if current_time - last_button_press >= button_cooldown:
            z += e
            last_button_press = current_time
    if cooldown_active2:
        current_time = pygame.time.get_ticks()
        if current_time - last_button_press >= button_cooldown:
            z += v
            last_button_press = current_time
    if cooldown_active3:
        current_time = pygame.time.get_ticks()
        if current_time - last_button_press >= button_cooldown:
            z += t
            last_button_press = current_time

    if current_time - load_text_start_time < LOAD_TEXT_DURATION:
        screen.blit(font2.render(TXT2, True, (txtcol3)), (20, 40))
    else:
        TXT2 = 'Load game [W]'
    if current_time - save_text_start_time < SAVE_TEXT_DURATION:
        screen.blit(font2.render(TXT1, True, (txtcol3)), (20, 20))
    else:
        TXT1 = 'Save game [Q]'



    circle_group.draw(screen)
    mouse.update()

    display_price = font2.render('Upgrade Price: ' + str(round(PRICE)), True, (255, 255, 255))
    screen.blit(display_price, (50, 650))
    display_price2 = font2.render('Upgrade Price: ' + str(round(PRICE2)), True, (255, 255, 255))
    screen.blit(display_price2, (200, 650))
    display_price3 = font2.render('Upgrade Price: ' + str(round(PRICE3)), True, (255, 255, 255))
    screen.blit(display_price3, (350, 650))
    display_unlock = font.render('Next Unlock: ' + str(round(o)), True, (ee))
    screen.blit(display_unlock, (290, 50))
    display_score = font.render('Echo: ' + str(round(z)), True, (255, 255, 255))
    screen.blit(display_score, (350, 100))
    display_text = font3.render('Upgrades Value: ', True, (255, 255, 255))
    screen.blit(display_text, (45, 615))
    display_text2 = font3.render('Autoclickers: ', True, (255, 255, 255))
    screen.blit(display_text2, (674, 125))
    display_aprice = font2.render(str(round(PRICE4)), True, (txtcol))
    screen.blit(display_aprice, (735, 550))
    display_aprice2 = font2.render(str(round(PRICE5)), True, (txtcol2))
    screen.blit(display_aprice2, (733, 350))
    display_aprice3 = font2.render(str(round(PRICE6)), True, (txtcol3))
    screen.blit(display_aprice3, (730, 150))
    display_instr = font2.render(TXT1, True, (txtcol3))
    screen.blit(display_instr, (20, 20))
    display_instr2 = font2.render(TXT2, True, (txtcol3))
    screen.blit(display_instr2, (20, 40))
    display_v̷o̶i̴d̸ = font2.render(void_text, True, (voidtxtcol))
    screen.blit(display_v̷o̶i̴d̸, (500, 750))

    pygame.display.flip()
    clock.tick(60)
