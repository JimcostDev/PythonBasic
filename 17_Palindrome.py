"""palíndromo: es una palabra que se lee igual al derecho o al reves"""

"""Metodo insert: Básicamente su estructura es; insert(index, object), 
donde el index es la posición donde quieres poner el object, que sería la 
}letra. Si ya existe una letra en la posición indicada entonces corre 
}esa letra a la siguiente posición y la letra que indicamos al principio 
la acomoda en la posición indicada. Para .join() es más fácil, solamente 
concatena o une strings."""
def palindromeTwo(word):
    reversed_word = word[:: - 1]
    if reversed_word == word:
        return True
    return False


def palindrome(word):
    reversed_letters = []# lista para almacenar las letras invertidas

    for letter in word:
        reversed_letters.insert(0,letter)

    reversed_word = ''.join(reversed_letters) #invertir la palabra

    if reversed_word == word:
        return True
    return False

if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))

    result = palindromeTwo(word)
    if result is True:
        print('{} sí es palíndromo.'.format(word))
    else:
        print('{} no es palíndromo.'.format(word))

