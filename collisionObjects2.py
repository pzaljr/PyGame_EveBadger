""" collisionObjects2.py
    A class library of objects used in the collision demos
    in chapter 6, stolen and ripped apart by Pete Z"""
    
import pygame, random

class Squeaker(pygame.sprite.Sprite):
    def __init__(self, screen, imageSqueak):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageSqueak)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())
        #create sound
        self.gameSqueak = pygame.mixer.Sound("sound/pop.wav")
    def squeakerMusic(self):
        self.gameSqueak.play()
        

class Circle(pygame.sprite.Sprite):
    """ makes a hookshot that 
        follows the mouse. """
        
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/hookshot.gif')
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
