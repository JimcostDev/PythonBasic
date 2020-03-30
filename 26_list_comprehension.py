print("*****************LISTA*******************")
pares = []
for num in range(1, 31):
    if num % 2 == 0:
        pares.append(num)
print("los números pares de la lista son: {}".format(pares))
print()
print("*****************LIST_COMPREHENSION*******************")
even = {}
even = [num for num in range(1, 31) if num % 2 == 0]
print("los números pares con list_comprehension son: {}".format(even))
