l = []

for c in range(0, 5):
    l1  = int(input('Digite um valor: '))
    if not l or l1 > l[-1]:
        l.append(l1)
        print('Adicionado ao final da lista...')
    else:
        for c, v in enumerate(l):
            if l1 <= v:
                l.insert(c, l1)
                print(f'Adicionado na posiçãa {c} da lista')
                break

print('-=' * 30)
print(f'Os valores digitados em ordem foram {l}')
