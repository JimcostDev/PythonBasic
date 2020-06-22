"""una lista es una secuencia de elementos, nos permite agrupar varios elementos en un solo lugar"""


def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps = sum_of_temps + float(temp)#sumar los valores de la lista

    return sum_of_temps / len(temps)#obtener promedio


if __name__ == '__main__':
    temps = [21, 24, 24, 22, 28, 23, 24]

    average = average_temps(temps)

    print('La temperatura promedio es: {}'.format(average.__round__(2)))




