"""
Decorador: es una función que recibe como parametro otra función y modifica su comportamiento,
es decir retorna una tercera función.

Función: no es mas que un conjunto de instrucciones (lineas de codigo) que hacen una tarea en concreto,
y esta funcion puede retornar un valor o no.

cada vez que veamos encima de una funcion el simbolo @ siginifica que es un decorador.
"""


def protected(func):#A
    def wrapper(password):#B
        if password == 'jimcostdev':
            return func()#C
        else:
            print('La contraseña es incorrecta.')

    return wrapper

@protected
def protected_func():
    print('Tu contraseña es correcta.')


if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))
    protected_func(password)
