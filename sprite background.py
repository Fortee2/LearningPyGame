import sys, pygame, os

pygame.init()

size = width, height = 600 , 480

speed = [2,0]
xPos = [0,480]
black = 0,0,0

screen = pygame.display.set_mode(size)
path = __file__.replace("sprite background.py","player/")

class obstacle(pygame.sprite.Sprite):
    # init
    def __init__(self, imageName):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load(path + imageName)
        self.image = pygame.transform.scale(self.image, [256, 256])
        self.rect = self.image.get_rect()
        self.rect.bottom = 480
        self.rect.left = 0

class player(pygame.sprite.Sprite):
    animationStep = 1
    xPosition = 0

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path + "Run (1).png").convert_alpha()
        self.image = pygame.transform.scale(self.image,[95,80])
        self.rect = self.image.get_rect()

        self.rect.bottom = 480
        self.rect.left = 0

        self.animationStep = 1
        self.xPosition = 0

    def update(self):

        if self.animationStep == 8:
            self.animationStep=1
        else:
            self.animationStep = self.animationStep + 1

        ballFile = path + "Run ({0}).png".format(self.animationStep)

        #print(ballFile)

        self.xPosition += 2

        self.image  = pygame.image.load( ballFile).convert()
        self.image = pygame.transform.scale(self.image,[95,80])
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.left = self.xPosition
        self.rect.bottom = 480

block_n_road = obstacle("Wall_Nodoor.png")
block_n_road2 = obstacle("Wall_Piece.png")
block_n_road3 = obstacle("Wall_Nodoor.png")
block_n_road2.rect.left = 256
block_n_road3.rect.left = 512

player_one = player()

obstacle_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

obstacle_group.add(block_n_road)
obstacle_group.add (block_n_road2)
obstacle_group.add (block_n_road3)
player_group.add(player_one)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    obstacle_group.update()
    player_group.update()

    if player_one.rect.left > width:
        player_one.xPosition = -95 #makes sprite look like it is walking in circle

    #if player_one.rect.right > center of screen
    #   stop moving player_one
    #   start moving background to right

    screen.fill(black)
    obstacle_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()
    pygame.time.delay(100)
