import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

red = np.array([255,0,0])
red = red.astype(np.uint8)
green = np.array([0,255,0])
green = green.astype(np.uint8)
blue = np.array([0,0,255])
blue = blue.astype(np.uint8)
yellow = np.array([255,255,0])
yellow = yellow.astype(np.uint8)
black = np.array([0,0,0])
black = black.astype(np.uint8)
white = np.array([255,255,255])
white = white.astype(np.uint8)
orange = np.array([255,128,0])
orange = orange.astype(np.uint8)

state_dict = {'face':[[red,red,red],[red,red,red],[red,red,red]],
             'right':[[green,green,green],[green,green,green],[green,green,green]],
             'opposite':[[blue,blue,blue],[blue,blue,blue],[blue,blue,blue]],
             'left':[[yellow,yellow,yellow],[yellow,yellow,yellow],[yellow,yellow,yellow]],
             'top':[[white,white,white],[white,white,white],[white,white,white]],
             'bottom':[[orange,orange,orange],[orange,orange,orange],[orange,orange,orange]]}

def reset_cube():
    global state_dict
    state_dict = {'face':[[red,red,red],[red,red,red],[red,red,red]],
             'right':[[green,green,green],[green,green,green],[green,green,green]],
             'opposite':[[blue,blue,blue],[blue,blue,blue],[blue,blue,blue]],
             'left':[[yellow,yellow,yellow],[yellow,yellow,yellow],[yellow,yellow,yellow]],
             'top':[[white,white,white],[white,white,white],[white,white,white]],
             'bottom':[[orange,orange,orange],[orange,orange,orange],[orange,orange,orange]]}

def right(top,middle,bottom):
    if (top == 0)&(middle == 0)&(bottom == 0):
        pass
        
        
    if (top == 1)&(middle == 1)&(bottom == 1):
        temp = state_dict['face']
        state_dict['face'] = state_dict['left']
        state_dict['left'] = state_dict['opposite']
        state_dict['opposite'] = state_dict['right']
        state_dict['right'] = temp
        state_dict['top'] = list(np.rot90(state_dict['top']))
        state_dict['bottom'] = list(np.rot90(np.rot90(np.rot90(state_dict['bottom']))))
        
        
    if (top == 1)&(middle == 0)&(bottom == 0):
        temp = state_dict['face'][0]
        state_dict['face'][0] = state_dict['left'][0]
        state_dict['left'][0] = state_dict['opposite'][0]
        state_dict['opposite'][0] = state_dict['right'][0]
        state_dict['right'][0] = temp
        state_dict['top'] = list(np.rot90(state_dict['top']))
        
        
        
    if (top == 0)&(middle == 1)&(bottom == 0):
        temp = state_dict['face'][1]
        state_dict['face'][1] = state_dict['left'][1]
        state_dict['left'][1] = state_dict['opposite'][1]
        state_dict['opposite'][1] = state_dict['right'][1]
        state_dict['right'][1] = temp
        
        
        
    if (top == 0)&(middle == 0)&(bottom == 1):
        temp = state_dict['face'][2]
        state_dict['face'][2] = state_dict['left'][2]
        state_dict['left'][2] = state_dict['opposite'][2]
        state_dict['opposite'][2] = state_dict['right'][2]
        state_dict['right'][2] = temp
        state_dict['bottom'] = list(np.rot90(np.rot90(np.rot90(state_dict['bottom']))))
        
        
        
    if (top == 1)&(middle == 1)&(bottom == 0):
        temp0 = state_dict['face'][0]
        temp1 = state_dict['face'][1]
        state_dict['face'][0] = state_dict['left'][0]
        state_dict['left'][0] = state_dict['opposite'][0]
        state_dict['opposite'][0] = state_dict['right'][0]
        state_dict['right'][0] = temp0
        state_dict['face'][1] = state_dict['left'][1]
        state_dict['left'][1] = state_dict['opposite'][1]
        state_dict['opposite'][1] = state_dict['right'][1]
        state_dict['right'][1] = temp1
        state_dict['top'] = list(np.rot90(state_dict['top']))
        
        
        
    if (top == 1)&(middle == 0)&(bottom == 1):
        temp0 = state_dict['face'][0]
        temp2 = state_dict['face'][2]
        state_dict['face'][0] = state_dict['left'][0]
        state_dict['left'][0] = state_dict['opposite'][0]
        state_dict['opposite'][0] = state_dict['right'][0]
        state_dict['right'][0] = temp0
        state_dict['face'][2] = state_dict['left'][2]
        state_dict['left'][2] = state_dict['opposite'][2]
        state_dict['opposite'][2] = state_dict['right'][2]
        state_dict['right'][2] = temp2
        state_dict['top'] = list(np.rot90(state_dict['top']))
        state_dict['bottom'] = list(np.rot90(np.rot90(np.rot90(state_dict['bottom']))))
        
        
        
    if (top == 0)&(middle == 1)&(bottom == 1):
        temp1 = state_dict['face'][1]
        temp2 = state_dict['face'][2]
        state_dict['face'][1] = state_dict['left'][1]
        state_dict['left'][1] = state_dict['opposite'][1]
        state_dict['opposite'][1] = state_dict['right'][1]
        state_dict['right'][1] = temp1
        state_dict['face'][2] = state_dict['left'][2]
        state_dict['left'][2] = state_dict['opposite'][2]
        state_dict['opposite'][2] = state_dict['right'][2]
        state_dict['right'][2] = temp2
        state_dict['bottom'] = list(np.rot90(np.rot90(np.rot90(state_dict['bottom']))))
        
        

