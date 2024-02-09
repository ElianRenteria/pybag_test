import os
import pygame
from random import randint
r = str(randint(1,4))
bg = pygame.transform.scale(pygame.image.load("backgrounds/BG_0"+r+"/BG_0"+r+".png"), (1920, 930))





def natural_sort_key(s):
    import re
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def load_images(directory, array, height, width):
    for folderName in sorted(os.listdir(directory), key=natural_sort_key):
        if folderName != ".DS_Store":
            sprites = []
            for filename in sorted(os.listdir(os.path.join(directory, folderName)), key=natural_sort_key):
                if filename.endswith(".png"):
                    sprites.append(pygame.transform.scale(pygame.image.load(os.path.join(directory, folderName, filename)), (height, width)))
            array[folderName] = sprites

# Example usage
turtle = {}
load_images('Sprites/', turtle, 100, 100)
