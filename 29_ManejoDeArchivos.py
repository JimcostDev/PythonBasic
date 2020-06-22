def run():
    # abrimos el archivo en modo escritura ('w')
    with open('numeros.txt', 'w') as filepy:
        # por cada numero del 0 hasta el 9
        for i in range(10):
            filepy.write(str(i))


if __name__ == '__main__':
    run()
