#Sumar 2 numeros
import os
os.system("cls || clear")
os.system("color a4")
try:
    num1 = eval(input("Por favor dime un numero: "))
    num2 = eval(input("Por favor dime otro numero: "))
    suma = num1 + num2
    print("La suma es: ", suma)
except Exception as ex:
    os.system("Color cf")
    print("Error, verifique y vuelva a intentar...")

