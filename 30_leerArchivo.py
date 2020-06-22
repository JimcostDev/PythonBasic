def run():
    with open('zen.txt') as filepy:
        #vamos a contar cuantas veces aparece la palabra mejor en el archivo zen
        for line in filepy:
            print(filepy.readlines())

if __name__ == '__main__':
    run()
