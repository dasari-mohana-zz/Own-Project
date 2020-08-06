# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 17:48:28 2020

@author: MOHANA D
"""

# We can do in two different ways

# 1st method
'''Using -> tkinter'''
from pygame import mixer
from tkinter import *

root = Tk()
root.geometry("600x300") #tk window dimensions

# initializing mixer
mixer.init()
mixer.music.load("Best Piano.mp3") #uploading music file in '.mp3' format

#defining play(),pause(),resume() and stop() options
def pause():
    mixer.music.pause()

def play():
    mixer.music.play()

def resume():
    mixer.music.unpause()
    
def stop():
    mixer.music.stop()
 
# tk-window features
Label(root, text="Welcome to music player", font="lucidia 30 bold").pack()
Button(text="Play", command=play).place(x=200, y=100)
Button(text="Pause", command=pause).place(x=250, y=100)
Button(text="Resume", command=resume).place(x=310, y=100)
Button(text="Stop", command=stop).place(x=380, y=100)

root.mainloop()

quit()

###############################################################################

# 2nd method
'''Usung -> mixer'''

import pygame
from pygame import mixer

#initiliazing pygame and mixer
pygame.init()
mixer.init()

# Creating a window
screen = pygame.display.set_mode((300, 300))
mixer.music.load("Best Piano.mp3") #uploading music file in '.mp3' format
mixer.music.play()

print("Press 'P' to Pause")
print("Press 'R' to Resume")
print("Press 'Q' to Quit")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: # Creating Controls
            if event.key == pygame.K_p:
                mixer.music.pause()
            if event.key == pygame.K_r:
                mixer.music.unpause()
            if event.key == pygame.K_q:
                running = False
                
quit()


