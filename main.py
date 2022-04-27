from json.tool import main
from principalFuntions import dividir, multiplicar, restar, sumar

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

if opcCalc == "*":
    resultado = multiplicar(num1,num2)
elif opcCalc == "/":
    resultado = dividir(num1,num2)
elif opcCalc == "+":
    resultado = sumar(num1,num2)
elif opcCalc == "-":
    resultado = restar(num1,num2)

print (resultado)