import sys

def text_analyzer(texto=None):
    """Función llamada text_analyzer que toma como argumento una única cadena y muestra
    la suma de sus caracteres en mayúsculas, minúsculas, signos de puntuación y espacios.
    Argumentos:
    Texto -- La cadena que se va a analizar.
    Retorna:
    #None
    """
    if texto is None or texto == "":
        texto = input("Introduce una cadena de texto: ")
    if not isinstance(texto, str):
        print("Error: el argumento debe ser una cadena de texto.")
        return
    num_mayusculas = 0
    num_minusculas = 0
    num_puntuacion = 0
    num_espacios = 0
    for caracter in texto:
        if caracter.isupper():
            num_mayusculas += 1
        elif caracter.islower():
            num_minusculas += 1
        elif caracter.isspace():
            num_espacios += 1
        else:
            num_puntuacion += 1
    
    
    resultado = len(texto)
    print("El texto contiene " + str(resultado) + " caracteres(s):")
    print("Número de mayúsculas: ", num_mayusculas)
    print("Número de minúsculas: ", num_minusculas)
    print("Número de signos de puntuación: ", num_puntuacion)
    print("Número de espacios: ", num_espacios)

if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Error: You should enter one argument.")
        exit()
    elif len(sys.argv) > 1:
        texto = " ".join(sys.argv[1:])
        text_analyzer(str(texto))
        sys.exit()
    elif len(sys.argv) < 2:
        texto = " ".join(sys.argv[1:])
        text_analyzer(str(texto))
        sys.exit()
