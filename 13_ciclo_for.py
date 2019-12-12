"""iteración:
*las iteraciones permiten realizar la misma secuencia de pasos varias veces
*tambien permiten recorrer una secuencia(como un string)
in, break y continue hay que memorizarlas de corazón"""
for i in range(5,40,3):#comenzar iteración en 5 hasta 40(sin incluirlo) en saltos de 3
    print(i)
end = '******'
print(end)
#otro ejercicio
for i in range(30):
    if i % 3 != 0: #si la var i no es exactamente divisible entre 3
        continue
    else:
        print(i**2)#imprime los que son divisibles entre 3

print(end)

for i in range(30):
    if i % 3 == 0:
        print(i)
    elif i == 22:
        break #el ciclo se rompe aqui y no continu la iteración

