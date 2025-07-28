def get_precedence(c):
    precedencia = {
        '(': 1,
        '|': 2,
        '.': 3,
        '?': 4,
        '*': 4,
        '+': 4,
        '^': 5
    }
    return precedencia.get(c, 6) 


def format_regex(regex):
    res = ""
    all_ops = {'|', '?', '+', '*', '.', '^'}
    binarios = {'*', '+', '?'}


    def is_operand(c):
        return c not in all_ops and c not in {'(', ')', '[', ']', '{', '}'}

    i = 0
    while i < len(regex) - 1:
        c1 = regex[i]
        c2 = regex[i + 1]
        res += c1

   
        if (
            (is_operand(c1) or c1 in binarios or c1 in {')', ']'}) and
            (is_operand(c2) or c2 in {'(', '['})
        ):
            res += '.'

        i += 1

    if i < len(regex):
        res += regex[-1]
    return res


def infix_to_postfix(regex):
    output = ''
    stack = []
    formatted = format_regex(regex)
    print(f"\nInfix original : {regex}")
    print(f"Infix formateado: {formatted}")
    print("Pasos de conversión:")

    for c in formatted:
        if c == '(':
            stack.append(c)
            print(f"Push '(': {stack}")
        elif c == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
                print(f"Pop hasta '(': salida = {output}, stack = {stack}")
            stack.pop()  
            print(f"Eliminar '(': {stack}")
        elif c in "|.+?^":
            while stack and get_precedence(stack[-1]) >= get_precedence(c):
                output += stack.pop()
                print(f"Pop por precedencia: salida = {output}, stack = {stack}")
            stack.append(c)
            print(f"Push operador '{c}': {stack}")
        else:
            output += c
            print(f"Añadir operando '{c}' a salida: {output}")

    while stack:
        output += stack.pop()
        print(f"Vaciar stack: salida = {output}")

    print(f"Postfix final  : {output}")
    return output

def procesar_archivo(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            lineas = [line.strip() for line in f if line.strip()]
            for linea in lineas:
                infix_to_postfix(linea)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta}'.")


procesar_archivo("/Users/javiercarredano/Documents/Teoria de la computacion/Laboratorio2TeoriaCompu/Ejercicio3/expresiones.txt")  