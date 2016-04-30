import pygame
import sys
import random
import time
from pygame.locals import *
from array import array
pygame.init()
pygame.font.init
pygame.mixer.init
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
bg=pygame.image.load('BG.jpg')
menu=pygame.image.load('menu.jpg')
bgc=pygame.image.load('BGC.jpg')
bggo=pygame.image.load('BGgo.jpg')
bgs=pygame.image.load('BGS.jpg')
gl=pygame.image.load('GL.jpg')
fps=15

diswidth=1000
disheight=600

cellsize=10
UP ='up'
DOWN='down'
RIGHT='right'
LEFT='left'
ENTER='enter'

def runmenu():
    
    while True:
        setDisplay.blit(menu,(0,0))
        pygame.display.update()
        event=pygame.event.wait()
        if pygame.mouse.get_pressed()==(1,0,0):
            (xm,ym)=pygame.mouse.get_pos()
            if xm>248 and xm<420:
                if ym>146 and ym<201:
                    rungame()
            if xm>457 and xm<591:
                if ym>232 and ym<285:
                    runscore()
            if xm>456 and xm<590:
                if ym>357 and ym<409:
                    runcontrol()
            if xm>293 and xm<439:
                if ym>450 and ym<502:
                    pygame.quit()
                    sys.exit()
def runcontrol():
    while True:
        setDisplay.blit(bgc,(0,0))
        pygame.display.update()
        event=pygame.event.wait()
        if pygame.mouse.get_pressed()==(1,0,0):
            (xc,yc)=pygame.mouse.get_pos()
            if xc>49 and xc<206:
                if yc>63 and yc<125:
                    runmenu()
def runscore():
    highscore1=get_high_score()
    while True:
        setDisplay.blit(bgs,(0,0))
        myfont=pygame.font.SysFont('timesnewroman',45,1)
        scorelabel=myfont.render(str(highscore1),1,(255,255,255))
        setDisplay.blit(scorelabel,(diswidth/2.3,disheight/1.75))
        pygame.display.update()
        event=pygame.event.wait()
        if pygame.mouse.get_pressed()==(1,0,0):
            (xc,yc)=pygame.mouse.get_pos()
            if xc>49 and xc<206:
                if yc>63 and yc<125:
                    runmenu()
    
def get_high_score():
    high_score= 0
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
    except IOError:
        print("There is no high score yet.")
    except ValueError:
        print("I'm confused. Starting with no high score.")
    return high_score
def save_high_score(new_high_score):
    try:
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        print("Unable to save the high score.")

