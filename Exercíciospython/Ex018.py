import math
a = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
h = math.tan(math.radians(a))
print('O ângulo de {} tem o SENO de {:.2f} '.format(a, s))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, c))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, h))
