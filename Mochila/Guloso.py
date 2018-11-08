qtditens = int(input('Quantidade de itens: '))
pesomochila = int(input('Peso maximo da Mochila: '))
peso  = []
valor = []
mochila = list()
ptotal = 0
vtotal = 0

for i in range (qtditens):
    peso.append(int(input('Item {} peso: '.format(i+1))))
    valor.append(float(input('Item {} valor: '.format(i + 1))))

aux1 = peso[:]
pesoatual = pesomochila
while len(aux1) != 0:
	 # Se o maior peso não cabe na mochila ele é removido do array
	 # se não é colocado na mochila e depois removido do array
     if (pesoatual - max(aux1)) < 0:
         aux1.remove(max(aux1))
     else:
         pesoatual -= max(aux1)
         i = peso.index(max(aux1))
         mochila.append([i+1,peso[i],valor[i]])
         aux1.remove(max(aux1))

print('\n***** Condição Maior peso *****')
for i in mochila:
    print( f'Item  {i[0]} '
          f'peso  {i[1]} '
          f'valor {i[2]} ')
    ptotal += i[1]
    vtotal += i[2]
print(' Peso Total: {} '
      'Valor Total: {}'.format(ptotal,vtotal))

# Limpa os arrays para sere ultilizados na nova Condição
mochila.clear()
aux1.clear()
aux1 = peso[:]
pesoatual = pesomochila
ptotal = 0
vtotal = 0

while len(aux1) != 0:
	 # Se o maenor peso não cabe na mochila ele é removido do array
	 # se não é colocado na mochila e depois removido do array
     if (pesoatual - min(aux1)) < 0:
         aux1.remove(min(aux1))
     else:
         pesoatual -= min(aux1)
         i = peso.index(min(aux1))
         mochila.append([i+1,peso[i],valor[i]])
         aux1.remove(min(aux1))

print('\n***** Condição Menor Peso *****')
for i in mochila:
    print( f'Item  {i[0]} '
          f'peso  {i[1]} '
          f'valor {i[2]} ')
    ptotal += i[1]
    vtotal += i[2]
print(' Peso Total: {} '
      'Valor Total: {}'.format(ptotal,vtotal))

# Limpa os arrays para sere ultilizados na nova Condição	  
mochila.clear()
aux1.clear()
aux1 = valor[:]
pesoatual = pesomochila
ptotal = 0
vtotal = 0

while len(aux1) != 0:
	 
	 # Salva o indix do Maior valor
     i = valor.index(max(aux1))
	 # Se o peso não cabe na mochila ele é removido do array
	 # se não é colocado na mochila e depois removido do array
     if (pesoatual - peso[i]) < 0:
         aux1.remove(max(aux1))
     else:
         pesoatual -= peso[i]
         mochila.append([i+1,peso[i],valor[i]])
         aux1.remove(max(aux1))

print('\n***** Condição Maior Valor *****')
for i in mochila:
    print( f'Item  {i[0]} '
          f'peso  {i[1]} '
          f'valor {i[2]} ')
    ptotal += i[1]
    vtotal += i[2]
print(' Peso Total: {} '
      'Valor Total: {}'.format(ptotal,vtotal))

# Limpa os arrays para sere ultilizados na nova Condição	  
mochila.clear()
aux1.clear()
aux1 = valor[:]
pesoatual = pesomochila
ptotal = 0
vtotal = 0

while len(aux1) != 0:
# Salva o indix do Menor valor
    i = valor.index(min(aux1))
# Se o peso não cabe na mochila ele é removido do array
# se não é colocado na mochila e depois removido do array
    if (pesoatual - peso[i]) < 0:
        aux1.remove(min(aux1))
    else:
        pesoatual -= peso[i]
        mochila.append([i+1,peso[i],valor[i]])
        aux1.remove(min(aux1))

print('\n***** Condição Menor Valor *****')
for i in mochila:
    print( f'Item  {i[0]} '
          f'peso  {i[1]} '
          f'valor {i[2]} ')
    ptotal += i[1]
    vtotal += i[2]
print(' Peso Total: {} '
      'Valor Total: {}'.format(ptotal,vtotal))