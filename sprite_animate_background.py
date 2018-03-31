import sys, pygame, os

pygame.init()

size = width, height = 600 , 480

speed = [2,0]
xPos = [0,480]
black = 0,0,0

screen = pygame.display.set_mode(size)
path = __file__.replace("sprite_animate_background.py","player/")

class obstacle(pygame.sprite.Sprite):

    # init
    def __init__(self, imageName):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load(path + imageName)
        self.image = pygame.transform.scale(self.image, [256, 256])
        self.rect = self.image.get_rect()
        self.rect.bottom = 480
        self.rect.left = 0

    def update(self):
        self.rect.left -= 2

class player(pygame.sprite.Sprite):
    animationStep = 1
    xPosition = 0
    assetPath ="/"
    runImages = dict()
    speed = 2

    def __init__(self,PathtoAssets):
        pygame.sprite.Sprite.__init__(self)
        self.assetPath = PathtoAssets

        self.__preprocessImages()
        self.image = pygame.image.load(path + "Run (1).png").convert_alpha()
        self.image = pygame.transform.scale(self.image,[95,80])
        self.rect = self.image.get_rect()

        self.rect.bottom = 480
        self.rect.left = 0

        self.animationStep = 1
        self.xPosition = 0

    def __preprocessImages(self):

        img = pygame.image.load(self.assetPath + "Run (1).png").convert_alpha()
        img= pygame.transform.scale(img,[95,80])
        self.runImages.update({"1": img})

        img = pygame.image.load(self.assetPath + "Run (2).png").convert_alpha()
        img= pygame.transform.scale(img,[95,80])
        self.runImages.update({"2": img})

        img = pygame.image.load(self.assetPath + "Run (3).png").convert_alpha()
        img= pygame.transform.scale(img,[95,80])
        self.runImages.update({"3": img})

        img = pygame.image.load(self.assetPath + "Run (4).png").convert_alpha()
        img= pygame.transform.scale(img,[95,80])
        self.runImages.update({"4": img})

        img = pygame.image.load(self.assetPath + "Run (5).png").convert_alpha()
        img= pygame.transform.scale(img,[95,80])
        self.runImages.update({"5": img})

        img = pygame.image.load(self.assetPath + "Run (6).png").convert_alpha()
        img= pygame.transform.scale(img,[95,80])
        self.runImages.update({"6": img})

        img = pygame.image.load(self.assetPath + "Run (7).png").convert_alpha()
        img= pygame.transform.scale(img,[95,80])
        self.runImages.update({"7": img})

        img = pygame.image.load(self.assetPath + "Run (8).png").convert_alpha()
        img= pygame.transform.scale(img,[95,80])
        self.runImages.update({"8": img})

    def update(self):

        if self.animationStep == 8:
            self.animationStep=1
        else:
            self.animationStep = self.animationStep + 1

        self.xPosition += self.speed

        self.image = self.runImages[self.animationStep.__str__()]
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.left = self.xPosition
        self.rect.bottom = 480

block_n_road = obstacle("Wall_Nodoor.png")
block_n_road2 = obstacle("Wall_Piece.png")
block_n_road3 = obstacle("Wall_Nodoor.png")
block_n_road4 = obstacle("Wall_Nodoor.png")
block_n_road2.rect.left = 256
block_n_road3.rect.left = 512
block_n_road4.rect.left = 768

player_one = player(path)

obstacle_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

obstacle_group.add(block_n_road)
obstacle_group.add (block_n_road2)
obstacle_group.add (block_n_road3)
obstacle_group.add (block_n_road4)
player_group.add(player_one)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    player_group.update()

    if player_one.rect.left > width/2:
        player_one.speed = 0
        obstacle_group.update()
        if block_n_road.rect.right < 0:
            block_n_road.rect.left = block_n_road4.rect.right
        if block_n_road2.rect.right < 0:
            block_n_road2.rect.left = block_n_road.rect.right
        if block_n_road3.rect.right < 0:
            block_n_road3.rect.left = block_n_road2.rect.right
        if block_n_road4.rect.right < 0:
            block_n_road4.rect.left = block_n_road3.rect.right 

    screen.fill(black)
    obstacle_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()
    pygame.time.delay(100)