def left(top,middle,bottom):
    if (top == 0)&(middle == 0)&(bottom == 0):
        pass
        
        
    if (top == 1)&(middle == 1)&(bottom == 1):
        temp = state_dict['face']
        state_dict['face'] = state_dict['right']
        state_dict['right'] = state_dict['opposite']
        state_dict['opposite'] = state_dict['left']
        state_dict['left'] = temp
        state_dict['bottom'] = list(np.rot90(state_dict['bottom']))
        state_dict['top'] = list(np.rot90(np.rot90(np.rot90(state_dict['top']))))
        
        
        
    if (top == 1)&(middle == 0)&(bottom == 0):
        temp = state_dict['face'][0]
        state_dict['face'][0] = state_dict['right'][0]
        state_dict['right'][0] = state_dict['opposite'][0]
        state_dict['opposite'][0] = state_dict['left'][0]
        state_dict['left'][0] = temp
        state_dict['top'] = list(np.rot90(np.rot90(np.rot90(state_dict['top']))))
        
        
        
    if (top == 0)&(middle == 1)&(bottom == 0):
        temp = state_dict['face'][1]
        state_dict['face'][1] = state_dict['right'][1]
        state_dict['right'][1] = state_dict['opposite'][1]
        state_dict['opposite'][1] = state_dict['left'][1]
        state_dict['left'][1] = temp
        
        
        
    if (top == 0)&(middle == 0)&(bottom == 1):
        temp = state_dict['face'][2]
        state_dict['face'][2] = state_dict['right'][2]
        state_dict['right'][2] = state_dict['opposite'][2]
        state_dict['opposite'][2] = state_dict['left'][2]
        state_dict['left'][2] = temp
        state_dict['bottom'] = list(np.rot90(state_dict['bottom']))
        
        
        
    if (top == 1)&(middle == 1)&(bottom == 0):
        temp0 = state_dict['face'][0]
        temp1 = state_dict['face'][1]
        state_dict['face'][0] = state_dict['right'][0]
        state_dict['right'][0] = state_dict['opposite'][0]
        state_dict['opposite'][0] = state_dict['left'][0]
        state_dict['left'][0] = temp0
        state_dict['face'][1] = state_dict['right'][1]
        state_dict['right'][1] = state_dict['opposite'][1]
        state_dict['opposite'][1] = state_dict['left'][1]
        state_dict['left'][1] = temp1
        state_dict['top'] = list(np.rot90(np.rot90(np.rot90(state_dict['top']))))
        
        
        
    if (top == 1)&(middle == 0)&(bottom == 1):
        temp0 = state_dict['face'][0]
        temp2 = state_dict['face'][2]
        state_dict['face'][0] = state_dict['right'][0]
        state_dict['right'][0] = state_dict['opposite'][0]
        state_dict['opposite'][0] = state_dict['left'][0]
        state_dict['left'][0] = temp0
        state_dict['face'][2] = state_dict['right'][2]
        state_dict['right'][2] = state_dict['opposite'][2]
        state_dict['opposite'][2] = state_dict['left'][2]
        state_dict['left'][2] = temp2
        state_dict['bottom'] = list(np.rot90(state_dict['bottom']))
        state_dict['top'] = list(np.rot90(np.rot90(np.rot90(state_dict['top']))))
        
        
        
    if (top == 0)&(middle == 1)&(bottom == 1):
        temp1 = state_dict['face'][1]
        temp2 = state_dict['face'][2]
        state_dict['face'][1] = state_dict['right'][1]
        state_dict['right'][1] = state_dict['opposite'][1]
        state_dict['opposite'][1] = state_dict['left'][1]
        state_dict['left'][1] = temp1
        state_dict['face'][2] = state_dict['right'][2]
        state_dict['right'][2] = state_dict['opposite'][2]
        state_dict['opposite'][2] = state_dict['left'][2]
        state_dict['left'][2] = temp2
        state_dict['bottom'] = list(np.rot90(state_dict['bottom']))
        
        

