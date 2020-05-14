import pygame
print(f"{'*'*10}Desafio 021 - Tocar MP3{'*'*10}")
pygame.mixer.init()
pygame.mixer.music.load('01 Faixa 1.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()