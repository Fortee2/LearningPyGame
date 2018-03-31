import sys, pygame, os, gameCharacter

pygame.init()

size = width, height = 600 , 480

speed = [2,0]
xPos = [0,480]
black = 0,0,0

screen = pygame.display.set_mode(size)
path = __file__.replace("sprite_enemies.py","")

class background(pygame.sprite.Sprite):

    # init
    def __init__(self, imageName):
        pygame.sprite.Sprite.__init__(self)
        self.image  = pygame.image.load(path + "player/" + imageName)
        self.image = pygame.transform.scale(self.image, [256, 256])
        self.rect = self.image.get_rect()
        self.rect.bottom = 480
        self.rect.left = 0

    def update(self):
        self.rect.left -= 2

def PreprocessPlayerImages():

    runImages = dict()

    for i in range(8):
        img = pygame.image.load(path + "player/Run ({0}).png".format(i+1)).convert_alpha()
        img= pygame.transform.scale(img,[95,80])
        runImages.update({"{0}".format(i+1): img})

    return runImages

def PreprocessPlayerIdleImages():

    idleImages = dict()

    img = pygame.image.load(path + "player/Idle (1).png").convert_alpha()
    img= pygame.transform.scale(img,[95,80])
    idleImages.update({"1": img})

    return idleImages

def PreprocessEnemyImages():
    ghostImages = dict()

    for i in range(4):
        img = pygame.image.load(path + "ghost/Ghost_{0}.png".format(i+1)).convert_alpha()
        img= pygame.transform.scale(img,[64,64])
        ghostImages.update({"{0}".format(i+1): img})

    return ghostImages

block_n_road = background("Wall_Nodoor.png")
block_n_road2 = background("Wall_Piece.png")
block_n_road3 = background("Wall_Nodoor.png")
block_n_road4 = background("Wall_Nodoor.png")
block_n_road2.rect.left = 256
block_n_road3.rect.left = 512
block_n_road4.rect.left = 768

player_one = gameCharacter.player(path)
player_one.runImages.update( PreprocessPlayerImages())
player_one.idleImages.update(PreprocessPlayerIdleImages())

ghost = gameCharacter.player(path)
ghost.runImages.update(PreprocessEnemyImages())
ghost.xPosition = 600
ghost.speed = -2
ghost.State = gameCharacter.playerState.WALKING

background_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

background_group.add(block_n_road)
background_group.add (block_n_road2)
background_group.add (block_n_road3)
background_group.add (block_n_road4)

player_group.add(player_one)
enemies_group.add(ghost)

while 1:
    #Returns all of the events that have queued up since last time we were here.
    for event in pygame.event.get():
        player_one.speed= 0
        player_one.State = gameCharacter.playerState.STANDING
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_one.speed = -2
                player_one.State = gameCharacter.playerState.WALKING
            if event.key == pygame.K_RIGHT:
                player_one.speed = 2
                player_one.State = gameCharacter.playerState.WALKING

    player_group.update()
    enemies_group.update()

    if player_one.rect.left > width/2:
        player_one.speed = 0
        background_group.update()
        if block_n_road.rect.right < 0:
            block_n_road.rect.left = block_n_road4.rect.right
        if block_n_road2.rect.right < 0:
            block_n_road2.rect.left = block_n_road.rect.right
        if block_n_road3.rect.right < 0:
            block_n_road3.rect.left = block_n_road2.rect.right
        if block_n_road4.rect.right < 0:
            block_n_road4.rect.left = block_n_road3.rect.right

    if player_one.rect != None:
        pygame.sprite.spritecollide(player_one, enemies_group,True)

    screen.fill(black)
    background_group.draw(screen)
    player_group.draw(screen)
    enemies_group.draw(screen)

    pygame.display.flip()
    pygame.time.delay(100)
