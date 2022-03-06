#PRACTICA DE BOLEANOS
# print (10>9)
#print (9<20)
#print (5==4)
"""
a = 10 
b = 20
if a == b:
    print ("a es igual que 10")
else: 
    print ("a no es igual que b")"""

#Devuelve false cuando la lista este vacia o el valor de la variable sea 0 
"""def mifuncion ():
    return False 

if (mifuncion()):
    print ("el valor es verdadero")
else: 
    print ("el valor es falso")"""
#------------------------------------------------------------------------------------------------------------
# OPERADORES EN PYTHON 
# Operadores aritmeticos =-/*, 
# operadores de asignacion +=, -= igualmente con diferentes operaciones 
"""n = 3 
for x in range (0, 100):
    n += 1 # is the same to say n + 1 
    print ("n:",n)"""

# operadores de comparacion ==, >=, <= !=, <, > (igual a, mayor e igual, menor e igual, igual e diferente, mayor q, menor q,)
# == (de comparacion) = de asignacion a vlaor

import numbers


x = 20 
y = 20
z = 40

"""if x == y : #== 
    print ("yes")
else:
    print ("not")"""

# operadores logicos 
# and (todos los valores son verdaderos si no devuelve falso)
# or (si hay un verdadero true, si toodos son falsos devuelve falso.)
# not si no se cumplen los (parametros)
"""if not (x == y): 
    print ("yes")
else: 
    print ("not")"""

# operadores de identidad is, is not 

"""print (x is y) 
True"""
#devuelve true porque los valores tiene la misma identidad si no la tienen sera falso
"""print (z is not x)
True"""
# devuelve true por que z y x no tienen la misma identidad.

# operaddores de membresia 
# in (si una variable esta dentro de otra)
"""j = "Python"
l = "thon"
print (l in j)"""
# in not (no se encuentra la variable dentro de otra)
"""p = "Python"
q = "fgu"
print (q not in  p)"""
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#LISTAS [] - ordenados, modificables, si duplicados 
#SET - no ordenados, no indexados, no duplicados
#TUPLE () - ordenados, no modificables si duplicados 
#DICCIONARIO {} - no ordenados, modificable e indexados, no duplicados
colores = ["azul", "rojo", "verde", "morado", "negro", "blanco", "turquesa", "amarillo", "gris", "plateado", "dorado", "rosa"] # pueden haber listas boleans nums etc
color = input ("en que color quieress tu carro  ")
respuesta = input ("porfavor confirma: ")
p = False
if color in colores:
    print ("perfecto tu carro va a estar en el color", color)
    marcas = ["BMW", "Mercedes-Benz", "Audi", "Lexus", "Renault", "Ford", "Opel", "Seat"]
    marca = input (" que marca prefieres?  : ")
    if marca in marcas:
        print (f"tu auto va a ser un {marca} {color} {respuesta}")
        
        if (respuesta == "no" or respuesta == "si"):
            if  respuesta == "si":  
                print ("listo terminaste el cuestionario")
            elif respuesta == numbers:
                print ("no numeros")
            else:
                print ("respuestas validas si, no")
        else:
            print ("repite porfovor")
    else: 
        print ("no disponible en el inventario")
else: 
    print ("noencontrado en el inventtario")






