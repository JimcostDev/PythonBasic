class Lampara:
    _LAMPS = ['''
              .
         .    |    ,
          \   '   /
           ` ,-. '
        --- (   ) ---
             \ /
            _|=|_
           |_____|
        ''',
              '''
                   ,-.
                  (   )
                   \ /
                  _|=|_
                 |_____|
              ''']

    # metodo de instanciq (init, es el metodo constructor)
    def __init__(self, esta_encendida):
        # por convección usamos _ para especificar que mi variable y/o metodo es de tipo privado
        self._esta_encendida = esta_encendida

    def encendido(self):
        self._esta_encendida = True
        self._imagen_enPantalla()

    def apagado(self):
        self._esta_encendida = False
        self._imagen_enPantalla()

    def _imagen_enPantalla(self):
        if self._esta_encendida:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


def run():
    # instancia de la clase (objeto)
    lampara = Lampara(esta_encendida=False)
    while True:
        command = str(input('''
        ¿Que deseas hacer?
        
        [p] prender
        [a] apagar
        [s] salir
        '''))

        if command == 'p':
            lampara.encendido()
        elif command == 'a':
            lampara.apagado()
        else:
            break


if __name__ == '__main__':
    run()
