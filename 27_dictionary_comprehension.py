cuadrados = {}
for num in range(1, 11):
    cuadrados[num] = num ** 2
print(cuadrados)
print("****************DICTIONARY_COMPREHENSION********************")
squares = {}
squares = {num: num ** 2 for num in range(1, 11)}
print(squares)
