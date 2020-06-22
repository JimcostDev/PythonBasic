
#un número primo es aquel que unicamente es divisible por la unidad (1) y el mismo, por ejemplo el 7
def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else :
        for i in range(3, number):
            if number % i == 0:
                return False

    return True
def run():
    pass #keyword (es un placeholder, es decir por el momento la funcion esta vacia, pero en algun momento va adquirir un valor.
    number = int(input('Escribe un número entero: '))
    result = is_prime(number)

    if result is True:
        print('Tu número es primo')
    else:
        print('Tu número no es primo')

print(run())
if __name__ == '__main__':
    run()
"""Nota: Entre más profunda este de anidada una condicional, más dificil es de leer. Consejo, procurar siempre la 
legibilidad de tu programa"""
