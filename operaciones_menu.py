
def mostrar_menu ():
    print("Seleccione una operación:")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Historial")
    print("0- Salir")
 
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