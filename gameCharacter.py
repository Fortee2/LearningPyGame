import sys, pygame
from enum import Enum

class playerState(Enum):
    STANDING = 1
    WALKING = 2
    JUMPING = 3
    DYING =4
    ATTACKING = 5

class player(pygame.sprite.Sprite):


    def __init__(self,PathtoAssets):
        pygame.sprite.Sprite.__init__(self) #Intialize Pygame sprite base class
        self.assetPath = PathtoAssets #set the path where our images are found
        self.animationStep = 1 #Where we are in the action animation
        self.xPosition = 0 #where the player sprite is on the screen
        self.assetPath ="/" #path where image assests can be found
        self.runImages = dict() #A list of sprites for making the running animation
        self.idleImages = dict()
        self.speed = 0 #Positive Speed is moving right, Negative is moving right
        self.rect = None
        self.State = playerState.STANDING

        self.animationStep = 1 #first step in any animation
        self.xPosition = 2 #start on the left side of the screen

    def update(self):
        #Different characters will have a different number of images in their animations
        #We want to cycle through whatever is in the array
        if self.animationStep == len(self.runImages):
            self.animationStep = 1
        else:
            self.animationStep = self.animationStep + 1

        #Move the character based on Speed
        self.xPosition += self.speed
        if self.State == playerState.STANDING:
            self.animationStep == 0
            self.speed == 0
            self.image = self.idleImages["1"]
        else:
            #Retrieve the next animation image
            if self.speed >= 0: #All of the images are facing right.  We flip them if moving left
                self.image = self.runImages[self.animationStep.__str__()]
            elif self.speed <0:
                self.image = pygame.transform.flip(self.runImages[self.animationStep.__str__()],True, False)

        #Set the transparancey color
        self.image.set_colorkey((0,0,0))
        #create a rectangle around the image
        self.rect = self.image.get_rect()
        #move the rectangle
        self.rect.left = self.xPosition
        #this is the floor in the game.  hard coded for now
        self.rect.bottom = 480
