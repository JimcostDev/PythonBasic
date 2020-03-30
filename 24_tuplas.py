"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y
"""


def first_not_repeating_char(char_sequence):
    ver_letras = {}  # diccionario

    for idx, letra in enumerate(char_sequence):
        if letra not in ver_letras:
            ver_letras[letra] = (idx, 1)
        else:
            ver_letras[letra] = (ver_letras[letra][0], ver_letras[letra][1] + 1)

    final_letters = []
    for key, value in ver_letras.items():
        if value[1] == 1:
            final_letters.append((key, value[0]))

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return '_'


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))
