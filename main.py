from historial import agregar_historial, mostrar_historial
from operaciones_menu import mostrar_menu, sumar, restar, multiplicar, dividir


def calculadora ():
    while True:
        mostrar_menu()
        seleccion = input ("Ingrese una opcion del 0 a 5: ")
        if seleccion == '0' :
            print ("Saliendo de calculadora")
            break
        elif seleccion in ['1', '2','3','4','5'] :
            try:
                num1= float(input("Ingrese el primer numero: "))
                num2= float(input("Ingrese el segundo numero: "))
            except ValueError:
                print("Ingrese un valor valido")
                continue
            
            if seleccion == '1':
                resultado = sumar(num1, num2)
                operacion = f"{num1} + {num2} = {resultado} "
                agregar_historial(operacion)
                print(operacion)
            elif seleccion == '2':
                resultado = restar(num1, num2)
                operacion = f"{num1} - {num2} = {resultado} "
                agregar_historial(operacion)
                print(operacion)
            elif seleccion == '3':
                resultado = multiplicar(num1, num2)
                operacion = f"{num1} * {num2} = {resultado} "
                agregar_historial(operacion)
                print(operacion)
            elif seleccion == '2':
                resultado = dividir(num1, num2)
                operacion = f"{num1} / {num2} = {resultado} "
                agregar_historial(operacion)
                print(operacion)
        elif seleccion == '5':
            mostrar_historial()
        else:
            print ("Seleccion no valida, intente de nuevo")
            
if __name__== "__main__":
    calculadora()    
