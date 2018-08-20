import pygame
pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Badger!")

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score=0
        self.goal=False
        self.font=pygame.font.SysFont("None",28)

    def update(self):
        self.text="ISK: %d" %self.score
        self.image=self.font.render(self.text,1,(255,255,255))
        self.rect=self.image.get_rect()
        self.rect.left=500
        self.rect.top=10

    def incDeaths(self):
        self.score+=1
        self.goal=False

    def hitGoal(self):
        self.goal=True

class Badger(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface((205, 47))
        self.image = pygame.image.load('img/badger.gif')
        """self.image = self.image.convert()
        self.image.fill((255, 0, 0))
        pygame.draw.rect(self.image,(0,0,0),(0,0,24,24),5)
        self.rect = self.image.get_rect()
        self.rect.centerx = 100
        self.rect.centery = 240
        """
        self.dx=0
        self.dy=0
        self.dying=False
        self.deathThroes=0

    def checkBounds(self):
        self.dying=False
        
    def update(self):
        if not self.dying:
            self.centerx+=self.dx
            self.centery+=self.dy
            self.checkBounds()
        else:
            #if self.deathThroes==0:
                #self.fade=2
            #disappear
            #if self.deathThroes<=20:
                #self.image.fill((255,self.fade,self.fade))
                #pygame.draw(self.image,(self.fade,self.fade,self.fade),(0,0,24,24),5)
                #self.fade+=12
                #self.deathThroes+=1
            #reappear
            if self.deathThroes==21:
                self.centerx=100
                self.centery=240
                self.image.fill((255,self.fade,self.fade))
                pygame.draw.rect(self.image,(self.fade,self.fade,self.fade),(0,0,24,24),5)
                self.fade-=12
                self.deathThroes+=1  
            elif self.deathThroes<=40:
                self.image.fill((255,self.fade,self.fade))
                pygame.draw.rect(self.image,(self.fade,self.fade,self.fade),(0,0,24,24),5)
                self.fade-=12
                self.deathThroes+=1
            else:
                self.image.fill((255, 0, 0))
                pygame.draw.rect(self.image,(0,0,0),(0,0,24,24),5)
                self.dying=False       

    def reset(self):
        self.dying=True
        self.deathThroes=0
        self.dx=0
        self.dy=0

    def isDying(self):
        return self.dying
    """
    def changeUp(self,halt):
        if not self.dying:                self.dx=0
            if halt:
                self.dy=0
            else:
                self.dy=-3
    """
    """
    def changeDown(self,halt):
        if not self.dying:                self.dx=0
            if halt:
                self.dy=0
            else:
                self.dy=3
    """
    def changeRight(self,halt):
        if not self.dying:
            if halt:
                self.dx=0
            else:
                self.dx=3
            
    def changeLeft(self,halt):
        if not self.dying:
            if halt:
                self.dx=0
            else:
                self.dx=-3

def drawLevel1(background):
    background = pygame.image.load('img/back1.jpg')

def level1():
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    
    drawLevel1(background) #take drawLevel1 and do it
    screen.blit(background, (0,0))

    
    
    #create the player sprite
    badger = Badger()
    playerSprite = pygame.sprite.Group(badger)

    #put the titan here later
    """
    #create the enemy sprites
    ballSprites=pygame.sprite.Group()
    x=165
    topy=165
    bottomy=315
    up=False
    for i in range(12):
        if not up:
            blueBall=BlueBall(x,topy,up,165,315)
            up=True
        else:
            blueBall=BlueBall(x,bottomy,up,165,315)
            up=False
        x=x+30
        ballSprites.add(blueBall)
    """

    """
    #create the goal sprite
    goal=YellowBall(150+180,150+90)
    goalGroup=pygame.sprite.Group(goal)
    """
    
    #create the scoreboard
    scoreboard=Scoreboard()
    scoreGroup=pygame.sprite.Group(scoreboard)
    
    clock = pygame.time.Clock()
    keepGoing = True
    success=False
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                #if event.key==pygame.K_UP:
                #    badger.changeUp(False)
                #elif event.key==pygame.K_DOWN:
                #   badger.changeDown(False)
                if event.key==pygame.K_LEFT:
                    badger.changeLeft(False)
                elif event.key==pygame.K_RIGHT:
                    badger.changeRight(False)
            elif event.type==pygame.KEYUP:
                #if event.key==pygame.K_UP:
                #    badger.changeUp(True)
                #elif event.key==pygame.K_DOWN:
                #    badger.changeDown(True)
                if event.key==pygame.K_LEFT:
                    badger.changeLeft(True)
                elif event.key==pygame.K_RIGHT:
                    badger.changeRight(True)

        #check for collisions with enemies
        """
        if not badger.isDying():
            #if pygame.sprite.spritecollide(badger,ballSprites,False):
                scoreboard.incDeaths()
                box.reset()
                if not goal in goalGroup:
                    goalGroup.add(goal)

        #check for collision with goal
        if not box.isDying():
            if pygame.sprite.spritecollide(box,goalGroup,True):
                scoreboard.hitGoal()
            if pygame.sprite.spritecollide(box,endZoneGroup,False):
                if scoreboard.goal:
                    success=True
                    keepGoing=False
        """        
        #drawing updates
        playerSprite.clear(screen, background)
        #ballSprites.clear(screen,background)
        scoreGroup.clear(screen,background)
        #goalGroup.clear(screen,background)
        
        playerSprite.update()
        #ballSprites.update()
        scoreGroup.update()
        #goalGroup.update()
        
        playerSprite.draw(screen)
        #ballSprites.draw(screen)
        scoreGroup.draw(screen)
        #goalGroup.draw(screen)
        
        pygame.display.flip()

    #pause for effect
    pygame.time.wait(3000) #3000 miliseconds
    return success

def kGoScreen(successKGo):
    keepGoing=True
    clock = pygame.time.Clock()
    background=pygame.Surface(screen.get_size())
    background.fill((0,0,0))
    font=pygame.font.SysFont("None",28)
    if successKgo:
        text="This is the message you get when you win"
    else:
        text="You lost, lol."
    label=font.render(text,1,(255,255,255))
    background.blit(label,(100,100))
    screen.blit(background, (0,0))

    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                keepGoing=False
    
        pygame.display.flip()
    return not keepGoing


def main():
    donePlaying=False
    while not donePlaying:
        success=level1()
        donePlaying=kGoScreen(success)

   
if __name__ == "__main__":
    main()
