from json.tool import main
from principalFuntions import dividir, multiplicar, restar, resto, sumar, ifOpcionesMenu

main

print ("BIENVENIDO A LA CALCULADORA")

num1 = int(input("valor del primer numero: "))
num2 = int(input("valor del segundo numero: "))

print ("ELIJA LA OPCION QUE NECESITE: ")
print ("+ SUMAR ")
print ("- RESTAR ")
print ("/ DIVIDIR ")
print ("* MULTIPLICAR ")
opcCalc = input(" ")

print(ifOpcionesMenu(opcCalc,num1,num2))