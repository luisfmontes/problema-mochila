# As variaveis qtditens e pesomochila devem ser um valor maior
# devido o indice 0 não ser utilizado
qtditens = int(input(' Quantidade de itens: '))+1
pesomochila = int(input(' Peso maximo da Mochila: '))+1
mochila = list()
peso  = []
valor = []
aux1 = []
ptotal = 0
vtotal = 0

#Cria a matriz e inicializa com 0
for i in range(qtditens):
    aux1.append([0] * pesomochila)

peso.append(0)
valor.append(0)
for i in range (1,qtditens):
    peso.append(int(input(' Item {} peso: '.format(i))))
    valor.append(float(input(' Item {} valor: '.format(i))))

for l in range(1,qtditens):
    for c in range(1,pesomochila):
        # Se cabe na mochila atualiza o valor
        # Se não conserva o valor na mochila
        if c - peso[l]  >= 0:
            # Se o "novo" valor não é maior que o valor na mochila
            # conserva o valor na mochila
            if aux1[l-1][c - peso[l] ] + valor[l] > aux1[l-1][c]:
                aux1[l][c] = aux1[l-1][c - peso[l]] + valor[l]
            else:
                aux1[l][c] = aux1[l - 1][c]
        else:
            aux1[l][c] = aux1[l-1][c]

# Imprime a Matriz com os valores
print('\n')
for l in range(qtditens):
    print(aux1[l])


c = pesomochila-1
for l in range(qtditens-1,0,-1):
    # Se o valor for diferente do valor da linha anterior
    # O intem entra na Mochila
    if aux1[l][c] != aux1[l-1][c]:
        mochila.append([l,peso[l],valor[l]])
        ptotal += peso[l]
        vtotal += valor[l]
        c -= l

print('\n**** Itens na Mochila ****')
for i in mochila:
    print(f' Item  {i[0]} '
          f'peso  {i[1]} '
          f'valor {i[2]} ')
print('Peso Total: {} '
      'Valor Total: {}'.format(ptotal,vtotal))