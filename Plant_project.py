# Plant project
# March
# Rayner

from time import sleep
from tkinter import Scale
import pygame
import random

pygame.init()

# Hard variables
# Screen size

WIDTH = 1500
HEIGHT = 900
SHELF_HEIGHT = 30

# Def

# Watering, cutting, selling, planting

# Classes

class Pot: # This makes class Pot (Capital first letter in classes)

    picture = pygame.image.load("pot_terracotta.png") # gets picture from folder
    picture = pygame.transform.scale(picture, (128,128)) # Scales picture

    def __init__(self, x, y): # This is run when making pot. To set it up.
        self.x = x 
        self.y = y
        self.plant = None
        self.unlocked = False

    def update(self): # Checks if there is not plant in pot
        if self.plant != None:
            self.plant.update()

    def show(self): 
        if not self.unlocked: # Checks if pot is locked
            return

        screen.blit(Pot.picture, (self.x, self.y))
        
        if self.plant != None: # Cheking if there is a plant. show plant if is
            self.plant.show(self.x, self.y)

    def get_rect(self): # Makes rectangle 
        if self.plant == None: #Makes size of pot, if no plants
            rect = pygame.Rect(self.x, self.y, Pot.picture.get_width(), Pot.picture.get_height())
        
        else: # Makes size of pot + plant if has plant
            rect = pygame.Rect(self.x, self.y - self.plant.picture.get_height(), Pot.picture.get_width(), Pot.picture.get_height() + self.plant.picture.get_height())
        return rect

    def clicked(self):
        if not self.unlocked:
            return

        if self.plant == None:
            self.plant = Plant(1, 1, "sansevieria")

        else:
            self.plant.water()


class Plant: # Makes class plant (Capital first letter)

    little_picture = pygame.image.load("plant_size_smal.png")
    big_picture = pygame.image.load("plant_size_2.gif")

    little_picture = pygame.transform.scale(little_picture, (128,128))
    big_picture = pygame.transform.scale(big_picture, (128,128))

    def __init__(self, size, growth, species): # Makes plant an object
        self.size = size
        self.growth = growth
        self.species = species
        if self.size == 1: # Checks what size plant has, chooses picture 
            self.picture = Plant.little_picture
        else:
            self.picture = Plant.big_picture


    def water(self): # Waters plant
        self.growth += 1 
        print('"Splosh" "splash" "splush"')

    def growing(self):  # Makes plant grow
        self.growth -= 10
        self.size += 1
        print("Sprout")
        if self.size == 1: # Checks what size plant has, chooses picture 
            self.picture = Plant.little_picture
        else:
            self.picture = Plant.big_picture

    def status(self):
        print(f"Statues is:\nSize: {self.size}\nGrowth: {self.growth} \nSpecies: {self.species}")

    def show(self, x, y):
        screen.blit(self.picture, (x,y - self.picture.get_height()))

    def update(self):
        if self.growth >= 10:
            self.growing()
        
# Class Mouse:
# Class Character:

starter_plant = Plant(1, 1, "Sansevieria") #Makes the starter plant and second plant
second_plant = Plant(2, 1, "Sansevieria") # Unsure about numbers and names. Write in brackets and learn to read that!


# Creating scenario

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Makes screen
shelf = pygame.Rect(0, HEIGHT//2, WIDTH, SHELF_HEIGHT) # makes shelf
pygame.draw.rect(screen,(150,100,10),shelf) # Draws shelf

pots = [] # List of pots
gap = 10
first_pot = Pot(gap, shelf.top - Pot.picture.get_height()) # Makes first pot
pots.append(first_pot) # Puts first_pot in list of pots

for i in range(1,10): # Loops through the placerment of pots 
    pot_i = Pot((Pot.picture.get_width() + pots[i - 1].x + gap), pots[i - 1].y)
    pots.append(pot_i) # Adds pot_i to the back of the list of pots

pots[0].unlocked = True
pots[0].plant = starter_plant

num_pots=1

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    
    if e.type == pygame.KEYUP:
        if e.key == pygame.K_SPACE:
            pots[num_pots].unlocked=True
            num_pots += 1

    if e.type == pygame.MOUSEBUTTONUP and e.button == pygame.BUTTON_LEFT:
        for pot in pots:
            if pot.get_rect().contains(e.pos[0],e.pos[1], 0, 0):
                pot.clicked()


    for pot in pots:
        #pygame.draw.rect(screen, (255,90,255),pot.get_rect())
        pot.update()
        pot.show()

    pygame.display.flip()

pygame.quit()