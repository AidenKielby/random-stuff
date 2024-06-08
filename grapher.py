
import pygame
from pygame import *
import sys
import math
from math import *
men = False

pygame.init()
x = 400
y = 400
x23 = 400
y23 = 400
press = True
mult = 10
ragtag = 8000
base_font = pygame.font.Font(None, 32)
user_text = ''
small_font = pygame.font.Font(None, 30)

pygame.display.set_caption("Aiden Kielbasinski's graphing calculator", icontitle='ello')
screen = pygame.display.set_mode((800, 800))

equation = 'y = (1x)'
testemonial = {}
# Split the equation into its components
def eqew(equation,ragtag,testemonial):
    for i in range(ragtag):
        parts = equation.split('=')
        lhs, rhs = parts[0], parts[1]
        m_index = lhs.find('m')
        b_index = lhs.find('b')
        if m_index != -1:
            m = float(lhs[:m_index])
        else:
            m = float(1)
        if b_index != -1:
            b = float(lhs[b_index + 1:])
        else:
            b = 0.0
        i -= ragtag/2
        x = 1 * i/10
        y = eval(rhs.replace('x', f'* {str(x)}'))
        
        testemonial[x] = y
        screen.fill((255,255,255))
    return testemonial
testemonial = eqew('y=1x',ragtag,testemonial)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            user_text += event.unicode
            if event.key == K_BACKSPACE:
                user_text = user_text[:-2]
            if event.key == pygame.K_TAB:
                testemonial = {}
                testemonial = eqew(user_text, ragtag, testemonial)
                user_text = user_text[:-1]
                men = True
            if event.key == K_UP:
                if mult < 100:
                    mult += 4
            if event.key == K_DOWN:
                if mult > 10:
                    mult -= 4
            screen.fill((255,255,255))
            press = True
        if event.type == pygame.KEYUP:
            press = False
    pygame.draw.line(screen, (0,0,255),(0,y),(800,y),2)
    pygame.draw.line(screen, (0,0,255),(x,0),(x,800),2)
    o = 0
    for i in testemonial:
        x1 = i
        y1 = testemonial[i]
        x1 = x1 * mult
        y1 = y1 * mult
        y -= y1
        x += x1
        if user_text == 'y=(1x)**(0.4)' and men:
            print(x,y,y1,testemonial[i],eval(str(y)))
        if o == 20:
            text_surface1 = small_font.render("|", True, (0,0,0))
            screen.blit(text_surface1, (x,y23-10))
            #text_surface2 = small_font.render("--", True, (0,0,0))
            #screen.blit(text_surface2, (x23-6,y))
            o = 0
        y = eval(str(y))
        pygame.draw.circle(screen, (0,0,0), (x,y), 2)
        y = y23
        x = x23
        o += 1
    pygame.display.update()
    if press:
        screen.fill((255,255,255))
    text_surface = base_font.render(user_text, True, (0,0,0))
    screen.blit(text_surface, (0,0))
    