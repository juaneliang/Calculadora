classmethod

def sumar(numero1, numero2):
    return numero1 + numero2

def restar(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    resultadoDivisionReal = numero1 / numero2
    return resultadoDivisionReal

def resto(numero1, numero2):
    resultadoDivisionResto = numero1 % numero2
    return resultadoDivisionResto

def ifOpcionesMenu(opcCalc,num1,num2):
    if opcCalc == "*":
        resultadoMultiplicacion = multiplicar(num1,num2)
        resultado = print ("el resultado de la multiplicacion es: " + str(resultadoMultiplicacion))
    elif opcCalc == "/":
        resultadoDivision = dividir(num1,num2)
        resultadoResto = resto(num1,num2)
        resultado = print ("el resultado de la division es: " + str(resultadoDivision) + " y el resultado del resto es: " + str(resultadoResto))
    elif opcCalc == "+":
        resultadoSuma = sumar(num1,num2)
        resultado = print ("el resultado de la multiplicacion es: " + str(resultadoSuma))
    elif opcCalc == "-":
        resultadoResta = restar(num1,num2)
        resultado = print ("el resultado de la multiplicacion es: " + str(resultadoResta))