#funcion para multiplicar dos numeros
def product(num1, num2):
    return num1 *  num2

def main():
    num1 = int(input("Primer valor: "))
    num2 = int(input("Segundo valor: "))
    print("El producto es: ", product(num1, num2))
    
main()