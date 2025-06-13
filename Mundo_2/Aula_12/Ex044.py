# Gerenciador de Pagamentos

print('=' * 12, 'LOJAS AMERICANAS', '=' * 12)
p = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista no cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no catão''')
op = int(input('Qual é a opção? '))

if op == 1:
    p1 = p * 0.9
    print(f'Sua compra de R${p:.2f} vai custar R${p1:.2f} no final.')
elif op == 2:
    p1 = p * 0.95
    print(f'Sua compra de R${p:.2f} vai custar R${p1:.2f} no final.')
elif op == 3: 
    p1 = p / 2
    print(f'Sua compra será parcelada em 2x de R${p1:.2f} SEM JUROS.')
    print(f'Sua compra vai custar R${p:.2f} no final.')
elif op == 4:
    pa = int(input('Quantas parcelas? '))
    p1 = p * 1.2
    p2 = p1 / pa
    print(f'Sua compra será parcelada em {pa}x de R${p2:.2f} COM JUROS.')
    print(f'Sua compra de R${p:.2f} vai custar R${p1:.2f} no final.')
else:
    print('\33[31mOpção invalida. Tente novamente.\33[m]')
