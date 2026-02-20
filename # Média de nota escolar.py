# Comprimento da hipotenusa
import math

ca= float(input('Digite o comprimento do cateto adjacente: '))
co= float(input('Digite o comprimento do cateto oposto: '))
hip= math.hypot(ca,co)
print(f'O comprimento da hipotenusa é: {hip:.1f}')