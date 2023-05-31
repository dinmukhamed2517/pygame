import time
import pygame
import random
import sys
pygame.init()
done = True
FPS=60
ok=True
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
Clock =pygame.time.Clock()
SPEED = 5 
COIN_SPEED = 2.5
SCORE = 0
COINS = 0 
cnt = 0
lvl =1
Font = pygame.font.SysFont("Verdana",60)
font_medium = pygame.font.SysFont("Verdana",40)
font_small = pygame.font.SysFont("Verdana",20)
gv= Font.render("Game Over ",True,BLACK)
background = pygame.image.load("AnimatedStreet.png")
size= width,height =(400,600)
screen =pygame.display.set_mode(size)
screen.fill(WHITE)
pygame.display.set_caption("Racer")
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("Enemy.png")
        self.rect =self.image.get_rect()
        self.rect.center =(random.randint(40,width-40),0)
    def move(self):
        global SCORE
        self.rect.move_ip(0,COIN_SPEED)
        if(self.rect.top>600):
            SCORE += 1 
            self.rect.top =0
            self.rect.center =(random.randint(30,370),0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect =self.image.get_rect()
        self.rect.center =(160,520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left >0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right<width:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5,0)
class SmallCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin1.png")
        self.rect  =self.image.get_rect()
        self.rect.center =(random.randint(50,width-50),random.randint(100,height-100))
    def move(self):
        self.rect.move_ip(0,COIN_SPEED)
        if(self.rect.top>600):
            self.rect.top =0
            self.rect.center =(random.randint(30,width-30),0)
class BigCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin2.png")
        self.rect  =self.image.get_rect()
        self.rect.center =(random.randint(50,width-50),random.randint(100,height-100))
    def move(self):
        self.rect.move_ip(0,COIN_SPEED+1.5)
        if(self.rect.top>600):
            self.rect.top =0
            self.rect.center =(random.randint(30,width-30),0)
P1=Player()
E1=Enemy()
C1=SmallCoin()
C2=BigCoin()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins2 = pygame.sprite.Group()
coins.add(C1)
coins2.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)    
while(done):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = False
    screen.blit(background,(0,0))
    scores = font_small.render(str(SCORE),True,BLACK)
    screen.blit(scores,(10,10))
    level =font_small.render(f'lvl:{lvl}',True,BLACK)
    for entity in all_sprites:
        screen.blit(entity.image,entity.rect)
        entity.move()
    if pygame.sprite.spritecollideany(P1,enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        total_score =font_medium.render(f'Total score:{SCORE}',True,BLACK)
        total_coins =font_medium.render(f'Total coins:{COINS}',True,BLACK)
        screen.fill(RED)
        screen.blit(gv,(30,100))
        screen.blit(total_score,(40,250))
        screen.blit(total_coins,(40,350))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    if P1.rect.colliderect(C1.rect):
        pygame.mixer.Sound("coin.wav").play()
        COINS += 1
        cnt+=1
        C1.rect.center =(random.randint(30,width-30),0)
    if COINS >10:
        for entity in coins2:
            screen.blit(entity.image,entity.rect)
            entity.move() 
    if P1.rect.colliderect(C2.rect):
        pygame.mixer.Sound("coin.wav").play()
        COINS += 3
        cnt +=3
        C2.rect.center =(random.randint(30,width-30),0)
    if cnt>=7:
        lvl += 1
        SPEED += 0.5
        COIN_SPEED +=0.3        
        cnt = 0
    screen.blit(C1.image,(364,10))
    screen.blit(level,P1.rect)
    img_coin = font_small.render(str(COINS),True,YELLOW)
    screen.blit(img_coin,(370,45))
    Clock.tick(60)
    pygame.display.update()
pygame.quit()