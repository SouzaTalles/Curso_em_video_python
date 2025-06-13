# Aluguel de Carros

d = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
vd = (d * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(vd))