def rungame():
    global a,b,x,y,score
    startx=random.randrange(10,diswidth/cellsize)
    starty=random.randrange(10,disheight/cellsize)
    coords=[{'x':startx,'y':starty}]
    direction=RIGHT
    score=5
    j=0
    l=0
    pause=False
    

    while True:
        
        j+=1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type ==KEYDOWN:
                if event.key== K_LEFT or event.key==K_a:
                    if direction!=RIGHT:
                        direction= LEFT
                        newcell={'x':coords[0]['x']-1, 'y':coords[0]['y']}
                        coords.insert(0,newcell )
                        setDisplay.blit(bg,(0,0))
                        drawcell(coords[:score-1])
                        pygame.display.update()
                        if (a==newcell['x']*cellsize and b==newcell['y']*cellsize):
                            score+=1
                            a=random.randrange(10,diswidth,cellsize)
                            b=random.randrange(10,disheight,cellsize)
                    
                elif event.key==K_RIGHT or event.key==K_d:
                    if direction!=LEFT:
                        direction=RIGHT
                        newcell={'x':coords[0]['x']+1, 'y':coords[0]['y']}
                        coords.insert(0,newcell )
                        setDisplay.blit(bg,(0,0))
                        drawcell(coords[:score-1])
                        pygame.display.update()
                        if (a==newcell['x']*cellsize and b==newcell['y']*cellsize):
                            score+=1
                            a=random.randrange(10,diswidth,cellsize)
                            b=random.randrange(10,disheight,cellsize)
                elif event.key==K_DOWN or event.key==K_s:
                    if direction!=UP:
                        direction=DOWN
                        newcell={'x':coords[0]['x'], 'y':coords[0]['y']+1}
                        coords.insert(0,newcell )
                        setDisplay.blit(bg,(0,0))
                        drawcell(coords[:score-1])
                        pygame.display.update()
                        if (a==newcell['x']*cellsize and b==newcell['y']*cellsize):
                            score+=1
                            a=random.randrange(10,diswidth,cellsize)
                            b=random.randrange(10,disheight,cellsize)
                elif event.key==K_UP or event.key==K_w:
                    if direction!=DOWN:
                        direction=UP
                        newcell={'x':coords[0]['x'], 'y':coords[0]['y']-1}
                        coords.insert(0,newcell )
                        setDisplay.blit(bg,(0,0))
                        drawcell(coords[:score-1])
                        pygame.display.update()
                        if (a==newcell['x']*cellsize and b==newcell['y']*cellsize):
                            score+=1
                            a=random.randrange(10,diswidth,cellsize)
                            b=random.randrange(10,disheight,cellsize)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    while 1: 
                        event = pygame.event.wait()
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                            break
        
                    
                    
                        
                           
        if direction ==UP:
            newcell={'x':coords[0]['x'], 'y':coords[0]['y']-1}
            
        if direction ==DOWN:
            newcell={'x':coords[0]['x'], 'y':coords[0]['y']+1}
           
        if direction == LEFT:
            newcell={'x':coords[0]['x']-1, 'y':coords[0]['y']}
            
        if direction == RIGHT:
            newcell={'x':coords[0]['x']+1, 'y':coords[0]['y']}
            

       
        coords.insert(0,newcell )
        setDisplay.blit(bg,(0,0))
        drawcell(coords[:score-1])
        pygame.draw.circle(setDisplay,red,(a,b),5,5)
        myfont=pygame.font.SysFont('timesnewroman',15,1)
        label=myfont.render('SCORE:',1,(255,255,255))
        label1=myfont.render(str(score-5),1,(255,255,255))
        setDisplay.blit(label,(diswidth*9/10,disheight/30))
        setDisplay.blit(label1,(diswidth*9.57/10,disheight/30))
        pygame.display.update()
        fpstime.tick(fps)
        


        if (newcell['x']<0 or newcell['x']>diswidth/cellsize or newcell['y']<0 or newcell['y']>disheight/cellsize):
            rungameover()

        if (a==newcell['x']*cellsize and b==newcell['y']*cellsize):
            score+=1
            a=random.randrange(10,diswidth,cellsize)
            b=random.randrange(10,disheight,cellsize)
        if(j>4):
            for i in range(1,score-1):
                if coords[0]==coords[i]:
                    l=1
                    break
        if(l==1):
            rungameover()

def rungameover():
    high_score=get_high_score()
    while True:
        setDisplay.blit(bggo,(0,0))
        myfont=pygame.font.SysFont('timesnewroman',25,1)
        label=myfont.render('Your Score:',1,(255,255,255))
        label1=myfont.render(str(score-5),1,(255,255,255))
        setDisplay.blit(label,(diswidth*7.2/10,disheight/2.1))
        setDisplay.blit(label1,(diswidth*8.5/10,disheight/2.1))
        pygame.display.update()
        cscore=score-5
        
        if cscore>high_score:
            labelhisc=myfont.render('Congratulations HIGH SCORE',1,white)
            setDisplay.blit(labelhisc,(diswidth/3,disheight*8/10))
            pygame.display.update()
            pygame.image.save(setDisplay,'image.jpg')
            save_high_score(cscore)
            
            
        if pygame.mouse.get_pressed()==(1,0,0):
            (xs,ys)=pygame.mouse.get_pos()
            if xs>806 and xs<913:
                if ys>50 and ys<100:
                    runmenu()
            if xs>442 and xs<659:
                if ys>323 and ys<390:
                    rungame()
        event=pygame.event.wait()
            
        
def drawcell(coords):
    if (coords[0]==coords[1]):
        print('same')
    for coord in coords:
        global x
        global y
        x=coord['x']*cellsize
        y=coord['y']*cellsize
        pygame.draw.circle(setDisplay,white,(x,y),5,5)

while True:
    global fpstime
    global setDisplay
    global score
    

    fpstime=pygame.time.Clock()
    setDisplay=pygame.display.set_mode((diswidth,disheight))
    pygame.display.set_caption('COBRA')
    icon=pygame.image.load('Icon.gif')
    pygame.display.set_icon(icon)
    a=random.randrange(20,diswidth,cellsize)
    b=random.randrange(30,disheight,cellsize)
    setDisplay.blit(gl,(0,0))
    pygame.display.update()
    time.sleep(1)
    runmenu()
    break


        

            

