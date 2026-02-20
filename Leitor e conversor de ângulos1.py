# Leitor e conversor de ângulos.
import math

angulo=float(input('Insira o valor do ângulo em graus: '))
sin=math.sin(float(angulo))
cos=math.cos(float(angulo))
tan=math.tan(float(angulo))
rad=math.radians(float(angulo))

print(f'O valor de {angulo} em radianos é: {rad:.2f}\nSeu seno é: {sin:.2f}\nSeu cosseno é: {cos:.2f}\nSua tangente é: {tan:.2f}')
