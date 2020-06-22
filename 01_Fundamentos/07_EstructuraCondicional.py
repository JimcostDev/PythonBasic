45# -*- coding: utf-8 -*-
"""Las condiciones son sentencias que devuelven un valor booleano (True, False)
Podemos utilizar:
OPERADORES RELACIONALES:
== (es igual)
!= (es diferente)
> (es mayor que)
< (es menor que)
>= (es mayor o igual que)
<= (es menor o igual que)
OPERADORES LÓGICOS:
and
or
not
"""

def say_hello(age):
    if age > 18:
        return 'Hola señor'
    else:
        return 'Hola niño'

def run():
    age = int(input('¿Cual es tu edad?: '))
    result = say_hello(age)
    print(result)
if __name__ == '__main__':
    run()
    print('Fin del progrma')