def down(Left,middle,Right):    
    temp = state_dict['top']
    state_dict['top'] = list(np.rot90(state_dict['right']))
    state_dict['right'] = list(np.rot90(state_dict['bottom']))
    state_dict['bottom'] = list(np.rot90(state_dict['left']))
    state_dict['left'] = list(np.rot90(temp))
    state_dict['face'] = list(np.rot90(state_dict['face']))
    state_dict['opposite'] = list(np.rot90(np.rot90(np.rot90(state_dict['opposite']))))
    right(Right,middle,Left)
    temp = state_dict['top']
    state_dict['top'] = list(np.rot90(np.rot90(np.rot90(state_dict['left']))))
    state_dict['left'] = list(np.rot90(np.rot90(np.rot90(state_dict['bottom']))))
    state_dict['bottom'] = list(np.rot90(np.rot90(np.rot90(state_dict['right']))))
    state_dict['right'] = list(np.rot90(np.rot90(np.rot90(temp))))
    state_dict['opposite'] = list(np.rot90(state_dict['opposite']))
    state_dict['face'] = list(np.rot90(np.rot90(np.rot90(state_dict['face']))))
    
    

def up(Left,middle,Right):    
    temp = state_dict['top']
    state_dict['top'] = list(np.rot90(state_dict['right']))
    state_dict['right'] = list(np.rot90(state_dict['bottom']))
    state_dict['bottom'] = list(np.rot90(state_dict['left']))
    state_dict['left'] = list(np.rot90(temp))
    state_dict['face'] = list(np.rot90(state_dict['face']))
    state_dict['opposite'] = list(np.rot90(np.rot90(np.rot90(state_dict['opposite']))))
    left(Right,middle,Left)
    temp = state_dict['top']
    state_dict['top'] = list(np.rot90(np.rot90(np.rot90(state_dict['left']))))
    state_dict['left'] = list(np.rot90(np.rot90(np.rot90(state_dict['bottom']))))
    state_dict['bottom'] = list(np.rot90(np.rot90(np.rot90(state_dict['right']))))
    state_dict['right'] = list(np.rot90(np.rot90(np.rot90(temp))))
    state_dict['opposite'] = list(np.rot90(state_dict['opposite']))
    state_dict['face'] = list(np.rot90(np.rot90(np.rot90(state_dict['face']))))
    
    



def clockwise(front,middle,last):
    up(1,1,1)
    left(front,middle,last)
    down(1,1,1)
    
    
def anticlockwise(front,middle,last):
    up(1,1,1)
    right(front,middle,last)
    down(1,1,1)
    

def rotate_right(top,middle,bottom):
    right(top,middle,bottom)
    plt.imshow(state_dict['face'])
    plt.show()
    
def rotate_left(top,middle,bottom):
    left(top,middle,bottom)
    plt.imshow(state_dict['face'])
    plt.show()
    
def rotate_up(left,middle,right):
    up(left,middle,right)
    plt.imshow(state_dict['face'])
    plt.show()
    
