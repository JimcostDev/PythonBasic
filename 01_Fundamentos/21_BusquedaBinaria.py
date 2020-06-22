def binary_search(numbers, number_to_find, low, high):
    #si en algun caso nuestro indice bajo se vuelve mas alto que nuestro indice mas alto, el numero no esta en la lista
    if low > high:
        return False

    mid = (low + high) // 2

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)



if __name__ == '__main__':
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    number_to_find = int(input('Ingresa un número para buscar en la lista: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El número sí está en la lista.')
    else:
        print('El número NO está en la lista.')