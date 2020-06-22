"""variable: contenedor de valores (es un espacio en memoria que almacena
 un valor y a lo largo de algoritmo su valor puede cambiar)
 script: basicamente significa que nuestro computo (codigo fuente), los podemos guardar en un archivo
  y luego ejecutar ese archivo como si lo hubieramos escrito directamente en la consola."""
concatenar = 'el area' + ' es:'
pi = 3.14159
radio = 3
area = pi * radio ** 2
print(concatenar, area)
# cambio de valor la variable radio
radio = 5
area = pi * radio ** 2
print(concatenar, area)