def rotate_down(left,middle,right):
    down(left,middle,right)
    plt.imshow(state_dict['face'])
    plt.show()
    
def rotate_clockwise(front,middle,last):
    clockwise(front,middle,last)
    plt.imshow(state_dict['face'])
    plt.show()
    
def rotate_anticlockwise(front,middle,last):
    anticlockwise(front,middle,last)
    plt.imshow(state_dict['face'])
    plt.show()

def reverser(function):
    if function == rotate_right:
        return rotate_left
    if function == rotate_left:
        return rotate_right
    if function == rotate_up:
        return rotate_down
    if function == rotate_down:
        return rotate_up
    if function == rotate_clockwise:
        return rotate_anticlockwise
    if function == rotate_anticlockwise:
        return rotate_clockwise



import pygame

pygame.init()

import pylab
import matplotlib
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg

fig = pylab.figure(figsize=[3, 3],dpi=100)
ax = fig.gca()
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_xticks([])
ax.set_yticks([])



white = [255,255,255]
pygame.display.set_caption('Rubiks Cube')
#surf = pygame.surfarray.make_surface(f)
window = pygame.display.set_mode((400, 400))
window.fill(white)
screen = pygame.display.get_surface()




num = ""
keyd = []
run = True
while run:
    
    for event in pygame.event.get():
###############################################################    
        if event.type == pygame.KEYDOWN:
            if (event.key == 257):
                num = 1
            if (event.key == 258):
                num = 2
            if (event.key == 259):
                num = 3
            if (event.key == 260):
                num = 4
            if (event.key == 261):
                num = 5
            if (event.key == 262):
                num = 6
            if (event.key == 263):
                num = 7
            if (event.key == 264):
                num = 8
            if (event.key == 265):
                num = 9
                
        if event.type == pygame.KEYDOWN:
            if (event.key == 276)&((num == 1)|(num == 2)|(num == 3)):
                left(0,0,1)    
        if event.type == pygame.KEYDOWN:
            if (event.key == 276)&((num == 4)|(num == 5)|(num == 6)):
                left(0,1,0)
        if event.type == pygame.KEYDOWN:
            if (event.key == 276)&((num == 7)|(num == 8)|(num == 9)):
                left(1,0,0)
                
                
        if event.type == pygame.KEYDOWN:
            if (event.key == 275)&((num == 1)|(num == 2)|(num == 3)):
                right(0,0,1)    
        if event.type == pygame.KEYDOWN:
            if (event.key == 275)&((num == 4)|(num == 5)|(num == 6)):
                right(0,1,0)
        if event.type == pygame.KEYDOWN:
            if (event.key == 275)&((num == 7)|(num == 8)|(num == 9)):
                right(1,0,0)
                
                
        if event.type == pygame.KEYDOWN:
            if (event.key == 273)&((num == 1)|(num == 4)|(num == 7)):
                up(1,0,0)    
        if event.type == pygame.KEYDOWN:
            if (event.key == 273)&((num == 2)|(num == 5)|(num == 8)):
                up(0,1,0)
        if event.type == pygame.KEYDOWN:
            if (event.key == 273)&((num == 3)|(num == 6)|(num == 9)):
                up(0,0,1)
                
                
        if event.type == pygame.KEYDOWN:
            if (event.key == 274)&((num == 1)|(num == 4)|(num == 7)):
                down(1,0,0)    
        if event.type == pygame.KEYDOWN:
            if (event.key == 274)&((num == 2)|(num == 5)|(num == 8)):
                down(0,1,0)
        if event.type == pygame.KEYDOWN:
            if (event.key == 274)&((num == 3)|(num == 6)|(num == 9)):
                down(0,0,1)

        f = state_dict['face']
        f = np.array(f)
        ax.imshow(f)

        canvas = agg.FigureCanvasAgg(fig)
        canvas.draw()

        renderer = canvas.get_renderer()
        raw_data = renderer.tostring_rgb()
        size = canvas.get_width_height()
        surf = pygame.image.fromstring(raw_data, size, "RGB")
        screen.blit(surf, (40,40))
        pygame.display.flip()
        pygame.display.update()
    
        if event.type == pygame.QUIT:
            run = False
            break
pygame.quit()