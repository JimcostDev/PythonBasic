from lamp import Lampara

# instancia de la clase (objeto)
lampara = Lampara(esta_encendida=False)
while True:
    command = str(input('''
        ¿Que deseas hacer?

        [p] prender
        [a] apagar
        [s] salir
        ...
        '''))

    if command == 'p':
        lampara.encendido()
    elif command == 'a':
        lampara.apagado()
    else:
        break

if __name__ == '__main__':
    run()
