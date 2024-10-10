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
