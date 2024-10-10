def mostrar_menu ():
    print("Seleccione una operación:")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Historial")
    print("0- Salir")
    
historial = []

def agregar_historial(operacion):
    historial.append(operacion)

def mostrar_historial():
    if historial:
        print("historial de operaciones")
        for operacion in historial :
            print (operacion)
    else:
        print(operacion)        
    
def sumar(x , y):
    return x + y

def restar(x , y):
    return x - y

def multiplicar(x , y):
    return x * y

def dividir(x , y):
    if y == 0:
        return "Error: Divicion por cero"
    return x / y

def calculadora ():
    while True:
        mostrar_menu
        seleccion = input ("Ingrese un opcion del 0 a 6: ")
        if seleccion == '0' :
            print ("Saliendo de calculadora")
            break
        elif seleccion in ['1', '2','3','4','5'] :
            try:
                num1= float(input("Ingrese el primer numero"))
                num2= float(input("Ingrese el segundo numero"))
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
