# -*- coding: utf-8 -*-
def foreign_exchange_calculator_mex(ammount):
        mex_to_col_rate =   179.40
        return mex_to_col_rate * ammount
def foreign_exchange_calculator_col(ammount):
        col_to_mex_rate =   0.005575
        return col_to_mex_rate * ammount

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S')
    print('')
    print('1. Pesos mexicanos a colombianos')
    print('')
    print('2. Pesos colombianos a mexicanos')
    print('')
    print('Elige una opción')
    opt = int(input('opción 1 o opción 2: '))
    
    if opt == 1:
        ammount = float(input('Ingresa la catidad de pesos mexicanos que quieres convertir: '))
        #'${}' = concatenar
        # .format()= como parametros recibe las ${}', según las hallamos ordenado
        result = foreign_exchange_calculator_mex(ammount)
        print('${} pesos mexicanos equivalen a ${} pesos colombianos'.format (ammount,result) )
        print('')
        
    else:
        ammount = float(input('Ingresa la catidad de pesos colombianos que quieres convertir: '))
        result = foreign_exchange_calculator_col(ammount)
        print('${} pesos colombianos equivalen a ${} pesos mexicanos'.format (ammount,result) )
        print('')
        
        
        
        
    

     

if __name__ == '__main__':
    run()#comenzar en la funcion run()
    print('Final del programa')

"""Nota: El scope de una función es el ámbito de sus variables ya que cada vez que una función es ejecutada
en python se genera un contenedor bajo el nombre de la función que agrupara sus variables y esta s solo existen 
mientras la función se este ejecutando."""
