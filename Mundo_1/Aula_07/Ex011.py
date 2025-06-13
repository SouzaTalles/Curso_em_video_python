# Pintura de Parede
# Cálculo da área de uma parede e a quantidade de tinta necessária para pintá-la

l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
ar = l * a 
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(l, a, ar))
t = ar / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(t))
