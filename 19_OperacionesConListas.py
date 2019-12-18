# unir listas (+)
lista = [1, 2, 3]

listaDos = [4, 5, 6]
listaTres = lista + listaDos
lista.extend(listaDos)

print('Unir listas: {}'.format(listaTres))
print('Unir listas: {}'.format(lista))

#multiplicar elementos
listaCuatro = [5]
listaCinco = listaCuatro * 10
print('multiplicar elementos {}'.format(listaCinco))
"""los operadores /(division) y -(resta) no puede utilizarse en cuando tenemos el tipo list
las listas soportan el operador de slices [:::]. punto de inicio, punto final y opcional de cada cuantos pasos."""

listaSeis = listaTres[1:3]#indice uno hasta 3
print('index 1 hasta el 3: {}'.format(listaSeis))

listaSiete =listaTres [0:6:2]#indice uno hasta 3 de 2 en 2
print('index 0 hasta el 6 de 2 en 2: {}'.format(listaSiete))

listaOcho = listaTres[::-1]#desde el inicio hasta el final invertida
print('desde el inicio hasta el final invertida: {}'.format(listaOcho))

listaOcho.append(9)#anadir elemento al final de  la lista
print('añadir elememto{}'.format(listaOcho))

listaOcho.pop()#eliminar ulttimo elemento de la lista
print('eliminar ultimo elememto{}'.format(listaOcho))

listaDesordenada = [5,7,9,2,1,4,3]
listaDesordenada.sort()
print('ordenar lista: {}'.format(listaDesordenada))

#eliminar elemento de la lista
utiles = ['borrador', 'lapiz', 'ega', 'cuaderno']
del utiles[2]
print(utiles)

#guardar un str en una lista
platzi = 'platzi'
lista_platzi = list(platzi)
print(lista_platzi)

#recontrir str
str_platzi = ''.join(lista_platzi)
print(str_platzi)