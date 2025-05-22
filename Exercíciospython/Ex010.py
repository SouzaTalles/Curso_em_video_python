n = float(input('Quanto dinherio você tem na carteira? R$'))
d = n / 5.64
e = n / 6.36
print('Com R${:.2f} você pode comprar US${:.2f}'.format(n, d))
print('com R${:.2f} você pode comprar EUR${:.2f}'.format(n, e))
