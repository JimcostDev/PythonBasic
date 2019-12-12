#-*- coding: utf-8 -*-

"""Funcion: es una secuencia de comandos que realizan un computo (tambien llamadas metodos en otros lenguajes - Acciones del objeto).
Utilizamos la keyword def"""

#refactorizar: modicamos nuestro codigo, para evitar repeticiones
import turtle
def index(): #defenir funcion
    window = turtle.Screen()
    jimcost = turtle.Turtle()

    make_square(jimcost)
    turtle.mainloop()#evitar que se cierre(mantener ventana abierta)

def make_square(jimcost):
    length = int(input('Tamaño del cuadrado: '))
    for i in range(4):#realizar 4 lineas, con su respectivo giro
     make_line_and_turn(jimcost, length)

def make_line_and_turn(jimcost, length):
    jimcost.forward(length)
    jimcost.left(90)


"""si el nombre internamente de este archivo, python le llama main, y python  le llama main a los archivos que recorre 
cuando  ejecuta un nombre de archivo entonces ejecuta esta serie de instrucciones"""
if __name__ == '__main__':
    index()#estamos comenzando en la funcion index()






