""" badger1.py
    (adapted from hardestGame.py)
    just setting up the game level """

import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))

class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((24, 24))
        self.image = self.image.convert()
        self.image.fill((255, 0, 0))
        pygame.draw.rect(self.image,(0,0,0),(0,0,24,24),5)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 240

        
    
def main():
    pygame.display.set_caption("Badger Badger Badger - MUSHROOM!")
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    drawLevel(background)
    background = pygame.image.load('img/back1.jpeg')
    screen.blit(background, (0,0))
    
    box = Box()
    allSprites = pygame.sprite.Group(box)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
    
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
if __name__ == "__main__":
    main()
