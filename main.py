import os
import random
import pygame
import neat
import time
#Defining window resolution
WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS=[pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird2.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird3.png")))]
PIP_IMG=pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")))
BASE_IMG=pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))
BG_IMG=pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))

class Bird:
    IMGS= BIRD_IMGS
    MAX_ROTATION = 25 #degrees of tilting of bird
    ROT_VEL=20 # rotation of frame with bird movement
    ANIMATION_TIME=5

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.tilt=0
        self.tick_count=0
        self.vel=0
        self.height=self.y
        self.img_count=0 #we know which image we showing for bird to animate it
        self.img=self.IMGS[0]

    def jump(self):
        self.vel=-10.5
        self.tick_count=0 #track when we last jumped
        self.height=self.y #where bird jumped from 

    def move(self):
        self.tick_count+=1

        d = self.vel*self.tick_count+1.5*self.tick_count**2 #Displacement up or down for our bird

        if d>=16: #Our terminal velocity
            d = 16
        if d<0: #Jump height
            d-=2    
        self.y=self.y + d

        if d<0 or self.y<self.height+50:
            if self.tilt<self.MAX_ROTATION:
                self.tilt=self.MAX_ROTATION
        else:
            if self.tilt>-90:
                self.tilt -=self.ROT_VEL
    def draw(self,win): #Showing Flappy Bird images based on condition and animating them
        self.img_count+=1

        if self.img_count<self.ANIMATION_TIME:
            self.img=self.IMGS[0]
        elif self.img_count<self.ANIMATION_TIME*2:
            self.img=self.IMGS[1]
        elif self.img_count<self.ANIMATION_TIME*3:
            self.img=self.IMGS[2]    
        elif self.img_count<self.ANIMATION_TIME*4:
            self.img=self.IMGS[1]
        elif self.img_count==self.ANIMATION_TIME*4+1:
            self.img=self.IMGS[0]
            self.img_count=0

        if self.tilt<=-180: #Not flapping when going down
            self.img=self.IMGS[1]
            self.img_count=self.ANIMATION_TIME*2        
while True:#we kinda specifying fps here ,well its also kind of gameloop
    bird.move()
