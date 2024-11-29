import pygame,sys
from pygame import *
from math import*
from random import*
from perlin_noise import PerlinNoise


pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

clicked = False
class button():
    ##colours for button
    text_col = (0, 0, 0)
    white = (255, 255, 255)
    black = (0,0,0)
    def __init__(self, x, y, text,w ,h,font):
        self.x = x
        self.y = y
        self.text = text
        self.w = w
        self.h = h
        self.font = font
    def draw_button(self):
        global clicked
        action = False
        ######get mouse position
        pos = pygame.mouse.get_pos()
        #######create pygame Rect object for the button
        button_rect = Rect(self.x-5, self.y, self.w, self.h)
        #pygame.draw.rect(screen,self.white,button_rect,1)
        #######add text to button
        text_img = self.font.render(self.text, True, self.white)
        screen.blit(text_img, (self.x , self.y))
        #######check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            text_img = self.font.render(self.text, True, self.white)
            screen.blit(text_img, (self.x , self.y))
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            return action
stars=[sample(range(20,1180),450),sample(range(20,680),450)]


x=randint(0,9999999999999999)
print(x)
noise = PerlinNoise(octaves=1, seed=x)
pos=[[],[]]
for i,j in enumerate(range(1000,-1,-1)):
    #x=noise(i/40)*1000
   
    x = [(tanh(noise(j/100)*pi)*100)+600,(tan(noise(i/100)*pi)*100)+350]
    #print(cos(noise(i/100)))
    x=tuple(x)
    pos[0].append(x)
    x = [(tan(noise(j/100)*pi)*100)+600,(tanh(noise(i/100)*pi)*100)+350]
    x=tuple(x)
    pos[1].append(x)

fps = 60
i=0
z=4
#pos=(randint(150,1100),randint(150,550))


yellow = (255,255,0)
blue=(0,150,255)
path = True
while True:
    screen.fill((0,0,0))
    """for y in range(len(stars[0])):
        pygame.draw.circle(screen,(255,255,255),(stars[0][y],stars[1][y]),randint(1,2))"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode=='s':
                path = not(path)
            if event.unicode=='r':
                x=randint(0,99999999999)
                print(x)
                noise = PerlinNoise(octaves=1, seed=x)
                pos=[[],[]]
                for i,j in enumerate(range(1000,-1,-1)):
                    #x=noise(i/40)*1000
                
                    x = [(tanh(noise(i/100)*pi)*100)+600,(tan(noise(j/100)*pi)*100)+350]
                    #print(cos(noise(i/100)))
                    x=tuple(x)
                    pos[0].append(x)
                    x = [(tan(noise(i/100)*pi)*100)+600,(tanh(noise(j/100)*pi)*100)+350]
                    x=tuple(x)
                    pos[1].append(x)
                i=0
                z=4
    
    # pygame.draw.circle(screen,yellow,(pos[0][i][0],pos[0][i][1]),z)
    # pygame.draw.circle(screen,blue,(pos[1][i][0],pos[1][i][1]),z)
    if path:
        pygame.draw.lines(screen,(255,255,255),True,pos[0])
        pygame.draw.lines(screen,(255,255,255),True,pos[1])
    i+=1
    if i==999:
        i=0
    pygame.display.update()
    clock.tick(fps)

