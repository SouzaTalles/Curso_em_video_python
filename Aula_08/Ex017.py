# Catetos e Hipotenusa

from math import hypot
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float (input('Comprimento do cateto adjacente: '))
h = (co**2 + ca**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))

#or 

co = float(input('Comprimento do cateto oposto: '))
ca = float (input('Comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))