import random
def run():
    number_found = False
    limit =  int(input('Ingresa el limite para generar el número aleatorio :'))
    random_number = random.randint(0,limit)#generar num aleatorio entre 0 y 20

    while not number_found:
        number = int(input('Intenta un número:'))

        if number == random_number:
            print('Feliciddes. Enontraste el número')
            number_found = True #validamos que se ha encontrado el número y la condición es falsa
        elif number > random_number:
            print('El número es menor')
        else:
            print('El número es mayor')


if __name__ == '__main__':
    run()