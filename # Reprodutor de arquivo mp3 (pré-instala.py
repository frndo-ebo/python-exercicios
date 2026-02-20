# Reprodutor de arquivo mp3 (pré-instalado)

import pygame

print('Se liga no som do pai')
print('Música tocando... digite "stop" para parar a música')
while True:
    comando = input('> >').lower().strip()
    if comando == 'stop':
        pygame.mixer.music.stop()
    break

pygame.mixer.init()
pygame.mixer.music.load('c:\\Users\\spbes\\Music\\Downloads\\Eu te devoro remix.mp3')
pygame.mixer.music.play()
input()
