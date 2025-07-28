def esta_balanceada(expresion):
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}
    apertura = set(pares.values())


    print(f"\nProcesando: {expresion}")
    print("Pasos de la pila:")

    for i, simbolo in enumerate(expresion):
        if simbolo in apertura:
            pila.append(simbolo)
            print(f"  Paso {i+1}: Push '{simbolo}' → {pila}")
        elif simbolo in pares:
            if pila and pila[-1] == pares[simbolo]:
                pila.pop()
                print(f"  Paso {i+1}: Pop '{simbolo}' → {pila}")
            else:
                print(f"  Paso {i+1}: Error con '{simbolo}' → {pila}")
                print("Resultado: No balanceada")
                return False
                
    print("Resultado:", "Balanceada")

def procesar_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                linea = linea.strip()
                esta_balanceada(linea)
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")


procesar_archivo('/Users/javiercarredano/Documents/Teoria de la computacion/Laboratorio2TeoriaCompu/Ejercicio2/expresiones.txt')
