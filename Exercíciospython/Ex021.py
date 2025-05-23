import pygame
pygame.init()
pygame.mixer.music.load('materiais/ex.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue  

# Código adicionando uma música