# Our libraries
import pygame, sys
from pygame.locals import *
import random, time

# Initialize 
pygame.init()

# установление частоты кадров в секунду
FPS = 60
FramePerSec = pygame.time.Clock()

# размеры экрана и скорость
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
coinscore=0

# шрифты для счета и окончания игры
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, "black") 

background = pygame.image.load("C:/Users/Admin/lab10_pp2/AnimatedStreet.png")
coin = pygame.image.load("C:/Users/Admin/lab10_pp2/coins.png"),

# Переменные для монет
coini = 0
coins = 0

# создать основную поверхность 
DISPLAYSURF = pygame.display.set_mode((400,600))
pygame.display.set_caption("Racer")

# Класс противника
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/Admin/lab10_pp2/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс Игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("C:/Users/Admin/lab10_pp2/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    # Клавишы для игрока, видеоплеер
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(7, 0)

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image=coin[coini]
        self.rect = self.image.get_rect() 
        self.rect.center = (random.randint(32, SCREEN_WIDTH-32), -31)
        self.a =random.randint(600,1000)    
    def move(self):
        global coinscore
        self.rect.move_ip(0,10)
        if self.rect.top > 600:
            self.rect.top = -62
            self.rect.center = (random.randint(32, SCREEN_WIDTH-32), -31)
        elif self.rect.colliderect(P1):
            coinscore += 1
            self.rect.top = -62
            self.rect.center = (random.randint(32, SCREEN_WIDTH-32), -31) 
      
 
# Иницилизация 
P1 = Player()
E1 = Enemy()
C1 = Coin()

# создание групп спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
Coins = pygame.sprite.Group()
Coins.add(C1)

# добавление нового пользовательского события 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 500)

# Переменные для фоновой анимации и также координаты монет
bgy = 0
coin_y =- 62
coin_x = 0
y = 0

# Музыкаааа
bgsound = pygame.mixer.Sound("C:/Users/Admin/lab10_pp2/background.wav")
bgsound.play()

#Game Loop
while True:
    # просматривает все происходящие события
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.3     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # фоон
    DISPLAYSURF.blit(background, (0,bgy))
    DISPLAYSURF.blit(background, (0,bgy-600))

    # Обновление индекса анимации монета
    if coini == 23:
       coini = 0
    else:
       coini += 1

    # Также обновление фона для анимации
    if bgy < 600:
       bgy += 7
    else:
       bgy = 0

    # Отображение результата
    scores = font_small.render(str(SCORE), True, "BLACK")
    coinscores = font_small.render(str(coinscore), True, "BLACK")
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coinscores, (360,10))

    # Перемещение и рисование всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Перемещение и рисование все монеты
    for el in Coins:
        DISPLAYSURF.blit(el.image, el.rect)
        el.move()

    # Проверим, нет ли столкновение с машинками(врагами)
    if pygame.sprite.spritecollideany(P1, enemies):
          # Остановить фоновый звук и воспроизводить звук сбоя
          bgsound.stop()    
          pygame.mixer.Sound("C:/Users/Admin/lab10_pp2/crash.wav").play()
          time.sleep(0.5)
        
        # Отображение game over screen
          DISPLAYSURF.fill("RED")
          DISPLAYSURF.blit(game_over, (30,250))
        
          pygame.display.update()

        # Удалить все спрайты из игры
          for entity in all_sprites:
                entity.kill() 
        # Подаждем, и затем выйдем из игры
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    
    # Обновление и установление частоту кадров в секунду 
    pygame.display.update()
    FramePerSec.tick(FPS)