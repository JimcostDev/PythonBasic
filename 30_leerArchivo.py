def run():
    with open('zen.txt') as filepy:
        # vamos a contar cuantas veces aparece la palabra mejor en el archivo zen
        counter = 0
        for line in filepy:
            counter += line.count('mejor')

        print('Mejor se encuentra {} en el texto.'.format(counter))


if __name__ == '__main__':
    run()
